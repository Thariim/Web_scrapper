"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Viktor Krchňavý
email: krchnavy.viktor@gmail.com
discord: Tharim
"""
import sys

from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs

from csv_writer import CSVWriter
from parameters import Parameters
from param_maker import ParamMaker

def validate_url(url):
    """
    Validates that the provided URL starts with either 'http://' or 'https://'.
    
    Args:
        url (str): The URL to validate.

    Raises:
        ValueError: If the URL does not start with a valid scheme.
    """
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError(f"Invalid URL: {url}. URL must start with http:// or https://")


def validate_file_name(file_name):
    """
    Validates that the provided file name ends with '.csv'.
    
    Args:
        file_name (str): The file name to validate.

    Raises:
        ValueError: If the file name does not end with '.csv'.
    """
    if not file_name.endswith(".csv"):
        raise ValueError(f"Invalid file name: {file_name}. File name must end with .csv")


def url_maker(url):
    """
    Fetches the main page HTML and extracts all the village URLs from the page.

    Args:
        url (str): The main URL to scrape from.

    Returns:
        dict: A dictionary where keys are village codes and values are URLs to village detail pages.
    """
    serv_response = requests.get(url)
    soup = bs(serv_response.text, 'html.parser')
    table_tag_top = soup.find_all("td", {"class": "cislo"})
    anchors = {}
    for td in table_tag_top:
        num_tag = td.text
        a_tag = td.find("a")
        if a_tag:
            full_url = urljoin(url, a_tag.get("href"))
            anchors[num_tag] = (full_url)

    return anchors


def url_diver(url_dict):
    """
    Fetches detailed information from individual village pages, creates Parameter objects, and collects them.
    
    Args:
        url_dict (dict): A dictionary where keys are village codes and values are village URLs.

    Returns:
        list: A list of Parameters objects containing village data.
    """
    parameter_objects = []
    for village_code, url in url_dict.items():
        try:
            serv_response = requests.get(url)
            serv_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data for village code {village_code}: {e}")
            continue
        soup = bs(serv_response.text, 'html.parser')
        param_maker = ParamMaker(soup)
        village_name = param_maker.name_maker()
        voters = param_maker.voters_maker()
        envelopes = param_maker.envelopes_maker()
        votes = param_maker.votes_maker()
        parties = param_maker.party_maker()
        parameters = Parameters(village_code, village_name, voters , envelopes, votes, parties)
        parameter_objects.append(parameters)
    return parameter_objects


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Something's wrong.")
        sys.exit(1)
        
    else:
        url = sys.argv[1]
        file_name = sys.argv[2]
        try:
            validate_url(url)
            validate_file_name(file_name)
            result = url_diver(url_maker(url))
            if not result:
                print("No data was retrieved.")
                sys.exit(1)
            csv_writer = CSVWriter(file_name)
            csv_writer.write(result)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

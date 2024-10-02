class ParamMaker:
    def __init__(self, soup):
        """
        Initialize with a BeautifulSoup object.
        
        Args:
            soup (BeautifulSoup): BeautifulSoup object containing the HTML content.
        """
        self.soup = soup

    def number_maker(self, num):
         """
        Extract the number from the HTML.
        
        Returns:
            int: Number of voters or None if not found.
        """
         try:
            td_elements = self.soup.find_all("td", {'headers': num})
            if td_elements:
               return int(td_elements[0].text.strip().replace('\xa0', ''))
            return None
         except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)

    def name_maker(self):
        """
        Extract the village name from the HTML.
        
        Returns:
            str: Village name or None if not found.
        """
        target_value = 'Obec:'

        return next(
                    (h3.text.replace(target_value, '').strip()
                    for h3 in self.soup.find_all("h3")
                    if target_value in h3.text),
                    None
        )

    def voters_maker(self):
        """
        Extract the number of voters from the HTML.
        
        Returns:
            int: Number of voters or None if not found.
        """
        td_elements = self.soup.find_all("td", {'headers': 'sa2'})
        if td_elements:
            return int(td_elements[0].text.strip().replace('\xa0', ''))
        return None

    def envelopes_maker(self):
        """
        Extract the number of envelopes from the HTML.
        
        Returns:
            int: Number of envelopes or None if not found.
        """
        td_elements = self.soup.find_all("td", {'headers': 'sa3'})
        if td_elements:
            return int(td_elements[0].text.strip().replace('\xa0', ''))
        return None

    def votes_maker(self):
        """
        Extract the number of votes from the HTML.
        
        Returns:
            int: Number of votes or None if not found.
        """
        td_elements = self.soup.find_all("td", {'headers': 'sa6'})
        if td_elements:
            return int(td_elements[0].text.strip().replace('\xa0', ''))
        return None

    def party_maker(self):
        """
        Extract the party names and their votes from the HTML.
        
        Returns:
            dict: Dictionary of party names and their respective votes.
        """
        party_names = self.soup.find_all("td", {"class": "overflow_name"})
        party_votes = self.soup.find_all("td", {"headers": "t1sa2 t1sb3"})

        parties= [(name.text.strip() , int(vote.text.strip().replace('\xa0', '').replace(' ', ''))) for name, vote in zip(party_names, party_votes)]

        return parties

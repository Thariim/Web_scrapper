Popis projektu:

Tento projekt slouží k extrahování výsledků z parlamentích voleb v roce 2017.

Instalace knihoven:

Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt . Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spusti následovně:
pip install -r requirements.txt

Spouštění projektu:

Pro spuštění projektu je nutné do příkazového řádku zadat:

python web_scrapper.py "URL" "název.csv"

URL: URL stránky která obsahuje data obcí.
název.csv: Název souboru kam budou data uložena (musí končit .csv).

Struktura projektu:

web_scrapper.py: # Hlavní script pro spuštění scrapperu a export dat do csv.

param_maker.py: # Definuje ParamMaker class pro extrahování dat z HTML.

parameters.py: # Definuje Parameters class pro uložení dat vesnic.

requirements.txt: # List použitých knihoven.

README.md: # Dokumentace.


Ukázka projektu:
Výsledky hlasování pro okres Beroun:
1. Argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2106
2. Argument: elections.csv

Spouštění programu:
python web_scrapper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2106" "elections.csv"

Code,Name,Voters,Envelopes,Votes,Občanská demokratická strana.......
534421,Bavoryně,239,151,150,18,0,0,6,0,8,7,5,2,4,0,0,16
531057,Beroun,14804,9145,9076,1363,16,11,576,1,433,651,140,78,205,8,12,1290
......


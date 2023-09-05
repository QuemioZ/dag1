print('Start van de scraping applicatie')

from bs4 import BeautifulSoup
import requests

pagina =  request.get('https://www.bitcoinmeester.nl')

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')
tabel = heeldehtml.find('div') #tbody werkte niet?

print(tabel.prettify())

bitcoinprijs = heeldehtml.find(id_="price1")
print('Prijs van de bitcoin = ' + bitcoinprijs)
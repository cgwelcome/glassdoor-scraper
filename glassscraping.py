import requests
from bs4 import BeautifulSoup

class Parser:

    def __init__(self, raw):
        self.soup = BeautifulSoup(raw, "html.parser")

class GlassDoorParser(Parser):
    
    def to_dict(self):
        info = {
            'company': self.company,
            'headquarter': self.headquarter,
            'no_reviews': self.no_reviews,
            'no_jobs': self.no_jobs,
            'no_interviews': self.no_interviews,
            'review_score': self.review_score
        }
        return info
    
    @property
    def company(self):
        return self.soup.find('h1', class_=" strong tightAll").get_text(strip=True)
    
    @property
    def website(self):
        return self.soup.find('span', class_="value website").contents[0].get('href')

    @property
    def headquarter(self):
        return self.soup.find('label', text="Headquarters").next_sibling.get_text(strip=True)

    @property
    def no_reviews(self):
        return self.soup.find_all('span', class_="num h2")[1].get_text(strip=True)
    
    @property
    def no_jobs(self):
        return self.soup.find_all('span', class_="num h2")[2].get_text(strip=True)
        
    @property
    def no_interviews(self):
        return self.soup.find_all('span', class_="num h2")[3].get_text(strip=True)
        
    @property
    def review_score(self):
        return self.soup.find('div', class_="ratingNum").get_text(strip=True)


class Client:
    
    def __init__(self):
        self.headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36' }
        self.session = requests.Session()
    
    def get(self, website):
        return self.session.get(website, headers=self.headers)
        
    
website = 'https://www.glassdoor.ca/Overview/Working-at-Media-10-EI_IE1079906.11,19.htm'
client = Client()
response = client.get(website)
parser = GlassDoorParser(response.text)
print(parser.company)
print(parser.website)
print(parser.no_reviews)
print(parser.to_dict())

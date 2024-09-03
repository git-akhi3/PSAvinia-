import requests
from bs4 import BeautifulSoup
faculty_name='Ashish vaswani'
def scrape_google_scholar(faculty_name):
    search_url = f"https://scholar.google.com/scholar?q={faculty_name}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    publications = []
    for result in soup.select('.gs_ri'):
        title = result.select_one('.gs_rt').text
        link = result.select_one('.gs_rt a')['href']
        snippet = result.select_one('.gs_rs').text
        publications.append({"title": title, "link": link, "snippet": snippet})
    print(publications)
    return publications

scrape_google_scholar(faculty_name)

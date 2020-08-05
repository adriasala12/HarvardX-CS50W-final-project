import requests
import urllib

apiKey = 'AIzaSyDFfXEM1ApgkSRCkUnnFBlgk67D6DS9fhU'

def getBooksByTitle(title):
    
    query = urllib.parse.quote(title)
    print(f"query: {query}")
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&key={apiKey}')
    data = response.json()
    print(data['items'][0])
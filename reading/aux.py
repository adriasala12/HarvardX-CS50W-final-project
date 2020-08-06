import requests
import urllib

apiKey = 'AIzaSyDFfXEM1ApgkSRCkUnnFBlgk67D6DS9fhU'

class Book():

    def __init__(self, gid, title, authors, publisher, pubdate, pages, thumbnail):
        self.gid = gid
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.pubdate = pubdate
        self.pages = pages
        self.thumbnail = thumbnail


def getBooksByTitle(title):
    
    query = urllib.parse.quote(title)
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&key={apiKey}')
    data = response.json()
    
    books = []

    try:
        for item in data['items']:
            try:
                book = Book(item['id'], item['volumeInfo']['title'], 
                    item['volumeInfo']['authors'], 
                    item['volumeInfo']['publisher'], 
                    item['volumeInfo']['publishedDate'],
                    item['volumeInfo']['pageCount'],
                    item['volumeInfo']['imageLinks']['thumbnail'])

                books.append(book)
            except:
                pass
    except:
        pass

    return books
        
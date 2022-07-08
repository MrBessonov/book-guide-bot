import books_dict
import requests
from bs4 import BeautifulSoup

book_info = {'title': '', 'author': '', 'mark': '', 'annotation': '', 'cover': ''}


def soup_func(message, book_type="e-paper"):
    num = books_dict.books[message.text][2]
    book_info['title'] = books_dict.books[message.text][0]
    book_info['author'] = books_dict.books[message.text][1]
    book_url = f"http://fantlab.ru/work{num}"

    book_request = requests.get(book_url)
    book_content = book_request.content

    soup_mark = BeautifulSoup(book_content, "html.parser")
    mark = soup_mark.find_all("div", {"class": "rating-block"})
    mark = mark[0].find("span", {"itemprop": "ratingValue"}).text
    book_info['mark'] = mark

    soup_anno = BeautifulSoup(book_content, "html5lib")
    anno = soup_anno.find_all("div", {"class": "p-block"})
    anno = anno[0].find("span", {"itemprop": "description"}).text.replace("\n", " ")
    book_info['annotation'] = anno

    soup_cover = BeautifulSoup(book_content, "html5lib")
    editions_rus = soup_cover.select(f'div.e-lang1.{book_type} img')
    links = [edition['src'] for edition in editions_rus]
    cover = "http:" + links[-1].replace("small", "big")
    book_info['cover'] = cover
    return book_info

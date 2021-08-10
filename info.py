import openpyxl
import json
from urllib.request import urlopen

while True:

    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    isbn = input("Enter ISBN: ").strip()

    #Open URL with ISBN
    resp = urlopen(api + isbn)
    #JSON into py
    book_data = json.load(resp)

    
    #vars to search for
    volume_info = book_data["items"][0]["volumeInfo"]
    author = volume_info["authors"]
    genre = volume_info["categories"]
    #More Readable author info
    readable_author = author if len(author) > 1 else author[0]

    excel_file = ["C:\Users\ddaga\Desktop\Assorted\Projects\BookShelf_Analysis\bookshelf.xlsx"]
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook['Library']
    
    isbn = worksheet['']

    row = 1
    col = 0

    worksheet.write(row, col, isbn)
    worksheet.write(row, col + 1, {volume_info['title']})
    worksheet.write(row, col + 2, {readable_author})
    worksheet.write(row, col + 3, {volume_info['pageCount']})
    worksheet.write(row, col + 4, {volume_info['publishedDate']})
    worksheet.write(row, col + 5, {volume_info['categories']})

    workbook.close()

    #print(f"\nTitle: {volume_info['title']}")
    #print(f"Author: {readable_author}")
    #print(f"Page Count: {volume_info['pageCount']}")
    #print(f"Publication Date: {volume_info['publishedDate']}")
    #print(f"Genres: {volume_info['categories']}")
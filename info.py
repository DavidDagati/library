import pandas as pd
import numpy as np
import json
import urllib.request
import textwrap


def to_str(var):
    return str(list(np.reshape(np.asarray(var),(1, np.size(var)))[0]))[1:-1]

while True:

    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    csv_file = (r'C:\Users\ddaga\Desktop\Assorted\Projects\BookShelf_Analysis\bookshelf.csv')
    df = pd.read_csv(csv_file)

    column_names = ["ISBN", "Title", "Author", "Page Count", "Published Date", "Genres"]

    book_info = pd.DataFrame(columns = column_names)

    for index, row in df.iterrows():
        
        isbn = df['isbn'][index]
        #Open URL with ISBN
        #resp = urlopen(api + to_str(isbn))
        #JSON into py
        #book_data = json.load(resp)

        with urllib.request.urlopen(api + to_str(isbn)) as f:
            text = f.read()

        decoded_text = text.decode("utf-8")
        obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
        volume_info = obj["items"][0] 
        authors = obj["items"][0]["volumeInfo"]["authors"]
     

        #vars to search for

        #print("\nTitle:", volume_info["volumeInfo"]["title"])
        #print("\nSummary:\n")
        #print(textwrap.fill(volume_info["searchInfo"]["textSnippet"], width=65))
        #print("\nAuthor(s):", ",".join(authors))
        #print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
        #print("\nPage count:", volume_info["volumeInfo"]["pageCount"])


        #volume_info = book_data["items"][0]["volumeInfo"]
        #author = volume_info["authors"]
        #genre = volume_info["categories"]
        #More Readable author info
        #readable_author = author if len(author) > 1 else author[0]

        isbn_row = {"ISBN": isbn, "Title": volume_info["volumeInfo"]["title"], "Author(s)": ",".join(authors), "Page Count": volume_info["volumeInfo"]["pageCount"], "Published Date": volume_info["volumeInfo"]['publishedDate'], "Genres": volume_info["volumeInfo"]['categories']}
        
        book_info.loc[len(book_info)] = isbn_row

    book_info.head()


        #book_info.append([[{volume_info['title']}, {readable_author}, {volume_info['pageCount']}, {volume_info['publishedDate']}, {volume_info['categories']}]])
    
    #book_info.toCSV = "book_info_output.csv"

    #isbn = input("Enter ISBN: ").strip()
   







    #worksheet.write(row, col, isbn)
    #worksheet.write(row, col + 1, {volume_info['title']})
    #worksheet.write(row, col + 2, {readable_author})
    #worksheet.write(row, col + 3, {volume_info['pageCount']})
    #worksheet.write(row, col + 4, {volume_info['publishedDate']})
    #worksheet.write(row, col + 5, {volume_info['categories']})

    #workbook.close()

    #print(f"\nTitle: {volume_info['title']}")
    #print(f"Author: {readable_author}")
    #print(f"Page Count: {volume_info['pageCount']}")
    #print(f"Publication Date: {volume_info['publishedDate']}")
    #print(f"Genres: {volume_info['categories']}")


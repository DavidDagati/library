import pandas as pd

csv_file = (r'C:\Users\ddaga\Desktop\Assorted\Projects\BookShelf_Analysis\bookshelf.csv')
df = pd.read_csv(csv_file)

column_names = ["isbn"]
book_info = pd.DataFrame(columns = column_names)

print(len(df))

for index, row in df.iterrows():
    isbn = df['isbn'][index]

    print(isbn)
    print("next")
    isbn_row = {"isbn": isbn}
   
    book_info.loc[len(book_info)] = isbn_row

print(book_info.head())
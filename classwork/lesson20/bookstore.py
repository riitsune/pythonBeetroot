'''
Create an application for a small bookstore. Your application would store data about available items in stock - books, magazines and other related goods like notebooks, postcards etc.
Main functionality of your application is to track sales and available items quantity. Make sure your application supports stock replenishment.
Also it might be useful to have an easy way to calculate total cost of goods sold for some period (day, week, month).
For books application would keep some additional information like author, the genre of the book, year of publishing, optional short description.
For magazines we’re interested to know the month of its publication and possible target audience (children, adults, scientists, gardeners etc.)
Use sqlite database for your data storage.

'''


import sqlite3



class Item:
    @classmethod
    def create_table(cls, conn):
        with conn:
            conn.cursor().execute("""CREATE TABLE IF NOT EXISTS items  (
                name text,
                type text,
                price integer,
                quantity integer            
                )""")

    def __init__(self, name,item_type, price, quantity):
        self.name = name
        self.item_type = item_type
        self.price = price
        self.quantity = quantity


    def add_item(self, conn):
        with conn:
            c = conn.cursor()
            c.execute("SELECT name, quantity FROM items WHERE name = :name and type =:type"  , {'name': self.name, 'type':self.item_type} )
            results = c.fetchall()
            print(results)
            c.execute(f"""INSERT INTO items VALUES (:name, :type, :price, :quantity)""",
              {'name': self.name, 'type': self.item_type, 'price': self.price, 'quantity': self.quantity })




class Book(Item):
    def __init__(self, name, price, quantity, author, genre, year):
        super().__init__(name, "Book", price, quantity)
        self.author = author
        self.genre = genre
        self.year = year


class Magazine(Item):
    def __init__(self, name, price, quantity, month, target_audience):
        super().__init__(name, "Magazine", price, quantity)
        self.month = month
        self.target_audience = target_audience


if __name__ == "__main__":
    postcard1 = Item("Happy New Year", "postcard", 5, 1)
    book1 = Item("1984", "book", 140, 5)
    conn = sqlite3.connect('bookstore.db')
    c = conn.cursor()

    Item.create_table(conn)
    postcard1.add_item(conn)
    book1.add_item(conn)

    # c.execute("SELECT * FROM items")
    # print(c.fetchall())
    #
    # c.execute("SELECT price, quantity FROM items ")
    # print(c.fetchall())



# def insert_pers(pers):
#     with conn:
#         c.execute(f"""INSERT INTO persons VALUES (:name, :age, :gender)""",
#                   {'name': pers.name, 'age': pers.age, 'gender': pers.gender})

#
# def get_pers_by_gender(gender):
#     c.execute("SELECT * FROM persons WHERE gender = :gender", {'gender': gender})
#     return c.fetchall()

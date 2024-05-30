import sqlite3

conn = sqlite3.connect('book_db.sqlite')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE books (
#             id  INTEGER PRIMARY KEY AUTOINCREMENT,
#             title VARCHAR(50),
#             author VARCHAR(100),
#             price FLOAT);
#     ''')
conn.commit()

#N1
# author_value = "William Shakespeare"
# results = cursor.execute("SELECT * FROM books WHERE author=:author_name",
#                          {'author_name': author_value}).fetchall()
#
# for row in results:
#     print(row)


#N2
# results = cursor.execute("SELECT * FROM books WHERE author = 'William Shakespeare' or author = 'Rowling'").fetchall()
#
# for row in results:
#     print(row)


#N3
# pr_value = 20
# results = cursor.execute("SELECT * FROM books WHERE price<=?", (pr_value, ))
#
# for row in results:
#     print(row)


#N4
# results = cursor.execute("SELECT DISTINCT author FROM books").fetchall()
#
# for row in results:
#     print(row)


#N5
# pr_balance = 100
# results = cursor.execute("SELECT * FROM users WHERE balance>=?", (pr_balance, ))
#
# for row in results:
#     print(row)


#N6
# results = cursor.execute("SELECT b.*, p.purchase_date "
#                          "FROM purchase p "
#                          "JOIN books b "
#                          "ON p.book_id = b.id "
#                          "where cast(strftime('%Y', p.purchase_date) AS INTEGER) < 2018")
#
# for row in results:
#     print(row)

#N7
# results = cursor.execute("SELECT u.*, p.purchase_date "
#                          "FROM users u "
#                          "JOIN purchase p "
#                          "ON u.id = p.user_id "
#                          "WHERE cast(strftime('%Y', p.purchase_date) AS INTEGER) = 2018")
#
# for row in results:
#     print(row)

#N8
# results = cursor.execute("SELECT DISTINCT(u.id), u.username, u.balance "
#                          "FROM users u "
#                          "JOIN purchase p "
#                          "ON u.id = p.user_id")
#
# for row in results:
#     print(row)

#N9
# results = cursor.execute("SELECT DISTINCT(book_id), b.title, b.author, b.price "
#                          "FROM books b "
#                          "JOIN purchase p "
#                          "ON b.id = p.book_id")
#
# for row in results:
#     print(row)

#N10
results = cursor.execute("SELECT b.* FROM books b "
                         "LEFT JOIN purchase p "
                         "ON b.id = p.book_id "
                         "WHERE p.book_id IS NULL")

for row in results:
    print(row)

conn.close()

import sqlite3

con = sqlite3.connect('D:/byak/Project Q/blizzard_scraper/blizzard_scraper/spiders/base.db')
cur = con.cursor()

#cur.execute('''CREATE TABLE IF NOT EXISTs stocks
#               (date text)''')

#cur.execute("INSERT INTO stocks VALUES ('2006-01-05')")

#con.commit()

for row in cur.execute('SELECT * FROM winners'):
        print(row)
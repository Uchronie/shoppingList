import sqlite3

if __name__ == "__main__":
	db = sqlite3.connect('db/db.db')
	cursor = db.cursor()
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS categories(
	     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	     name TEXT
	)""")
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS units(
	     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	     name TEXT
	)""")
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS items(
	     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	     name TEXT,
	     idCategories INTEGER,
		 idUnits INTEGER,
		 FOREIGN KEY(idCategories) REFERENCES categories(id),
		 FOREIGN KEY(idUnits) REFERENCES units(id)
	)""")
	datas = ["l", "cl", "ml", "kg", "g", "mg"]
	for data in datas:
	    cursor.execute('''INSERT INTO units (name) VALUES (?)''', (data,))
	db.commit()

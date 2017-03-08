import sqlite3

## Not as abstract as I would like... For generalizing, a SQL parser
## is required. So up to know, a specific model according to our pourpose
## is implemented below.


class DBMS:
	
	def __init__(self, db_name="netflix_and_chill.db"):
		# Connection to database
		self.db_name = db_name
		self.connection = sqlite3.connect(db_name)
		self.cursor = self.connection.cursor()
		
		# Table's creation
		sql = """
		CREATE TABLE IF NOT EXISTS netflix_and_chill (
			id_chat INTEGER NOT NULL,
			movie_id INTEGER NOT NULL,
			movie_name VARCHAR(50) NOT NULL,
			PRIMARY KEY ( id_chat, movie_id))"""
		
		if self.cursor.execute(sql): print "Table created with success"
		else: print "Error while creating table"
		
		# Exiting properly...
		self.cursor.close()
		self.connection.commit()
		self.connection.close()

	# Row should be a tuple of parameters respecting types of the table
	def insert_row(self, row):
		self.connection = sqlite3.connect(self.db_name)
		self.cursor = self.connection.cursor()
		sql = """
		INSERT INTO netflix_and_chill( id_chat, movie_id, movie_name)
		VALUES (?, ?, ?) """
			
		if self.cursor.execute(sql, row): print "Row inserted"
		else: print "Error inserting row"
		
		# Exiting properly...
		self.cursor.close()
		self.connection.commit()
		self.connection.close()
		
	# Get movies from a chat ! (For example... :P)
	def get_rows(self, chat_id, number_of_movies):
		self.connection = sqlite3.connect(self.db_name)
		self.cursor = self.connection.cursor()
		sql = """SELECT * FROM netflix_and_chill WHERE id_chat = ? LIMIT ?;"""
		arguments = (chat_id, number_of_movies)
		self.cursor.execute(sql, arguments)
		rows = self.cursor.fetchall()
		movies = []
		for row in rows:
			movies.append(row[2]) # just the name
		# Exiting properly...
		self.cursor.close()
		self.connection.commit()
		self.connection.close()
		
		return movies
import sqlite3

with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS posts(Title TEXT, Post TEXT)")

	# Insert some dummy data
	c.execute("INSERT INTO posts VALUES('Today', 'I feel pretty good.')")
	c.execute("INSERT INTO posts VALUES('Tomorrow', 'I wonder what the day holds.')")
	c.execute("INSERT INTO posts VALUES('Next Year', 'I shall be king.')")

	
#Runs the web server, uses web.py
import web
import json
import sqlite3 as sql
import pickle

urls = ('/', "index", "/jquery", "jquery", "/edit", "edit")
database = "./data/main.db"

class index:
	def GET(self):
		html = open("./index.html").read()
		return html
	def POST(self):
		pass
class edit:
	def POST(self):
		editing = str(web.input()).split("'")[1]
		cursor = sql.connect(database).cursor()
		try:
			cursor.execute("update users set editing='" + str(editing) + "' where name='John Smith'")
		except:
			cursor.execute("insert into users values('John Smith', '0', '" + pickle.dumps([]) + "')")
		print(editing)

class jquery:
	def GET(self):
		html = open("./jquery.js").read()
		return html

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

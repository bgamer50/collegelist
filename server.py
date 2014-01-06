#Runs the web server, uses web.py
import web
import json
import sqlite3 as sql

urls = ('/', "index", "/jquery", "jquery")
database = "./data/main.db"

class index:
	def GET(self):
		html = open("./index.html").read()
		return html
	def POST(self):
		pass

class jquery:
	def GET(self):
		html = open("./jquery.js").read()
		return html

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

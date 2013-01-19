import web
import urls

db = web.database(dbn = 'mysql', user = 'root', pw='root', db = 'tweet')
render = web.template.render("/templates")

if __name__ == "__main__":
	app = web.application(urls.urls, globals())
	app.run()

class tweet :
	def POST(self):
		i = web.input()
		db.insert('tweet',text=i.tweet)		
		raise web.seeother('/')
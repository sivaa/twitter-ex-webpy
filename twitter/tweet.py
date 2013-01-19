import web

render = web.template.render('templates/')
db = web.database(dbn = 'mysql', user = 'root', pw='root', db = 'twitter')

class new:
	def GET(self):
		return render.base(render.new())

	def POST(self):
		i = web.input()
		db.insert('tweet',text = i.tweet)		
		raise web.seeother('/')

class list:
	def GET(self):
		tweets = db.select('tweet')
		return render.base(render.home(tweets))

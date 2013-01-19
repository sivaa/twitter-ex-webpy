import web
import main

render = web.template.render('templates/')
db = web.database(dbn = 'mysql', user = 'root', pw='root', db = 'twitter')

class new:
	def GET(self):
		session = main.get_session()
		if 'username' in session:
			return render.base(render.new())
		else:
			return render.base(render.login())
		

	def POST(self):
		i = web.input()
		db.insert('tweet',text = i.tweet)		
		raise web.seeother('/')

class list:
	def GET(self):		
		tweets = db.select('tweet')
		return render.base(render.home(tweets))

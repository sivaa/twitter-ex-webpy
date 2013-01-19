import web
from main import get_session, get_render, get_db
session = get_session()
render = get_render()
db = get_db()

class login:
	def GET(self):
		return render.base(render.login(), session)
	def POST(self):
		input = web.input()
		result = db.query("SELECT * FROM auth WHERE username = $username AND password = $password", 
						{
						'username': input.username,
						'password': input.password
						})
		if result:
			session.username = input.username
			return web.seeother("/")
		else:
			return render.base(render.login(), session)

class register:
	def GET(self):
		return render.base(render.register(), session)
	def POST(self):
		input = web.input()
		db.insert("auth", username = input.username, password = input.password)
		return web.seeother("/login")

class logout:
	def GET(self):
		session.kill()
		return web.seeother("/")

import web
import urls

render = web.template.render('templates/')
db = web.database(dbn = 'mysql', user = 'root', pw='root', db = 'twitter')


app = web.application(urls.urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
    web.config._session = session
else:
    session = web.config._session

def get_session():
	return session

def get_render():
	return render
def get_db():
	return db


if __name__ == "__main__":
	app.run()


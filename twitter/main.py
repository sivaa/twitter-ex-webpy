import web
import urls

app = web.application(urls.urls, globals())


if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
    web.config._session = session
else:
    session = web.config._session

def get_session():
	return session

if __name__ == "__main__":
	app.run()


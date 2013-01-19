import web
import urls

if __name__ == "__main__":
	app = web.application(urls.urls, globals())
	app.run()


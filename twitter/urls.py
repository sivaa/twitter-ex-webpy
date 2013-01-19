import web

urls = (
		 '/', 'tweet.list',
		 '/login', 'auth.login',
		 '/logout', 'auth.logout',		 
		 '/register', 'auth.register',
		 '/new', 'tweet.new',
		 '/user/(.*)', 'tweet.user_list',
		 '/follow/(.*)', 'tweet.follow',
	)
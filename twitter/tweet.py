import web
from main import get_session, get_render, get_db
session = get_session()
render = get_render()
db = get_db()

class new:
	def GET(self):
		if 'username' in session:
			print session.username
			return render.base(render.new(), session)
		else:
			return render.base(render.login(), session)

	def POST(self):
		i = web.input()
		db.insert('tweet',text = i.tweet, username = session.username)		
		raise web.seeother('/')

class follow:
	def GET(self, followed_user):
		db.insert('follower', followed_user = followed_user, followed_by = session.username)		
		raise web.seeother('/')

class list:
		def GET(self):	
			if 'username' in session:		
				follows = db.query("SELECT * from follower WHERE followed_by = $u", {'u' : session.username})
				flist = []
				for f in follows :
					flist.append(f.followed_user)
				flist_str = "','".join(flist)
				flist_str = "'" + flist_str + "'"
				tweets = db.query("SELECT * FROM tweet WHERE username IN (" + flist_str + ")")
			else :
				tweets = db.select('tweet')		
			return render.base(render.home(tweets, get_followers(session), get_following(session), follow_suggestions(session)), session)

class user_list:
	def GET(self, username):
		tweets = db.query("SELECT * FROM tweet WHERE username = $username", 
						{'username': username})
		return render.base(render.home(tweets, get_followers(session), get_following(session), follow_suggestions(session)), session)

def get_followers(session):
	if 'username' in session:	
		followers = db.query("SELECT * FROM follower WHERE followed_user = $username", 
						{'username': session.username})
		return followers
	else:
		return None

def get_following(session):
	if 'username' in session:	
		following = db.query("SELECT * FROM follower WHERE followed_by = $username", 
						{'username': session.username})
		return following
	else:
		return None



def follow_suggestions(session):
	if 'username' in session:	
		following_obj_list = db.query("SELECT * FROM follower WHERE followed_by = $username", 
						{'username': session.username})
		following_list = [session.username, ]
		for following in following_obj_list:
			following_list.append(following.followed_user)
		following_list_str =  "','".join(following_list)
		following_list_str = "'" +  following_list_str + "'"
		following_suggestion_obj_list = db.query("SELECT * FROM auth WHERE username NOT IN (" + following_list_str + ")")

		following_suggestion_list = []
		for following_suggestion in following_suggestion_obj_list:
			following_suggestion_list.append(following_suggestion.username)
		return following_suggestion_list
	else:
		return None
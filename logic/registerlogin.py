import tornado.web
from pycket.session import SessionMixin


#authenticated
class AuthBaseHandler(tornado.web.RequestHandler,SessionMixin):
   def get_current_user(self):
	return self.session.get('user',None)

# user register
class RegisterHandler(AuthBaseHandler):
  def get(self, *args, **kwargs):
	print('register')
	self.render('register.html')

  def post(self, *args, **kwargs):
	print('registerpost')
	username = self.get_argument('username','')
	password1 = self.get_argument('password1','')
	password2 = self.get_argument('password2','')

	if username and password1 and (password1 == password2):
		pass
	else:
		self.write({'msg':'register fail'})

# user login
class LoginHandler(AuthBaseHandler):
  def get(self,*args,**kwargs):
	if self.current_user:
		self.redirect('/') 
	else:
		nextname = self.get_argument('next','') 
		self.render('login.html',nextname = nextname)

  def authenticate(self,user,passwd):
	return True	

  def post(self,*args,**kwargs):
	username = self.get_argument('username',None)
	password = self.get_argument('password',None)

	passed = authenticate(username,password)

	if passed:
		self.session.set('user',username)
		next_url = self.get_argument('next', '')

		if next_url:
		  self.redirect(next_url)
		else:
		  self.redirect("/")
	else:
		self.write({'msg':'login fail'})

# user logout
class LogoutHandler(AuthBaseHandler):
	def get (self, *args,**kwargs):
	    #self.session.set('user_info','') #将用户的cookie清除
	    self.session.delete('user_info')
	    self.redirect('/login')

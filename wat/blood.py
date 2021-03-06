import webapp2
import webapp2
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import blobstore
import cgi
from google.appengine.ext import db
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app
import jinja2
import os
import json
import time
from datetime import date


JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                extensions=['jinja2.ext.autoescape'],
                    autoescape=True)

class camp(db.Model):
             name=db.StringProperty()
             user=db.UserProperty()
             contact=db.PhoneNumberProperty()
	     heading=db.StringProperty()
             address=db.PostalAddressProperty()
             category=db.StringProperty(choices=set(["Harassment","Theft","GangRelated","Unsafe At Night","Physical Assault","Bribe"]))
             coordinates=db.GeoPtProperty()
             age=db.StringProperty()
	     description=db.TextProperty()
             sex=db.StringProperty(choices=set(['Male','Female']))
             image=db.BlobProperty()
	     date= db.StringProperty() 
class pol(db.Model):
             name=db.StringProperty()
             user=db.UserProperty()
             contact=db.PhoneNumberProperty()
             address=db.PostalAddressProperty()
             coordinates=db.GeoPtProperty()
             headbranch=db.StringProperty()
             manager=db.StringProperty()
class ngo(db.Model):
             name=db.StringProperty()
             user=db.UserProperty()
	     category=db.StringProperty(choices=set(["Harassment","Theft","GangRelated","Unsafe At Night","Physical Assault","Bribe"]))
             contact=db.PhoneNumberProperty()
             incharge=db.StringProperty()
	     url=db.LinkProperty()
class like(db.Model):
	     ide=db.StringProperty()
	     likeno=db.IntegerProperty()
	     dislikeno=db.IntegerProperty()
	     user=db.UserProperty()
class comment(db.Model):
	     ide=db.StringProperty()
	     com=db.TextProperty()
	     user=db.UserProperty()
class addrb(db.Model):
	     address=db.PostalAddressProperty()
	     coordinates=db.GeoPtProperty()
class petition(db.Model):
	     ide=db.StringProperty()
	     user=db.UserProperty()
	     name=db.StringProperty()
	     father=db.StringProperty()
	     sex=db.StringProperty(choices=set(['Male','Female']))
import datetime
class petit(webapp2.RequestHandler):
	def get(self,get_key):
		template_values={'get_key':get_key}
	    	template=JINJA_ENVIRONMENT.get_template('html/petit.html')
		self.response.write(template.render(template_values))
	def post(self):
		user=users.get_current_user()
		k=petition.all().filter("user =",user)
		if k.count()>0:
			l=k[0].key()
			obj=petition.get(k)
			obj.ide=get_key
			obj.user=user
			obj.name=name
			obj.put()
		else:
			k=petition()
			k.ide=get_key
			k.user=user
			k.name=self.request.get("name")
			k.sex=self.request.get("sex")
			k.father=self.request.get("father")
			k.put()
		self.redirect("/thank")

		
class thank(webapp2.RequestHandler):
    	def get(self,get_key):
		user=users.get_current_user()
		k=petition.all().filter("user =",user)
		if k.count()>0:
			l=k[0].key()
			obj=petition.get(k)
			obj.user=user
			obj.name=name
			obj.put()
		else:
			k=petition()
			k.ide=get_key
			k.user=user
			k.name=self.request.get("name")
			k.sex=self.request.get("sex")
			k.father=self.request.get("father")
			k.put()
		template_values={}
	    	template=JINJA_ENVIRONMENT.get_template('html/thank.html')
		self.response.write(template.render(template_values))
class complaint(webapp2.RequestHandler):
    	def get(self):
	    	template_values={}
		user=users.get_current_user()
		login=users.create_login_url("/")
		logout=users.create_logout_url("/")
		if user:
			flag=1
		else:
			flag=0
		template_values={'flag':flag,'login':login,'logout':logout}
	#	upload_url=blobstore.create_upload_url('/upload_photo')
	    	template=JINJA_ENVIRONMENT.get_template('html/complaint.html')
		self.response.write(template.render(template_values))
	def post(self):
		v=str(self.request.get("lat"))
		l=str(self.request.get("long"))
		s=v+", "+l
		if self.request.get("img"):
			image=self.request.get("img")
		k=camp()
		if self.request.get("img"):
			k.image=db.Blob(image)
		k.name=self.request.get("name")
		k.user=users.get_current_user()
		k.category=self.request.get("type")
		k.contact=self.request.get("phone")
		k.address=self.request.get("address")
		k.description=self.request.get("description")
		k.age=self.request.get("age")
		k.sex=self.request.get("sex")
		k.coordinates=s
		x=datetime.datetime.now()
		k.date=x.strftime('%m/%d/%y:%H-%M-%S')
		k.put()
		user=users.get_current_user()
		l=camp.all().filter("user =", user)
		self.redirect("/report/" + str(k.key()))
class imagehandler2(webapp2.RequestHandler):
	def get(self):
                account_key=self.request.get('key')
                account = db.get(account_key)
                if account.image:
                        self.response.headers['Content-Type'] = "image/jpg"
                        self.response.out.write(account.image)
                else:
                        self.error(404)
class police(webapp2.RequestHandler):
    	def get(self):
		user=users.get_current_user()
		k=pol.all().filter("user =",user)

		if k.count()==0:
	    		template_values={}
	#	upload_url=blobstore.create_upload_url('/upload_photo')
	    		template=JINJA_ENVIRONMENT.get_template('html/police.html')
			self.response.write(template.render(template_values))
		else:
			self.redirect('/home_police')
	def post(self):
		v=str(self.request.get("lat"))
		l=str(self.request.get("long"))
		s=v+", "+l
		k=pol()
		k.name=self.request.get("name")
		k.user=users.get_current_user()
		k.contact=self.request.get("phone")
		k.address=self.request.get("address")
		k.manager=self.request.get("manager")
		k.headbranch=self.request.get("head_branch")
		k.coordinates=s
		k.put()
		self.redirect('/home_police')
class ngo_form(webapp2.RequestHandler):
    	def get(self):
		user=users.get_current_user()
		k=ngo.all().filter("user =",user)
		if k.count()==0:
	    		template_values={}
	#	upload_url=blobstore.create_upload_url('/upload_photo')
	    		template=JINJA_ENVIRONMENT.get_template('html/ngo_form.html')
			self.response.write(template.render(template_values))
		else:
			self.redirect('/home_ngo')
	def post(self):
		k=ngo()
		k.name=self.request.get("name")
		k.user=users.get_current_user()
		k.contact=self.request.get("phone")
		k.url=self.request.get("url")
		k.category=self.request.get("type")
		k.incharge=self.request.get("manager")
		k.put()
		self.redirect('/home_ngo')

class report(webapp2.RequestHandler):
	def get(self,get_key):
		l=camp.all()
		a=[]
		for i in l:
			if str(i.key())==str(get_key):
				a.append(i)
				break
		g=[]
		f=comment.all()
		for j in f:
			if str(j.ide)==str(get_key):
				g.append(j)
		k=[]
		l=petition.all()
		for j in l:
			if str(j.ide)==str(get_key):
				k.append(j)
		fat=[]
		an=like.all()
		for t in an:
			if str(t.ide)==str(get_key):
				fat.append(t)
				
		le=len(k)	
		template_values={'a':a,'g':g,'key':str(i.key()),'k':le,'fat':fat}
	    	template=JINJA_ENVIRONMENT.get_template('html/report.html')	
		self.response.write(template.render(template_values))
	
class like1(webapp2.RequestHandler):
	def get(self,get_key):
		l=camp.all()
		user=users.get_current_user()
		if user:
			a=[]
			for i in l:
				if str(i.key())==str(get_key):
					a.append(i)
					break;
			m=like.all()
			flag=0
			for i in m:
				if i.ide==str(get_key):
					flag=1
					break;
			if flag==0:
				k=like()
				k.ide=str(get_key)
				k.likeno=1
				k.dislikeno=0
				k.user=users.get_current_user()
				k.put()
			else:
				k=i.key()
				obj=like.get(k)
				if obj.user!=user:
					obj.likeno+=1
					obj.user=user
					obj.put()
			self.redirect('/report/'+get_key)
		else:	
			self.redirect(users.create_login_url(self.request.uri))		
class dislike1(webapp2.RequestHandler):
	def get(self,get_key):
		l=camp.all()
		user=users.get_current_user()
		if user:
			a=[]
			for i in l:
				if str(i.key())==str(get_key):
					a.append(i)
					break;
			m=like.all()
			flag=0
			for i in m:
				if i.ide==str(get_key):
					flag=1
					break;
			if flag==0:
				k=like()
				k.ide=str(get_key)
				k.dislikeno=1
				k.likeno=0
				k.user=users.get_current_user()
				k.put()
			else:
				k=i.key()
				obj=like.get(k)
				if obj.user!=user:
					obj.dislikeno+=1
					obj.user=user
					obj.put()
			self.redirect('/report/'+get_key)
		else:
			self.redirect(users.create_login_url(self.request.uri))		
			

class comment1(webapp2.RequestHandler):
	def get(self,get_key):
		l=camp.all()
		user=users.get_current_user()
		if user:
			a=[]
			for i in l:
				if str(i.key())==str(get_key):
					a.append(i)
					break;
			m=comment.all()
			flag=0
			for i in m:
				if i.ide==str(get_key):
					flag=1
					break;
			if flag==0:
				k=comment()
				k.ide=str(get_key)
				k.com=self.request.get("com")
				k.user=users.get_current_user()
				k.put()
			else:
				k=i.key()
				self.response.write(self.request.get("com"))
				obj=comment.get(k)
				obj.com=self.request.get("com")
				obj.user=user
				obj.put()
			self.redirect("/report/"+str(get_key))

		else:	
			self.redirect(users.create_login_url(self.request.uri))	
class home_police(webapp2.RequestHandler):
	def get(self):
		user=users.get_current_user()
		k=pol.all().filter("user =",user)
		if k.count()>0:
	    		template_values={}
	    		template=JINJA_ENVIRONMENT.get_template('html/home_police.html')
			self.response.write(template.render(template_values))	
		else:	
			template_values={}
	    		template=JINJA_ENVIRONMENT.get_template('html/police.html')
			self.response.write(template.render(template_values))	
class home_ngo(webapp2.RequestHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			k=ngo.all().filter("user =",user)
			if k.count()!=0:
				d=camp.all().filter("category =",k[0].category)
				if d.count()>0:
					lat=[]
					lng=[]
					final=[]
					add=[]
					name=[]
					lis=[]
					m=camp.all()
					for i in m:
						s=str(i.coordinates)
						l=s.split(",")
						lis.append(i.address)
						lis.append(i.contact)
						lis=[]
						lat.append(float(l[0]))
	                        		lat.append(float(l[1]))
						lat.append(i.name)
						lat.append(i.category)
						lat.append(i.address)
						lat.append(str(i.key()))
						final.append(lat)
						lat=[]
						add.append(i.address)
						name.append(add)
					template_values={'m':m,'k':k,'final':json.dumps(final)}
		 		   	template=JINJA_ENVIRONMENT.get_template('html/home_ngo.html')
					self.response.write(template.render(template_values))
				else:

					template_values={}
		 			template=JINJA_ENVIRONMENT.get_template('html/no_complaint.html')
					self.response.write(template.render(template_values))
			else:
				self.redirect("/ngo_form")
		else:
			self.redirect(users.create_login_url(self.request.uri))
class contact(webapp2.RequestHandler):
	def get(self):
	    	template_values={}
	    	template=JINJA_ENVIRONMENT.get_template('html/contact.html')
		self.response.write(template.render(template_values))
class about(webapp2.RequestHandler):
	def get(self):
	    	template_values={}
	    	template=JINJA_ENVIRONMENT.get_template('html/about.html')
		self.response.write(template.render(template_values))
class home_visitor(webapp2.RequestHandler):
	def get(self):
	    	template_values={}
	    	template=JINJA_ENVIRONMENT.get_template('html/home_visitor.html')
		self.response.write(template.render(template_values))	
class locality(webapp2.RequestHandler):
	def get(self):
		user=users.get_current_user()
		if user:
			k=pol.all().filter("user =", user)
			r=str(k[0].coordinates)
			r=r.split(",")
			lat=[]
			lng=[]
			final=[]
			add=[]
			name=[]
			lis=[]
			m=camp.all()
			for i in m:
				s=str(i.coordinates)
				l=s.split(",")
				lis.append(i.address)
				lis.append(i.contact)
				lis=[]
				lat.append(float(l[0]))
	                        lat.append(float(l[1]))
				lat.append(i.name)
				lat.append(i.category)
				lat.append(i.address)
				lat.append(str(i.key()))
				final.append(lat)
				lat=[]
				add.append(i.address)
				name.append(add)
			template_values={'k':k,'final':json.dumps(final),'locate':k[0].address,'long':float(r[1]),'latit':float(r[0])}
		    	template=JINJA_ENVIRONMENT.get_template('html/locality.html')
			self.response.write(template.render(template_values))
		else:
			self.redirect('/home_police')
class category(webapp2.RequestHandler):
	def get(self):
		user=users.get_current_user()
		k=pol.all().filter("user =", user)
		if k.count()>0:
			r=str(k[0].coordinates)
			r=r.split(",")
			lat=[]
			lng=[]
			final=[]
			add=[]
			name=[]
			lis=[]
			t=self.request.get("type")
			m=camp.all().filter("category =",t)
			if m.count()>0:
				for i in m:
					s=str(i.coordinates)
					l=s.split(",")
					lis.append(i.address)
					lis.append(i.contact)
					lis=[]
					lat.append(float(l[0]))
        	        	        lat.append(float(l[1]))
					lat.append(i.name)
					lat.append(i.category)
					lat.append(i.address)
					lat.append(str(i.key()))
					final.append(lat)
					lat=[]
					add.append(i.address)
					name.append(add)
				template_values={'m':m,'k':k,'final':json.dumps(final),'locate':k[0].address,'long':float(r[1]),'latit':float(r[0])}
		    		template=JINJA_ENVIRONMENT.get_template('html/category.html')
				self.response.write(template.render(template_values))	
			else:
				template_values={}
		    		template=JINJA_ENVIRONMENT.get_template('html/no_complaint.html')
				self.response.write(template.render(template_values))	
		else:
			template_values={}
		    	template=JINJA_ENVIRONMENT.get_template('html/police.html')
			self.response.write(template.render(template_values))		
class locality_visitor(webapp2.RequestHandler):
	def get(self):
	    	template_values={}
	    	template=JINJA_ENVIRONMENT.get_template('html/locality_visitor.html')
		self.response.write(template.render(template_values))	
	def post(self):
		v=str(self.request.get("lat"))
		l=str(self.request.get("long"))
		s=v+", "+l
		k=addrb()
		k.address=self.request.get("address")
		k.coordinates=s
		k.put()
		self.redirect('/loc/'+str(k.key()))

class loc(webapp2.RequestHandler):
	def get(self,get_key):
		l=addrb.all()
		a=[]
		for j in l:
			if str(j.key())==str(get_key):
				a.append(j)
				break
		r=str(j.coordinates)
		r=r.split(",")		
		lat=[]
		lng=[]
		final=[]
		add=[]
		name=[]
		lis=[]
		m=camp.all()
		for i in m:
			s=str(i.coordinates)
			l=s.split(",")
			lis.append(i.address)
			lis.append(i.contact)
			lis=[]
			lat.append(float(l[0]))
	                lat.append(float(l[1]))
			lat.append(i.name)
			lat.append(i.category)
			lat.append(i.address)
			lat.append(str(i.key()))
			final.append(lat)
			lat=[]
			add.append(i.address)
			name.append(add)
		template_values={'final':json.dumps(final),'long':float(r[1]),'latit':float(r[0]),'m':m}
	    	template=JINJA_ENVIRONMENT.get_template('html/loc.html')
		self.response.write(template.render(template_values))

class category_visitor(webapp2.RequestHandler):
	def get(self):
		lat=[]
		lng=[]
		final=[]
		add=[]
		name=[]
		lis=[]
		t=self.request.get("type")
		m=camp.all().filter("category =",t)
		if m.count()>0:
			for i in m:
				s=str(i.coordinates)
				l=s.split(",")
				lis.append(i.address)
				lis.append(i.contact)
				lis=[]
				lat.append(float(l[0]))
        	                lat.append(float(l[1]))
				lat.append(i.name)
				lat.append(i.category)
				lat.append(i.address)
				lat.append(str(i.key()))
				final.append(lat)
				lat=[]
				add.append(i.address)
				name.append(add)
			template_values={'final':json.dumps(final),'m':m}
		    	template=JINJA_ENVIRONMENT.get_template('html/category_visitor.html')
			self.response.write(template.render(template_values))	
		else:
			template_values={}
		    	template=JINJA_ENVIRONMENT.get_template('html/no_complaint.html')
			self.response.write(template.render(template_values))			
class main(webapp2.RequestHandler):
	def get(self):
		user=users.get_current_user()
		login=users.create_login_url("/")
		logout=users.create_logout_url("/")
		if user:
			flag=1
		else:
			flag=0
		template_values={'logout':logout,'flag':flag,'login':login}
	    	template=JINJA_ENVIRONMENT.get_template('html/main.html')
		self.response.write(template.render(template_values))	
application=webapp2.WSGIApplication([
			("/",main),
	                ("/complaint",complaint),
			("/report/(\S+)",report),
			("/imagehandler2",imagehandler2),
			("/like1/(\S+)",like1),
			("/dislike1/(\S+)",dislike1),
			("/comment1/(\S+)",comment1),
			("/home_police",home_police),
			("/locality",locality),
			("/ngo_form",ngo_form),
			("/home_ngo",home_ngo),
			("/loc/(\S+)",loc),
			("/home_visitor",home_visitor),
			("/category",category),
			("/contact",contact),
			("/about",about),
			("/thank/(\S+)",thank),
			("/petit/(\S+)",petit),
			("/category_visitor",category_visitor),
			("/locality_visitor",locality_visitor),
			("/police",police)
],debug=True)


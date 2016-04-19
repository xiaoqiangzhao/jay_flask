#! /home/b51816/localpython/python3/bin/python3
import sys
from flask import Flask , redirect
from flask import request,render_template,url_for
from werkzeug import secure_filename

app = Flask(__name__)
@app.route('/',methods=['get','post'])
def home():
   return render_template('home.html')

@app.route('/projects/',methods=["get"])
def projects():
   searchword = request.args.get('proj','')
   return '<h1 color="red">jay projects %s</h1>'%searchword

@app.route('/about',methods=["get"])
def about():
   return "<h1 color='red'>jay about</h1>"

@app.route('/hello/<name>/<greet>',methods=["get"])
def hello(name,greet):
   return '<html> <body> <h1>%s %s</h1> </body> </html>' %(greet,name)
def about():
   return "<h1 color='red'>jay about</h1>"

@app.route('/upload',methods=["get","post"])
def upload():
   print(request.method)
   if request.method == "GET":
      return render_template('upload.html')
   else:
      authorized=False
      if request.form['code'] == "b51816":
         authorized=True
         print("processing uploading")
         for key in request.files:
            print(key)
            f = request.files[key]
            f.save('/home/b51816/python_study/files/'+secure_filename(f.filename))
      return render_template('upload_done.html',permission=authorized)


@app.route('/signin',methods=['get'])
def signin_form():
   return render_template('form.html')
   # return '''<form action="/signin" method="post">
            # <p>username<input name="username"></p>
            # <p>password<input name="password" type="password"</p> 
            # <p><button type="submit">Sign In</button></p> 
            # </form>'''

@app.route('/site0',methods=['get'])
def site0():
   return redirect(url_for('jay_home'))


@app.route('/site1',methods=['get'])
def site1():
   return redirect(url_for('jay_home'))

@app.route('/jay_home',methods=['get'])
def jay_home():
   return render_template('jay_home.html')

@app.route('/signin',methods=['post'])
def signin():
   if request.form['username'] =='jay' and request.form['password']=='b51816':
      return redirect(url_for("jay_home"))
   return render_template('form.html',message='Shit, Go Away!',username=request.form['username'])
# with app.test_request_context():
   # print (url_for('hello',name="why",greet="love"))
if __name__=='__main__':
   app.run(host='0.0.0.0')

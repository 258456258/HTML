#application.py
from flask import Flask,render_tempalte,request
app=Flask(__name__)
@app.route('/')
def index():
	return render_tempalte('index.html')
@app.route('/hello',methods=['POST','GET'])
def hello():
	if request.method=='GET': #If user access direct hello then this will work and show this message
		return 'Please submit the form instead.'
	else:
		name=request.form.get('name')
		return render_tempalte('hello.html',name=name)

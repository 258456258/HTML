from flask import Flask,render_tempalte,request,session
from flask_session import Session

app=Flask(__name__)

app.config['SESSION_PERMANENT']=False
app.config['SESSION_TYPE']='filesystem'
Session(app)

@app.route('/',method=['GET','POST'])
def index():
	if session.get('notes') is None:
		session['notes']=[]
	if request.method=='POST':
		note=request.form.get('note')
		session['notes'].append(note)
	
	return render_tempalte('index.html',notes=session['notes'])

from django.http import HttpResponse
from django.shortcuts import render

'''
def index(request):

    return HttpResponse('''
    #<p>This is my first web page in Django</p><h1>1st URL.........</h1><a href="https://github.com/princetyagi258456"> My Github Profile</a>
#    	<h1> 2nd URL....</h1><a href="https://www.linkedin.com/in/prince-tyagi-962b191a4/">My Linked Profile</a>
def index(request):
	
	return render(request,'index.html')
	#return HttpResponse('''Home<p>This is my first web page in Django</p><br><a href="http://127.0.0.1:8000/removepunc">link to go removepunc</a><br><a href="http://127.0.0.1:8000/capitalizefirst">link to go capitalizefirst</a><br><a href="http://127.0.0.1:8000/newlineremove">link to go newlineremove</a><br><a href="http://127.0.0.1:8000/spaceremove">link to go spaceremovee</a><br><a href="http://127.0.0.1:8000/charcount">link to go charcount</a>''')

def analyze(request):
	#get the text
	djtext=request.GET.get('text','default')
	#CHECK CHECKBOX VALUES
	removepunc=request.GET.get('removepunc','off')
	fullcaps=request.GET.get('fullcaps','off')
	newlineremover=request.GET.get('newlineremover','off')
	extraspaceremover=request.GET.get('extraspaceremover','off')
	charcount=request.GET.get('charcount','off')

	#CHECK WHICH CHECKBOX IS ON
	if removepunc =="on":
	#analyzed=djtext
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed= ""
		for char in djtext:
			if char not in punctuations:
				analyzed=analyzed+char.upper()
		params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
	#Analyze the text
		return render(request,'analyze.html',params)

	elif(fullcaps=="on"):
		analyzed=""
		for char in djtext:
			analyzed=analyzed+char.upper()
		params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
		return render(request,'analyze.html',params)

	elif(newlineremover=="on"):
		analyzed=""
		for char in djtext:
			if (char!="\n"):
				analyzed=analyzed+char
		params={'purpose':'Removed New Lines','analyzed_text':analyzed}
		return render(request,'analyze.html',params)


	elif(extraspaceremover=="on"):
		analyzed=""
		for index, char  in enumerate(djtext):
			if not((djtext[index]==" ") and djtext[index+1]==" "):
				analyzed=analyzed+char
		params={'purpose':'Removed New Lines','analyzed_text':analyzed}
		return render(request,'analyze.html',params)

	elif(charcount=="on"):
		analyzed=""
		for char in djtext:
			analyzed=len(djtext)		

		params={'purpose':'Removed New Lines','analyzed_text':analyzed}
		return render(request,'analyze.html',params)


	else:
		return HttpResponse('Error')

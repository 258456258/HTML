	elif(extraspaceremover=="on"):
		analyzed=""
		for index, char  in enumerate(djtext):
			if not((djtext[index]==" ") and djtext[index+1]==" "):
				analyzed=analyzed+char
		params={'purpose':'Removed New Lines','analyzed_text':analyzed}
		return render(request,'analyze.html',params)

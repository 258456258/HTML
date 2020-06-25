
	elif(newlineremover=="on"):
		analyzed=""
		for char in djtext:
			if (char!="\n"):
				analyzed=analyzed+char
		params={'purpose':'Removed New Lines','analyzed_text':analyzed}
		return render(request,'analyze.html',params)

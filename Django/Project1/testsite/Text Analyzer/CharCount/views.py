	elif(charcount=="on"):
		analyzed=""
		for char in djtext:
			analyzed=len(djtext)		

		params={'purpose':'Removed New Lines','analyzed_text':analyzed}
		return render(request,'analyze.html',params)


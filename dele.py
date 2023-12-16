def pos(s):
	a=open("criminal.txt")
	lines = a.readlines()
	a.close()
	p=-1
	q=0
	for i in lines:
		q=q+1
		p=i.find(s)
		if p!=-1:
			flag=i
			break
	if p!=-1:
		del lines[q-1]
		b=open("criminal.txt","w+")
		for line in lines:
			b.write(line)
		b.close()


		
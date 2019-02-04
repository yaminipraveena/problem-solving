leap=int(input())
if leap%4==0 :
	if leap%100==0:
		if leap%400==0:
			print("leap")
		print("not")
	print("leap")
else :
	print("not")

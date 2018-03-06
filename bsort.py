list=[3,1,7,5,2,6,4]
def bubblesort():
	for i in range(len(list)):
		for j in range(len(list)):
			if list[i]<list[j]:
				t=0
				t=list[i]
				list[i]=list[j]
				list[j]=t  
	#print (list)
print(list)
bubblesort()

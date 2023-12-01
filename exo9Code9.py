antreUser=input("antre yon chenn karakte m ap ba w tout endis let 'a' ki ladan l nan yon lis : ")
n=len(antreUser)
lis=[]

for j in range(0,n):
	if antreUser[j]=="a":
		lis.append(j)

print( F"total endis karakte 'a' ki nan chenn sa se: {lis}")

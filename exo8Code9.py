antreUser=input("antre yon chenn karakte m ap ba w total endis let 'a' ki ladan l : ")
n=len(antreUser)
som=0
for j in range(0,n):
	if antreUser[j]=="a":
		som+=j
print( F"total endis karakte 'a' ki nan chenn sa se: {som}")

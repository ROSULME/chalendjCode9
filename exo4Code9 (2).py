antreUser = input("antre yon chenn karakte :")
nouvoChenn = ""
antreUser=antreUser.split()

for j in antreUser:
    nouvoChenn+= j[0]

print(nouvoChenn)
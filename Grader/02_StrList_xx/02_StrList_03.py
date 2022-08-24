month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dmy = input().split("/")

print(month[int(dmy[1])-1], dmy[0]+",", dmy[2])
#BT3051 Assignment 0b
#Roll number: BE17B037
#Collaborators: none
#Time: 0:10

print("Enter a number:")
n = int(input("> "))
for i in range(1,n+1,1):
	for j in range(1,i+1,1):
		print(j**i, end = " ")
	print()

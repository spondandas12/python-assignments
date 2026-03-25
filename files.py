#create file
f=open("shivanee.txt","w")
#f.write("hello shivanee\n")
#print("file created successfully!!")
f.close()

#read file
f=open("shivanee.txt")
#print(f.read())
f.close()

#append
f=open("shivanee.txt","a")
f.write("how are you?")
#print("content appended successfully!!")
f=open("shivanee.txt")
#print(f.read())
f.close()

f=open("shivanee.txt","r")
#print(f.read())


f=open("shivanee.txt","w")
f.write("mit adt university")
f=open("shivanee.txt","r")
print(f.read())
f.close()


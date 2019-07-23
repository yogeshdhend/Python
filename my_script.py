import io

print("Hello World from docker container")
file1 = open("myfile.txt","r+")  
  
print ("Output of Read function is ")
print (file1.read()) 

file1.close()

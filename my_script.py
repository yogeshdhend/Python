import datetime

print("wrting to text file from docker container")
	   
file = open("myfile.txt","a")
file.write('file updated at %s.\n' %(datetime.datetime.now()))
file.close()			   

file1 = open("myfile.txt","r+")  
  
print ("Output of Read function is ")
print (file1.read()) 

file1.close()

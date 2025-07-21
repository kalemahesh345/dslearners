import  csv


# with open("data.csv","w",newline="") as f :
#     writer=csv.writer(f)
#     writer.writerows(["name","age"])


# with open("data.csv","r",newline="")as f:
#     data = f.read()  
 

#   print(f.read())
   
# if data == " ":
#   print("file is empty")
# else:
#   print("file is not empty")

# if "name"  in data: 
  
#   print("this word in file")
# else:
   
#    print("no")



# # Write data to the CSV file
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"]) 

# Read and check for a specific word
with open("data.csv", "r", newline="") as f:
    data = f.read()

if "name" in data:
    print("This word is in the file")
else:
    print("No")

  
from sys import argv 

script, file_name = argv 

print("We are going to erase {file_name}.")
print("If you don't want to do that, then press CTRL + C (^C)")
print("If you want to do that, then hit RETURN")
input("? ")

print("Opening the file....")
f = open(file_name, 'w')

print("Truncating the file. Goodbye!")
f.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
f.write(f"{line1}\n{line2}\n{line3}")

print("And finally let's close it")
f.close()
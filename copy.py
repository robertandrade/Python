# Import 'argv' which will allow us to enter 
# arguements in the command line upon calling command
from sys import argv

# Import the 'exists' method to determine if file exists
from os.path import exists

# argv will take two arguements including the name 
# of the file at script call
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one file, how?
in_file = open(from_file).read()
# indata = in_file.read()

print("Hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()
# in_file.close()
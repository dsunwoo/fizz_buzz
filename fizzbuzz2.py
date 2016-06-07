import sys
# Check for user input variable in command line
if len(sys.argv)>1:
    if len(sys.argv)>2:
        print("More than 1 argument listed, only taking 1st argument.")
    clim=sys.argv[1]
else: 
# No input from command line. Ask user to input limit.
    clim=input("Enter number to count to (no spaces): ")
    print(clim)
# Check to see if limit is a number
try:
    int(clim)/1
except TypeError:
    print("Please enter an integer value")
    clim=input("Enter number to count to (no spaces): ")

# Start Main
print("Fizz counting up to {}".format(clim))

#Fizz Buzz Logic below
for n in range (1,int(clim)+1):
    shout=n
    if n % 3 == 0:
        shout="Fizz"
    if n % 5 == 0:
        if shout == "Fizz":
            shout+=" Buzz"
        else:
            shout="Buzz"
    print(shout)
    
import sys
clim=100 # Set upper limit for counting

print("Fizz counting up to {0}".format(clim))

for n in range (1,clim):
    shout=n
    if n % 3 == 0:
        shout="Fizz"
    if n % 5 == 0:
        if shout == "Fizz":
            shout+=" Buzz"
        else:
            shout="Buzz"
    print(shout)
    
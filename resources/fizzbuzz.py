limit = int(input("Type the number: "))

#for i in range(1, limit+1):
#    if i % 15 == 0:
#        print("fizzbuzz")
#    else: 
#        if i % 3 == 0:
#            print("fizz")
#        else:
#            if i % 5 == 0:
#                print("buzz")
#            else:
#                print(i)

#print(["fizzbuzz" if i%15==0 else "fizz" if i%3==0 else "buzz" if i%5==0 else i for i in range(1,limit+1)])

for i in range (1, limit+1):
    print("fizz"*(not i%3) + "buzz"*(not i%5) or i)

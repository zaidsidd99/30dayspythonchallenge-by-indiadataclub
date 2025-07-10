# num= input("enter a number :")
# num= int(num)

# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")





# indian= ["samosa", "dal", "paneer","chola_bhatura"]
# chinese= ["momos", "fried_rice" , "spring_roll"]
# italian= ["pasta", "pizza", "french_fries"]

# dish= input("enter a dish name :")

# if dish in indian:
#     print("its an indian cuisin.")

# elif dish in chinese:
#     print("its an chinese cuisine.")

# elif dish in italian:
#     print("its an italian cuisine.")

# else:
#     (" i dont know which country  cuisine dish is this . ")





# exp= [1200,3000,4000,9000,5900,4500]

# total= 0
# for item in exp:
#     total=total +item
# print(total)




# exp= [1200,3000,4000,9000,5900,4500]

# total = 0

# for i in range (len(exp)):
#     print('month:',(i+1),'expense:',exp[i])
#     total = total + exp[i]

# print('total expense is :',total)




# for i in range (1,6):
#     if i%2==0:
#       continue
#     print(i*i)





# Check if a user-entered number is prime ?

num = int(input("enter a number:"))

if num <= 1:
    print("not a prime number")
else:
    for i in range (2, num):
        if num%i == 0:
            print("not a prime number")
            break
    else:
        print ("prime number")
           
 


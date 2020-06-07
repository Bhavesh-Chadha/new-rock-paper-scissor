name = input("Enter your name: ")
print("Hello, ",name)
a = input().strip(',')
z  =len(a)
file =open("rating.txt")
fl = 1
for line in file:
    if name in line:
        y = line.split(' ')
        score = y[1]
        fl = 0
        break
if fl == 1:
    score = 0
print("Okay, let's start")
import random
if a == "":
  a  = ['rock','scissors', 'paper']
  while( 1):
    k = 0
    n = input()
    if n == '!exit':
        print("Bye!")
        exit()
    
    if n == '!rating':
        print("Your rating:",score)
        break
    b = random.choice(a)

    for i in range(3):
        if n == a[i]:
            k =3
            break
    if k == 0:
                print("Invalid input")
                
                continue
            
    if b == a[i]:
        print(f"There is a draw ({b})")
   
        score += 50
        continue
    elif b == a[i -1]:
        print(f"Sorry, but computer chose {b}")
        continue

    else :
        print(f"Well done. Computer chose {b} and failed")  
        score += 100
        continue          



else:
 while(True):
    n = input()
    k = 0
    if n == '!exit':
        print("Bye!")
        exit()
    
    if n == '!rating':
        print("Your rating:",score)
        continue
    b = random.choice(a)

    for i in range(z):
        if n == a[i]:
            k =3
            break
    if k == 0:
                print("Invalid input")
                
                continue
    o = a.index(n)
    diff = z - o - 1

    lis1 = a[o +1:o + z//2 +1:]
    if diff >=0:
     lis2= a[:z // 2 - diff: ] 
    else:
     lis2 = []
    lis1.extend(lis2)  
    #print(lis1)      
    if b == n:
        print(f"There is a draw ({b})")
        
        score += 50
        continue
     #print("=",b)   
    elif b  in lis1:    
        print(f"Sorry, but computer chose {b}")
        continue

    else :
        print(f"Well done. Computer chose {b} and failed")  
        score += 100
        continue          

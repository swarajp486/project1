import random
l=["s","w","g"]
u=0
c=0

print("You hove 10 chance to win")
print("Game start")

i=1
while(i!=10):
    print("Enter s(snake) w(water) g(gun)")
    n=input("Enter s(snake)\n w(water)\n g(gun)\n")
    choice=random.choice(l)
    if(n==choice):
        print(" Game is Draw ")
    elif(n=='s' and choice=='g'):
        print("You loose")
        c+=1
    elif(n=='w' and choice=='s'):
        print("You loose")
        c+=1
    elif(n=='g' and choice=='w'):
        print("You loose")
        c+=1
    else:
        print("You win")
        u+=1
    print("You have %d chance left"%(10-i))
    i+=1
if(c>u):
     print("I am win")
     print("computer point is %d and your point is %d"%(c,u))
elif(u>c):
      print("you  win")
      print("your point is %d and computer point is %d"%(u,c))
else:
     print(" the Game is Draw")
    
    



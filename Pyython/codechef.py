T=int(input())
for i in range(T):
     x , y, z = map(int , input().split())

    if(z%x==0 and y%x==0):
        print("any")
        
    elif(z%x==0 and z%y!=0):
        print("Chicken")
    
    elif(z%y==0 and z%x!=0):
        print("Duck")
        
    else:
        ("None")
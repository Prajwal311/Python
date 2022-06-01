# if __name__ == '__main__':
#     N = int(input())\
        
list1=[]

def insert_list(i,e):
    e=int(input())
    i=int(input())
    list1.insert(i,e)
    return list1
    print(list1)
    
def print1(list1):
    print(list1)
    
def remove_list(e):
    list1.remove(e)
    return list1
    print(list1)
def append_list(e):
    list1.append(e)
    return list1
    print(list1)

def sort_list(list1):
    list1.sort()
    return list1
    print(list1)

def pop_list(list1):
    list1.pop()
    return list1
    print(list1)

def reverse_list(list1):
    list1.reverse()
    return list1
    



insert_list(0,5)
insert_list(1,10)
insert_list(0,6)
print1(list1)
remove_list(6)
append_list(9)
append_list(1)
sort_list(list1)
print1(list1)
pop_list(list1)
reverse_list(list1)
print1(list1)


#WAP to check if a list contain a palindrome of element.(Hint : use copy() method)
#[1,2,3,2,1] [1,"abc","abc",1]

list = [1,2,3,2,1]

copylist = list.copy()
copylist.reverse()

if(list == copylist):
    print("Palindrome")
else:
    print("Not palindrome")
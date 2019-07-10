import  re
def int_float(x):
    x=eval(x)
    if type(x)==int :
        print("Integer")
        if x%2==0:
            print("Even")
        else:
            print("Odd")
    if type(x)== float :
        print("Float")

def typestr(x):
    if x.isalpha():
        if  x.isupper():
            print("Uppercase")
        elif x.islower()  :
            print("Lowercase")
        else:
            print("Both ")

    elif x.isalnum():
        print("Alphanumeric")

    elif re.match("(\d*\D*)+\!*\@*\#*\$*\\**\&*(\d*\D*)+",x) :
        print("Special Characters")





a= input('Enter the input')
if re.match("^\d*\.?\d*$",a) :
    print("Number")
    int_float(a)
else:
    print("String")
    typestr(a)

u=0
l=0
d=0
sc=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isnumeric():
        d+=1
    else:
        sc+=1
print("The number of uppercase letters",u)
print("The number of lowercase letters",l)
print("The number of digits",d)
print("The number of special characters letters",sc)





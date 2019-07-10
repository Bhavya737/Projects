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
            print("Both upper and lower case")

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





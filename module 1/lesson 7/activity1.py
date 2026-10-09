x = 5
#Identity Operator -> is or is not
if type(x) is int:
    print("True")
else:
    print("False")
y = 5.5
if type(y) is not float:
    print("True")
else:
    print("False")
sidratul = "math book"
miftahul = "math book"
if (sidratul is miftahul):
    print("Both have the SAME identity")
else:
    print("Both have DIFFERENT identity")

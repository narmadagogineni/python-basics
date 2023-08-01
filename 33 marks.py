sub1 = int(input("enter marks of s1 "))
sub2 = int(input("enter marks of s2 "))
sub3 = int(input("enter marks of s3 "))

if (sub1<33 or sub2<33 or sub3<33):
    print("fail because you have lesss marks in one of these sub")

elif ((sub1 + sub2 + sub3)/3 <40):
    print("fail due to least total marks")    
else:
    print("congrats, you passed!")    
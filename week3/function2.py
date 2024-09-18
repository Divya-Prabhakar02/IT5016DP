def function2(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    short_length = min(str1,str2)
    return short_length
def main():
    str1 = str(input("enter the string 1:"))
    str2 = str(input("enter the string 2:"))
    print("the shortest str is:", function2(str1,str2))
main()

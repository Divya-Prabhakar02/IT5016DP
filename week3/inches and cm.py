def inches_to_cm(inch,cm):
    inch = cm/2.54
    return 
def cm_to_inches(inch,cm):
    cm = inch*2.54
    return
def display():
    inch = float(input("enter the inches:"))
    cm = float(input("enter the centimeters:"))
    print(inches_to_cm(inch,cm))
    print(cm_to_inches(inch,cm))
display()



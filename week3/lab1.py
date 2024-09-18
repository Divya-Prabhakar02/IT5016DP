def earthquake():
    range = float(input("Enter the range of earthquake:"))
    if range <= 2.0:
        print("The earthquake is micro.")
    elif 2.0 <= range <=  3.0:
        print("The earthquake is very Minor")
    elif 3.0 <= range <= 4.0:
        print("The earthquake is minor.") 
    elif 4.0 <= range <= 5.0:
        print(" The earthquake is light.")   
    elif 5.0 <= range <= 6.0:
        print("The earthquake is Moderate.")    
    elif 6.0<= range <= 7.0:
        print("The earthquake is Strong.")     
    elif 7.0 <= range <= 8.0:
        print("The earthquake is Major.")  
    elif 8.0 <= range <= 10.0:
        print("The earthquake is great.")     
    else:
        print("The earthquake is Meteroic.")
earthquake()  


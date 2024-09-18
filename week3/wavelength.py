def wavelength():
    nm = int(input("enter the range:"))
    print("welcome to  wavelength to colour converter ")
    print (f"Thank you, The wavelength that you entered in nanaometer is {nm} ")

    if 620 <= nm <= 750:
        print("The colour of the wavelength is Red")
    elif 590 <= nm <= 620:
        print("The colour of the wavelength is Orange")    
    elif 570 <= nm  <= 590:
        print("The colour of the wavelength is Yellow")    
    elif 495 <= nm <= 570:
        print("The colour of the wavength is Green ")
    elif 450 <= nm <= 495:
        print("The colour of the wavenegth is Blue")
    elif 380 <= nm <= 450:
        print("The colour of the wavength is Violet")
    else: 
        print("ERROR!!!")  
wavelength()  

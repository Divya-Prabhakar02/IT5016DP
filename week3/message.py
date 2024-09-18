def display_welcome(name):
    message = "welcome**"+ name + "**"
    print(message)
    return
def display_cost(dollar, cent):
    cost_str = "cost is $" + str(dollar)+ ":"+ str(cent) 
    print(cost_str)
    return
display_welcome("divya")
print()
display_cost(15,35)   

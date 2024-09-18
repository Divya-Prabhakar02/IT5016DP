cover_price = 24.95
discount = 40/100
copies = 60 
price_after_discount = cover_price-(cover_price* discount)
shipping_cost = 3+(60-1)*75/100
total = price_after_discount*copies+shipping_cost
print(total)
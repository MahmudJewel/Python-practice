#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound=.76
new_price={item:value*dollar_to_pound for (item,value) in old_price.items()}
print(new_price)
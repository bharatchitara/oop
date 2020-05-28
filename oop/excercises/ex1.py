
def purchase_mobile(price,brand):
    if(brand=='Apple'):
    
        total_price = price*(0.90)
    else:
        total_price = price*(0.95)
    return total_price

    
def purchase_shoe(price,material):
    if(material =="leather"):
        total_price = price *(1.05)
    else:
        total_price = price *(1.02)
    return total_price

print(purchase_mobile(20000,"Apple"))
print(purchase_shoe(200,"leather"))


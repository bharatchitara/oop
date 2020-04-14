'''
#objects -  Customer, employee, item

#customer -- attributes: customer_name, bill_amount
             fucntions: pays_bill, purchases

employee-- attributes:employee_name,designation
            fucntion:

item-- attributes: item_id , price_per_unit
'''

class Customer:
    def __init__(self):
        self.customer_name="bharat"
        self.bill_amount=0
    
    def pays_bill(self, amount):
        print(self.customer_name+" pays bill amount of Rs. "+ str(amount))
        
    def purchases(self):
        self.bill_amount=200
        pay_bill=self.bill_amount*(95/100)
        self.pays_bill(pay_bill)

c1=Customer()
c1.purchases()
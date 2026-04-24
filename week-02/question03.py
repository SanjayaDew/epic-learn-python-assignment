price = 200
quantity = 4

total = price * quantity
print("Total amount : ",total)

if(total>700):
    discount = total * 0.10
    final_amount = total - discount
    print("Discount : ",discount)
    print("Final amount : ",final_amount)
else:
    print("Final amount : ",total)
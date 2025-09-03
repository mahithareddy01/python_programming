consumer_number=int(input("Enter consumer number: "))
consumer_name=input("Enter consumer name: ")
present_month_reading=int(input("Enter Present month reading of consumer:"))
last_month_reading=int(input("Enter Last1 month reading of consumer:"))
#calculating total units and current bill
total_units=present_month_reading-last_month_reading
cost_per_unit=3.80
curent_bill=total_units*cost_per_unit
print("---CUSTOMER DETAILS-----")
print("consumer number:",consumer_number)
print("consumer name: ",consumer_name)
print("Present month reading of consumer: ",present_month_reading)
print("Last month reading of consumer: ",last_month_reading)
print("Current bill is : ",curent_bill)
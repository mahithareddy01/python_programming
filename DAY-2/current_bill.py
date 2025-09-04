consumer_number=int(input("Enter consumer number: "))
consumer_name=input("Enter consumer name: ")
present_month_reading=int(input("Enter Present month reading of consumer:"))
last_month_reading=int(input("Enter Last1 month reading of consumer:"))
#calculating total units and current bill
total_units=present_month_reading-last_month_reading
#cost_per_unit=3.80 for 1-50 units
#4.20 for 51-100 units
#5.10 for 100-200 units
#6.30 for 200-300 units
#7.50 for above 300 units
#(total_units*3.80)+((total_units-50)*4.20)
if(total_units>0):
    units = min(total_units, 50)
    cost=(total_units*3.80)
    total_units-=units
if(total_units>0):
    units = min(total_units, 50)
    cost+=(total_units*4.20)
    total_units-=units
if(total_units>0):
    units = min(total_units, 100)
    cost+=(total_units*5.10)
    total_units-=units
if(total_units>0):
    units = min(total_units, 100)
    cost+=(total_units*6.30)
    total_units-=units
if(total_units>0):
    cost+=total_units*7.50


print("---CUSTOMER DETAILS-----")
print("consumer number:",consumer_number)
print("consumer name: ",consumer_name)
print("Present month reading of consumer: ",present_month_reading)
print("Last month reading of consumer: ",last_month_reading)
print("Current bill is : ",cost)
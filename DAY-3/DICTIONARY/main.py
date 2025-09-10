import ecommerce_utils
cart={"Laptop": 55000,"Phone":30000,"Headphones": 2000}
price=0
for val in cart.values():
    price+=val
ecommerce_utils.generate_invoice(cart)
new_price=ecommerce_utils.apply_discount(price,10)
print(f"After 10% discount: rs.{new_price}")
new=ecommerce_utils.add_gst(price,18)
print(f"After 18% GST: rs.{new}")
print("Thank you for shopping with us!")
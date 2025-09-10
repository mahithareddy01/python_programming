def apply_discount(price,disc_percent):
    disc_price=price-(disc_percent*price)/100
    return disc_price
def add_gst(price,gst_percent=18):
    new_price=price+((gst_percent*18)/100)
    return new_price
def generate_invoice(cart,discount_percent=0,gst_percent=18):
    print("-------Invoice------")
    for key in cart.keys():
        print(key," : ",cart.get(key))
    print("---------------------")
    tot=0
    for val in cart.values():
        tot+=val
    print("Subtotal: ",tot)


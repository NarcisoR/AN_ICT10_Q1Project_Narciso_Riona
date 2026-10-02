from pyscript import document


def generate(event):
    
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock = document.getElementById("stock").value

    if not product_name or not stock:
        document.getElementById("sku-output").innerHTML = "Not available. Please fill form completely"
        return

    category_code = category[0:3].upper()          
    product_code = product_name[0:3].upper()      
    stock_code = str(stock)              
    sku = category_code + "-" + product_code + "-" + stock_code

    document.getElementById("sku-output").innerHTML = f"Generated SKU: <strong>{sku}</strong>"



def order(event):
    
    menu = {
        "item1": ("Americano", 99),
        "item2": ("Spanish Latte", 129),
        "item3": ("Cold Brew Malt", 189),
        "item4": ("Affogato", 159),
        "item5": ("Caramel Macchiato", 129)
    }

    total = 0            
    items_ordered = []  
    for item_id, details in menu.items():
        checkbox = document.getElementById(item_id)
        if checkbox.checked:
            items_ordered.append(details[0])
            total += details[1]

    
    if len(items_ordered) == 0:
        document.getElementById("receipt-summary").innerHTML = "No items selected."
    else:
        summary = "<strong>Order Summary:</strong><br>"
        summary += "<br>".join(items_ordered)
        summary += f"<br><br><strong>Total Amount: ₱{total}</strong>"
        document.getElementById("receipt-summary").innerHTML = summary
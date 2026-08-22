import pandas as pd

# Load supplier and store data
supplier = pd.read_csv("supplier_inventory.csv")
store = pd.read_csv("store_inventory.csv")

print("Supplier Inventory:")
print(supplier)

print("\nStore Inventory:")
print(store)

import pandas as pd

# Load supplier and store data
supplier = pd.read_csv("supplier_inventory.csv")
store = pd.read_csv("store_inventory.csv")

# Merge both datasets on item_name
merged = pd.merge(supplier, store, on="item_name", suffixes=("_supplier", "_store"))

# Identify items out of stock in store but available at supplier
out_of_stock = merged[(merged['stock_quantity_store'] == 0) & (merged['stock_quantity_supplier'] > 0)]

# Print alerts
if not out_of_stock.empty:
    print("Out-of-stock alerts:")
    for item in out_of_stock['item_name']:
        print(f" - {item} is out of stock in store but available at supplier.")
else:
    print("All items are in sync.")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

def send_email_alert(items):
    sender = "belindaawinja0449@gmail.com"     # your Gmail address
    receiver = "belindahtom@gmail.com"         # recipient address
    password = "lyzu ryqv pmdh fydk"        # replace with Gmail app password

    subject = "Inventory Alert"
    body = "The following items are out of stock in store but available at supplier:\n" + "\n".join(items)

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully!")

# --- Inventory comparison logic ---
supplier = pd.read_csv("supplier_inventory.csv")
store = pd.read_csv("store_inventory.csv")

# Clean up item names (strip tabs, spaces)
supplier['item_name'] = supplier['item_name'].str.strip()
store['item_name'] = store['item_name'].str.strip()

# Merge inventories
merged = pd.merge(supplier, store, on="item_name", suffixes=("_supplier", "_store"))

# Find items where store = 0 but supplier > 0
out_of_stock = merged[(merged['stock_quantity_store'] == 0) & (merged['stock_quantity_supplier'] > 0)]

if not out_of_stock.empty:
    items = out_of_stock['item_name'].tolist()
    print("Out-of-stock alerts:")
    for item in items:
        print(f" - {item} is out of stock in store but available at supplier.")
    send_email_alert(items)
else:
    print("All items are in sync.")


# NorthStar Retail Co _ Live inventory sync service 

The Meridian Pivot:  This is a sprint‑phase prototype that tests adaptability under change — learning new tools, overcoming blockers, and refactoring deliverables to meet shifting requirements.
The project delivers a live inventory sync service that compares supplier (Y) and store (X) stock data, ensuring the support tool’s “is this in stock?” answers remain accurate. 
This prototype demonstrates independent learning (new tools for data sync and notifications), troubleshooting (documenting blockers and resolutions), and refactoring to meet pivot constraints. It also serves as evidence of adaptability, communication, and composure during the sprint evaluation phase.

# Conflict escalation path

| **Level** | **Action** | **Goal** | **Outcome** |
| --- | --- | --- | --- |
| **1. Self‑Resolution** | Document blockers in the **Learning & Blocker Journal** and attempt independent troubleshooting using docs, forums, and prototypes. | Solve issues independently and build resilience. | If resolved, record the fix and continue sprint work. |
| **2. Mentor Escalation** | Escalate unresolved blockers to sprint lead/mentor for guidance. | Gain clarity on trade‑offs, prioritization, or technical direction. | Document mentor input in the **Change Log** and adjust backlog accordingly. |
| **3. Final Reflection** | Capture the escalation path in the **Individual Adaptability Index**. | Reflect on composure, communication, and flexibility under pressure. | Demonstrate adaptability and structured problem‑solving in final evaluation. |

# Tool Assigned - Python with Pandas (data manipulation & automation)

- Documenting blockers while setting up Python environment and libraries.
- Created a script to merge supplier and store inventories, detect out‑of‑stock items, and trigger alerts.
- Adjusted logic to handle tab issues in CSV files and ensured duplicate protection.
- Delivered a working prototype that demonstrated adaptability under shifting requirements.

# 1. Setting Up the Inventory Folder
- Creating a folder named **Inventory sync**
- Inside, added two CSVs named, **Supplier Inventory** and **Store Inventory**

<img width="1085" height="888" alt="image" src="https://github.com/user-attachments/assets/0d05d32c-bd63-47ce-9ee3-909a5d7d00b5" />

# Scripting using Python and Pandas

For scripting the live inventory service, I'll be learning to use it with Python and Pandas technology

## Python Tool installation
First, I will confirm if python is successfully installed and verified in my terminal (PowerShell) by using, **python --version**

<img width="985" height="340" alt="image" src="https://github.com/user-attachments/assets/4cda2783-539c-4775-8c66-d9a27c5ab5cd" />

## Pandas Tool installation

Since I'm using  two technologies, I'll also have to install Pandas library and confirm it to be working

<img width="981" height="536" alt="image" src="https://github.com/user-attachments/assets/974dbc23-a98c-4b82-8d61-12bef13362ee" />

## Creating Script File

Created the script in a .py file called **sync_check.py**

[sync_check.py](https://github.com/user-attachments/files/31230173/sync_check.py)

### Running the script

Both commands load and display the CSV file contents
- cd path/to/inventory_sync
- python sync_check.py

<img width="981" height="480" alt="image" src="https://github.com/user-attachments/assets/b1a24842-5c31-493c-8919-a0c60741ffc6" />

# Loading and Comparing Data from both inventories

## Navigate to the folder, Merge the data, Identify Mismatches and print alerts

### pd.read_csn()
- This function from Pandas reads your CSV files and turns them into DataFrames

### Merge the data
- I used pd.merge() to combine both tables based on the shared column item_name.
- With this I compared each product’s stock side‑by‑side.

### Identifying Mismatches
- My filter rows are:
  - The store has no stock (stock_quantity_store == 0)
  - The supplier still has stock (stock_quantity_supplier > 0)
  
### Print Alerts
- This step ensures my support tool always gives accurate “is this in stock?” answers by comparing live supplier and store data.

- ** cd "E:/inventory sync" **
- ** python sync_check.py **

<img width="981" height="404" alt="image" src="https://github.com/user-attachments/assets/1f8e6bf0-d8b0-4518-aaa9-58608eb5c44e" />

# Adding Notifications and Automating the Sync

Extending the script to notify when items are out of stock in store but available at supplier.

I've achieve the notification with the SMTP - Email

<img width="986" height="518" alt="image" src="https://github.com/user-attachments/assets/ad72a1d0-bee5-4fcf-84f6-a855fea16092" />

** Email alert

<img width="1518" height="238" alt="image" src="https://github.com/user-attachments/assets/1117cc84-bfcd-4f86-b617-d42b622bf0ff" />

















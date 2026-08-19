# NorthStar Retail Co _ Live inventory sync service 

The Meridian Pivot:  This is a sprint‑phase prototype that tests adaptability under change — learning new tools, overcoming blockers, and refactoring deliverables to meet shifting requirements.
The project delivers a live inventory sync service that compares supplier (Y) and store (X) stock data, ensuring the support tool’s “is this in stock?” answers remain accurate. 
This prototype demonstrates independent learning (new tools for data sync and notifications), troubleshooting (documenting blockers and resolutions), and refactoring to meet pivot constraints. It also serves as evidence of adaptability, communication, and composure during the sprint evaluation phase.

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




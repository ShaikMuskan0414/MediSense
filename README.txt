# MediSense

Flow:
Registration -> Disease & Symptoms -> Hospital -> Insurance -> Payment -> Receipt

## 1. Put the dataset in this folder

Copy the original file without modifying it:

AP_Hospitals_Complete_Dataset.xlsx

## 2. Create the MySQL database

Run:

mysql -u root -p < schema.sql

## 3. Install Python packages

python3 -m pip install -r requirements.txt

## 4. Import the Excel data

python3 import_data.py

## 5. Run MediSense

python3 app.py

Open:
http://127.0.0.1:5000

## Important

The frontend keeps the original Registration and Disease & Symptoms UI.
A doctor-specialty recommendation now appears after a disease is selected. It suggests the appropriate type of specialist, but does not invent individual doctor names because the supplied dataset contains hospital specialties only.
Hospital information and insurance options are loaded from MySQL through Flask APIs.

Payment is still a frontend demo. It does not charge a real card or UPI account.

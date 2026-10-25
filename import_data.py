import pandas as pd
import mysql.connector
from database import DB_CONFIG

EXCEL_FILE = "AP_Hospitals_Complete_Dataset.xlsx"

COLUMN_MAP = {
    "Hospital Name": "hospital_name",
    "City": "city",
    "Address": "address",
    "Contact Number": "contact_number",
    "Email": "email",
    "Private Insurance Companies": "private_insurance_companies",
    "TPA Partners": "tpa_partners",
    "Government Schemes": "government_schemes",
    "Health Specialties": "health_specialties",
}


def clean(value):
    if pd.isna(value):
        return None
    return str(value).strip()


df = pd.read_excel(EXCEL_FILE)
df = df.rename(columns=COLUMN_MAP)

required = list(COLUMN_MAP.values())
missing = [c for c in required if c not in df.columns]

if missing:
    raise ValueError(
        "The Excel file is missing these expected columns: " + ", ".join(missing)
    )

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS hospitals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hospital_name VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    address TEXT,
    contact_number VARCHAR(100),
    email VARCHAR(255),
    private_insurance_companies TEXT,
    tpa_partners TEXT,
    government_schemes TEXT,
    health_specialties TEXT
)
""")

# This import replaces only the hospitals table data.
# The Excel source file itself is never modified.
cursor.execute("DELETE FROM hospitals")

sql = """
INSERT INTO hospitals
(hospital_name, city, address, contact_number, email,
 private_insurance_companies, tpa_partners, government_schemes,
 health_specialties)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    values = tuple(clean(row[c]) for c in required)
    cursor.execute(sql, values)

conn.commit()
print(f"Imported {len(df)} hospital records successfully.")

cursor.close()
conn.close()

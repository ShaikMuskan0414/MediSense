import os
import mysql.connector

DB_CONFIG = {
    "host": os.getenv("MEDISENSE_DB_HOST", "localhost"),
    "port": int(os.getenv("MEDISENSE_DB_PORT", "3306")),
    "user": os.getenv("MEDISENSE_DB_USER", "root"),
    "password": os.getenv("MEDISENSE_DB_PASSWORD", ""),
    "database": os.getenv("MEDISENSE_DB_NAME", "medisense_db"),
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def get_hospitals(specialty=""):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT id, hospital_name, city, address, contact_number, email,
               private_insurance_companies, tpa_partners,
               government_schemes, health_specialties
        FROM hospitals
    """
    params = []

    keyword_map = {
        "cardiology": "cardiology",
        "neurology": "neurology",
        "orthopedics": "orthopedic",
        "dermatology": "dermatology",
        "general": "general medicine",
        "ophthalmology": "ophthalmology",
        "ent": "ent",
        "gastro": "gastroenterology",
        "pulmonology": "pulmonology",
        "endocrinology": "endocrinology",
    }

    keyword = keyword_map.get(specialty.lower())
    if keyword:
        query += " WHERE LOWER(health_specialties) LIKE %s"
        params.append(f"%{keyword}%")

    query += " ORDER BY hospital_name"

    cursor.execute(query, params)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def get_hospital(hospital_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, hospital_name, city, address, contact_number, email,
               private_insurance_companies, tpa_partners,
               government_schemes, health_specialties
        FROM hospitals
        WHERE id = %s
    """, (hospital_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()
    return row

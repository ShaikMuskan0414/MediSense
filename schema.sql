CREATE DATABASE IF NOT EXISTS medisense_db;
USE medisense_db;

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
);

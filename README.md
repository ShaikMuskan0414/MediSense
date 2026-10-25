# MediSense — Medical Self-Service Kiosk

MediSense is a prototype medical self-service kiosk designed to help patients navigate a hospital-service workflow through a single web interface. It combines patient registration, symptom selection, doctor-specialty guidance, hospital information, insurance options, a simulated payment process, and receipt generation.

This project uses a sample Andhra Pradesh hospital dataset for development and demonstration. It is not connected to a live hospital system.

## Features

- **Patient registration:** Collects basic patient and contact information through a registration form.
- **Disease and symptoms:** Allows patients to select a condition, choose symptoms, and provide additional details.
- **Doctor-specialty recommendations:** Displays guidance about the type of specialist associated with a selected condition. These are predefined recommendations, not AI-generated diagnoses or verified individual doctor profiles.
- **Hospital directory:** Loads hospital details from a MySQL database and supports filtering by specialty.
- **Insurance information:** Displays private insurance companies, third-party administrators (TPAs), and government schemes recorded for the selected hospital.
- **Payment demonstration:** Provides card, cash, and UPI interface options for a simulated payment workflow. No real payment is processed.
- **Receipt generation:** Displays a summary of the patient, selected condition, hospital, insurance choice, and simulated payment. The current download function generates a text receipt.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Database | MySQL |
| Dataset processing | Pandas, OpenPyXL |
| Database connectivity | MySQL Connector/Python |

## Project Structure

```text
MediSense/
├── app.py
├── database.py
├── import_data.py
├── schema.sql
├── requirements.txt
├── README.md
├── AP_Hospitals_Complete_Dataset.xlsx
└── templates/
    └── index.html
```

## Requirements

Install the following before running the application:

- Python 3
- MySQL Server
- pip
- A modern web browser

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/ShaikMuskan0414/MediSense.git
cd MediSense
```

### 2. Install Python dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Configure MySQL

Make sure MySQL Server is running. Create the database and hospital table:

```bash
mysql -u root -p < schema.sql
```

Enter your MySQL password when prompted.

The default database configuration uses:
- Host: `localhost`
- Port: `3306`
- User: `root`
- Database: `medisense_db`

You can override these settings with environment variables:

```bash
export MEDISENSE_DB_HOST=localhost
export MEDISENSE_DB_PORT=3306
export MEDISENSE_DB_USER=root
export MEDISENSE_DB_PASSWORD='your_mysql_password'
export MEDISENSE_DB_NAME=medisense_db
```

Use your actual MySQL credentials. Do not commit passwords or other secrets to GitHub.

### 4. Import the hospital dataset

Ensure `AP_Hospitals_Complete_Dataset.xlsx` is in the project root, then run:

```bash
python3 import_data.py
```

The script reads the expected hospital columns from the Excel file and imports them into MySQL. It deletes the existing rows in the `hospitals` table before importing the dataset again. Back up any data you need before rerunning it.

The original Excel file is read, not modified.

### 5. Start the application

```bash
python3 app.py
```

Open the following address in your browser:

http://127.0.0.1:5000

Keep the Terminal process running while using the application.

## Backend API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Serves the MediSense interface |
| GET | `/api/hospitals` | Returns hospital records; an optional `specialty` query filters results |
| GET | `/api/hospitals/<hospital_id>/insurance` | Returns insurance and scheme options for a hospital |
| GET | `/api/specialties` | Returns the specialties listed in hospital records |

## Current Limitations

- This is a prototype and uses sample hospital data, not a verified live hospital directory.
- The application does not maintain a directory of verified individual doctors or real appointment schedules.
- Specialty recommendations are predefined guidance and must not be treated as medical diagnosis.
- Payment is simulated; no real card, cash, or UPI transaction is processed.
- The application does not integrate with a live hospital booking, billing, or insurance-approval system.
- The Flask development server is intended for local development, not production deployment.
- Patient information entered into the interface should be treated as sensitive. This prototype has not been assessed for production-grade privacy, security, or regulatory compliance.

## Future Improvements

- Integrate verified doctor profiles and availability from authorized sources.
- Add appointment scheduling and booking confirmation.
- Integrate a secure payment gateway in a test environment.
- Implement secure patient data storage, authentication, and access controls.
- Deploy using a production-ready web server and appropriate security measures.

## Disclaimer

MediSense is an educational prototype developed for demonstration and learning. Hospital records are sample data and must be verified before real-world use. The application does not replace professional medical advice, diagnosis, or treatment.

## Author

**Shaik Muskan**

GitHub: https://github.com/ShaikMuskan0414

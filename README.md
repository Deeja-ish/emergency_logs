# ER Operation and Bed Allocation Dashboard

A modern, high-end medical telemetry web dashboard built with Flask, MySQL, and Chart.js. This application queries, cleans, and visualizes real-time Emergency Room (ER) data to track unassigned (stranded) patients sorted by their clinical acuity scores.

## Features

- **Live Cleaned ER Data**: Standardizes, cleans, and extracts ER metrics directly from the raw database tables.
- **Dynamic Medical Telemetry Theme**: Sleek dark-mode UI utilizing modern typography (Inter), glassmorphic panels, CSS grid layouts, and hover interactions.
- **Horizontal Bar Visualization**: Interactive Chart.js chart demonstrating hallway traffic (stranded patients) categorized by acuity levels (1 to 5).
- **Critical Alert Counter**: Pulsing, color-coded medical alert panel highlighting the exact count of critical Level 5 acuity patients requiring immediate bed assignment.
- **Fully Responsive**: Adapts seamlessly to different screen sizes and devices (mobile, tablet, desktop).

---

## Technical Architecture

### 1. Database & Automated Cleaning Pipeline
The dashboard relies on a Common Table Expression (CTE) in MySQL to dynamically clean and normalize raw hospital log data at query-time:
- **Patient Name Cleaning**: Standardizes capitalization and removes underscores (`Tunde_Alao` $\rightarrow$ `TUNDE ALAO`).
- **Date Format Unification**: Standardizes dates from multiple inconsistent formats (e.g. `MM/DD/YYYY`, `MM-DD-YYYY`, `YYYY-MM-DD`) into a standard MySQL date format (`YYYY-MM-DD`).
- **Bed & Room Normalization**: Resolves null bed assignments to `'UNASSIGNED'` and normalizes abbreviations (e.g. `Rm 105`, `room 102`, `ROOM 105` $\rightarrow$ `ROOM 105`).
- **Insurance Alignment**: Maps missing values to `'SELF-PAY'` and trims whitespace.

### 2. Stack & Technologies
- **Backend**: Flask (Python)
- **Database Connector**: `mysql-connector-python`
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism, custom variables, keyframe animations)
- **Charts**: Chart.js (CDN)
- **Configuration**: `python-dotenv` for environment management

---

## Directory Structure

```text
emergency_logs/
│
├── app.py              # Main Flask application & database connector
├── dashboard.html      # Front-end UI template with Jinja data-binding
├── script.js           # Client-side Chart.js configuration
├── style.css           # Modern dark-mode styling & animations
├── .env                # Database environment variables (Excluded from Git)
└── README.md           # Project documentation (This file)
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server (running and accessible)
- Pip (Python Package Installer)

### Installation & Setup

1. **Clone or navigate** to the project directory:
   ```bash
   cd "c:/Users/Khadija Ismail/Documents/Sql_projects/Emergency _log/emergency_logs"
   ```

2. **Install dependencies**:
   ```bash
   pip install flask mysql-connector-python python-dotenv
   ```

3. **Configure Database Variables**:
   Create or edit the `.env` file inside the `emergency_logs` folder with your MySQL database credentials:
   ```env
   DB_HOST=localhost
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_NAME=emergency_log_data
   ```

4. **Initialize Database Schema & Data**:
   Ensure you have run the schema script located at the parent directory (`emergency_log_data.sql`) to set up the MySQL tables and insert raw hospital logs:
   ```bash
   mysql -u your_mysql_user -p < ../emergency_log_data.sql
   ```

---

## Running the Application

Start the Flask server by running the following command:
```bash
python app.py
```

The application will start in debug mode on port `5000`. You can access the dashboard in your web browser at:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## License
This project is open-source and available under the MIT License.

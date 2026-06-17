from flask import Flask, render_template
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

def get_er_dashboard_data():
    conn = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME').strip()
    )

    cursor = conn.cursor(dictionary=True)

    query = """
        WITH new_raw_hospital_logs AS (
            SELECT DISTINCT 
                log_id,
                UPPER(REPLACE(TRIM(patient_name), '_', ' ')) as cleaned_patient_name, 
                CASE 
                    WHEN admission_date LIKE '%/%' THEN STR_TO_DATE(admission_date, '%m/%d/%Y')
                    WHEN admission_date LIKE '__-__-____' THEN STR_TO_DATE(admission_date, '%m-%d-%Y')
                    ELSE STR_TO_DATE(admission_date, '%Y-%m-%d') 
                END AS cleaned_admission_date,
                acuity_score,
                CASE 
                    WHEN assigned_room IS NULL THEN 'UNASSIGNED' 
                    ELSE UPPER(REPLACE(REPLACE(TRIM(assigned_room), 'Rm', 'ROOM'), 'room', 'ROOM'))
                END AS cleaned_assigned_room,
                UPPER(COALESCE(TRIM(insurance_provider), 'SELF-PAY')) AS cleaned_insurance
            FROM raw_hospital_logs
        )
        SELECT acuity_score, COUNT(*) AS unassigned_patients
        FROM new_raw_hospital_logs
        WHERE cleaned_assigned_room = 'UNASSIGNED'
        GROUP BY acuity_score
        ORDER BY acuity_score DESC
    """

    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

@app.route("/")
def home():
    raw_metrics = get_er_dashboard_data()

    acuity_score = [row['acuity_score'] for row in raw_metrics]
    unassigned_patients = [row['unassigned_patients'] for row in raw_metrics]

    # Find the count of unassigned patients for acuity level 5 dynamically
    acuity_5_count = 0
    for row in raw_metrics:
        if row['acuity_score'] == 5:
            acuity_5_count = row['unassigned_patients']
            break

    return render_template('dashboard.html', acuity_score=acuity_score, patient_count=unassigned_patients, acuity_5_count=acuity_5_count)

if __name__ == "__main__" :
    app.run(debug=True, port='5000')



 Project Description
An end-to-end Airflow data pipeline that automtes transaction processing 
and sends email reports every 10 minutes using Doker and Python.

Tech Stack
- **Orchestration:** Apache Airflow
- **Language:** Python 3.x
- **Containerizatioon:** Docker
- **Operators:** PythonOperator, BashOperator, EmailOperator

DAG Workflow
The pipeline consists of 5 tasks:
1. **task1_start** — Initializes the workflow
2. **task2_process_transactions** — Prepares transaction data
3. **task3_run_script** — Runs the external Python script
4. **task4_read_report** — Reads the generated CSV report
5. **task5_send_email** — Sends the final report by email


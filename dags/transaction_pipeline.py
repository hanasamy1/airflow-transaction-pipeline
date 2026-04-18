from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
    "email_on_failure": False,
}

def start_pipeline():
    print("=== Pipeline Started ===")
    print(f"Time: {datetime.now()}")

def read_report():
    filepath = "/opt/airflow/shared/transaction_report.csv"
    with open(filepath, "r") as f:
        content = f.read()
    print("=== Transaction Report ===")
    print(content)

with DAG(
    dag_id="transaction_pipeline",
    default_args=default_args,
    description="Processes transactions every 10 minutes and sends email report",
    schedule_interval="*/10 * * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["transactions", "pipeline"],
) as dag:

    task1_start = PythonOperator(
        task_id="task1_start",
        python_callable=start_pipeline,
    )

    task2_process_transactions = PythonOperator(
        task_id="task2_process_transactions",
        python_callable=lambda: print("Processing transactions..."),
    )

    task3_run_script = BashOperator(
        task_id="task3_run_script",
        bash_command="python /opt/airflow/shared/process_transactions.py",
    )

    task4_read_report = PythonOperator(
        task_id="task4_read_report",
        python_callable=read_report,
    )

    task5_send_email = EmailOperator(
        task_id="task5_send_email",
        to="your_email@gmail.com",
        subject="Transaction Report",
        html_content="<h3>The transaction report has been generated successfully.</h3>",
    )

    task1_start >> task2_process_transactions >> task3_run_script >> task4_read_report >> task5_send_email

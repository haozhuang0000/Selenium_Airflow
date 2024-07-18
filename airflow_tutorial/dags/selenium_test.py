import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime

path = os.environ['AIRFLOW_HOME']
#dag.py
default_args = {
                'owner': 'YourName',
                'depends_on_past': False,
                'email': ['YourEmail@gmail.com'],
                'email_on_failure': False,
                'email_on_retry': False,
                'retries': 0,
                'retry_delay': timedelta(minutes=1)
                }


# Define the DAG, its ID and when should it run.
dag = DAG(
            dag_id='test_sl',
            start_date=datetime(year=2024, month=1, day=1),
            schedule_interval="@hourly",
            default_args=default_args,
            catchup=False
            )

# Define the task 1 (collect the data) id. Run the bash command because the task is in a .py file.
task = BashOperator(
                        task_id='get_data',
                        bash_command=f'python {path}/dags/src/main.py',
                        dag=dag)
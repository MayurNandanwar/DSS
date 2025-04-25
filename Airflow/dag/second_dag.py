# first task example 

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime ,timedelta

default_args = {
    'owner':'i',
    'retries':5,
    'retry_delay': timedelta(minutes=2)
}
with DAG(
    dag_id = 'my_first_dag',
    description = 'my first dag',
    start_date = datetime(2025,1,2,2) # means start with 2025 year 1st month a date is 2 at 2 am,
    schedule_interval = '@daily',
    default_args=default_args) as dag:
    
    task1 = BashOperator(
            task_id = 'my_first_dag',
            bash_command = 'echo hello, this is the first task'
        )
    
    task2 = BashOperator(
            task_id = 'second_dag',
            bash_command = 'echo second task'
        )
    task1.set_downstream(task2) # 

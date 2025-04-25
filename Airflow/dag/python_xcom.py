from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta


def geek():
    return 'may'

def pull_info_xcom(age,ti):
    name = ti.xcom_pull(task_ids = 'geek1')
    print(f'my name is {name} and age is {age}')


default_args = {'owner':'i',
                'retries':5,
                'retry_delay':timedelta(minutes=2)}

with DAG(
    dag_id = 'xcom'
    description='get information from task 1',
    start_date = datetime(2025,1,2),
    schedule_interval = '@daily',
    default_args = default_args
    ) as dag:

    task1 = PythonOperator(
            task_id = 'geek1',
            python_callable = geek
        )
    task2 = PythonOperator(task_id = 'task2',
                           python_collable = pull_info_xcom
                        )
    
    task1>>task2
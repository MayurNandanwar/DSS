from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta


def geek(ti):
    ti.xcom_push(key='first_name',value='may')
    ti.xcom_push(key='last_name',value='nandan')


def pull_info_xcom(age,ti):
    first_name = ti.xcom_pull(task_ids = 'geek1',key='first_name')
    last_name = ti.xcom_pull(task_ids = 'geek1',key = 'last_name')
    print(f'my name is {first_name} and lastname is {last_name} and age is {age}')


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
            python_callable = geek,
            
        )
    task2 = PythonOperator(task_id = 'pull_info_xcom',
                           python_collable = pull_info_xcom,
                           op_kwargs = {'age':20}
                        )
    
    task1>>task2
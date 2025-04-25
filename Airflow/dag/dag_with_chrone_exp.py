from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

default_params = {"owner":'i',
                  "retries":5,
                  "retry_delay": timedelta(minutes=2)
                }

def add():
    return 1+1

with DAG(dag_id='adding',
         description='adding',
         start_date=datetime(2022,1,1),
         schedule_interval='0 0 26 * sun',
         catchup=False):
    task1 = PythonOperator(task_ids ='add',
                           python_callable=add)
    
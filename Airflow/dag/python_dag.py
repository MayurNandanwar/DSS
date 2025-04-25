from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'i',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
    }

def greet(name, age):
    return f'hello world my name is {name} and my age is {age}'


with DAG(dag_id= 'python_dag',
         description = 'python dag',
         start_date = datetime(2025,1,2), # from 2 daily at 12 o'clock  
         schedule_interval = '@daily',
         default_args = default_args
         ) as dag:

    task1 = PythonOperator(task_id ='greet',
                           python_callable = greet,
                           op_kwargs = {'name':'may','age':20}
                           )
    task1


# we can share information between task using airflow Xcom
from airflow import DAG
from datetime import datetime,timedelta
from airflow.decorators import dag,task

default_args = {
        'owner':'i',
        'retries':5,
        'retry_delay': timedelta(minutes=3)
        }

@dag(dag_id = 'dag_one',
     description='task_flow_api',
     default_args=default_args,
     start_date=datetime(2025,1,2),
     schedule_interval='@daily')
def hello_world_etl():

    @task
    def get_name():
        return 'jerry'

    @task
    def get_age():
        return 12
    
    @task
    def greet(name,age):
        print(f'hello name is {name} and age is {age}')

    name = get_name()
    age = get_age()
    greet(name,age)

# here task_flow api automatically define dependency
greet_dag = hello_world_etl()
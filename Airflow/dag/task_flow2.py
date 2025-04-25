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

    @task(multiple_outputs=True)
    def get_name():
        return {'first_name':'jerry',
                'last_name':'nandan'}

    @task
    def get_age():
        return 12
    
    @task
    def greet(firstname,lastname,age):
        print(f'hello name is {firstname} and lastname is {lastname} and age is {age}')

    name_dict = get_name()
    age = get_age()
    greet(name_dict['first_name'],name_dict['last_name'],age)

# here task_flow api automatically define dependency
greet_dag = hello_world_etl()
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner':'i',
    'retries':4,
    'retry_delay':timedelta(minutes=2)}

with DAG(dag_id='connection_postgres',
         description='aaa',
         start_date=datetime(2022,1,1),
         schedule_interval='2 * * * *',
         default_args=default_args):
    
    task1 = PostgresOperator(task_id ='create_table',
                             postgres_conn_id = 'created in airflow',
                             sql = '''create table my_tbl id int Primary Key,
                             name varchar
                                ''')
    
    task2 = PostgresOperator(task_id = 'insert_into_pg',
                             postgres_conn_id = 'created in airflow',
                             sql = """ Insert into my_tbl(id,name) values ('{{1}}','{{'mayur'}}');

                            """)
    task1>task2
    
    


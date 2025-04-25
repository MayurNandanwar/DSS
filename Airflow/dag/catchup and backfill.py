
from airflow import DAG 
from datetime import datetime,timedelta
from airflow.bashoperators.bash import BashOperator


default_args = {'owner':'i',
                'retries':5,
                'retry_delay':timedelta(minutes=2)
                }
with DAG(
    dag_id = 'third_dag',
    description = "this is third dag",
    start_date = datetime(2024,12,31) # 2am at 2nd daate 1st month 2025,
    schedule_interval = '@daily',
    default_args=default_args,
    catchup=True
    ) as dag:

    task1 = BashOperator(
        task_id = 'first',
        bash_command = 'echo fiest dag'
        )
    
    task2 = BashOperator(
        task_id = 'second_'
        bash_command = 'echo second'
        )
    
    task3 = BashOperator(
        task_id = 'third',
        bash_command = 'echo third'
        )
    
    # now task 2 and 3 will run parallaly and after task 1
    ## 1st method
    task1.set_downstream(task2)
    task1.set_downstream(task3)

    ## 2nd method 
    task1>>task2
    task1>>task3

    # 3rd method 
    task1>>[task2, task3]

    #Note: use one of three  from date 2024,12,31 to this date all dag will be run.


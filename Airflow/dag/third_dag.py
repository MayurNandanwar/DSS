
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
    start_date = datetime(2025,1,2,2) # 2am at 2nd daate 1st month 2025,
    schedule_interval = '@daily',
    default_args=default_args
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
    
    # now task 2 and 3 will run parallay and after task 1
    ## 1st method
    task1.set_downstream(task2)
    task1.set_downstream(task3)

    ## 2nd method 
    task1>>task2
    task1>>task3

    # 3rd method 
    task1>>[task2, task3]

# once file arrived in amazone s3 then trigger airflow that file has been arrived 

# look in airflow providers doc 
from airflow import DAG
from airflow.providers.amazone.aws.sensors.s3_key import S3KeySensor
from datetime import datetime,timedelta


with DAG(dag_id = 'aaa',
         start_date=datetime(2020,1,11),
         schedule_interval='@daily',
         catchup =False,
         description='sensor'
         ):
    task1 = S3KeySensor(task_id = 'sensor_',
                        bucket_name = 'airflow',
                        bucket_key = 'data.csv',
                        aws_conn_id = 's3_conn',
                        mode = 'Poke',
                        poke_interval = 10,
                        timeout = 30)  # 30 second
    # poke continuously monitor that file came or not and watch till what we have set in timeout

    
    task1

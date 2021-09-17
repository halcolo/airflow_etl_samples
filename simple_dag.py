from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# 1- Configs as args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
  
# 2 - Dag creation
with DAG(
  'Simple Dag',
  default_args=default_args,
  description='A simple tutorial DAG',
  schedule_interval=timedelta(days=1),
  start_date=days_ago(2),
  tags=['example'],
) as dag:
  
# 3 - Task
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
)
 
# 4 - WORKFLOW
t1 >> t2

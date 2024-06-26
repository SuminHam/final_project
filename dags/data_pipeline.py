from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from pendulum import datetime

from module import get_data


@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def data_pipeline():
    start_task = EmptyOperator(task_id="start_task")

    boxoffice_task = PythonOperator(
        task_id="box_office",
        python_callable=get_data.get,
    )

    movieinfo_task = PythonOperator(
        task_id="movie_info",
        python_callable=get_data.update_movie_info,
    )

    end_task = EmptyOperator(task_id="end_task")

    start_task >> [boxoffice_task, movieinfo_task] >> end_task


data_pipeline()

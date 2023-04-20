import os

import psycopg2
from pydantic import BaseModel

database_postgres = "postgres"
host_postgres = "containers-us-west-179.railway.app"
user_postgres = "postgres"
password_postgres = "grT1581tkP6rYZy9DXVQ"


class Postgres(BaseModel):

    def connect_postgres():
        conn = psycopg2.connect(
            database=database_postgres, host=host_postgres, user=user_postgres, password=password_postgres)
        cur = conn.cursor()

        return cur, conn

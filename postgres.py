import os

import psycopg2
from pydantic import BaseModel

database_postgres = "railway"
host_postgres = "containers-us-west-92.railway.app"
user_postgres = "postgres"
password_postgres = "GQcqIDhpYMQe2TzM4l2d"
port_postgres = 7184


class Postgres(BaseModel):

    def connect_postgres():
        conn = psycopg2.connect(
            database=database_postgres, host=host_postgres, user=user_postgres, password=password_postgres, port=port_postgres)
        cur = conn.cursor()

        return cur, conn

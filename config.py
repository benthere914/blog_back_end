import os
username = "benthere914"
password = "password"
rds_endpoint = "aa168dne82z8rx4.c4exkio8rsp6.us-west-2.rds.amazonaws.com"
rds_port = "5432"
rds_database_name = "ebdb"
class Config:
    SECRET_KEY = 'SECRET'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{rds_endpoint}:{rds_port}/{rds_database_name}"

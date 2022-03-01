import os
import boto3
from dotenv import load_dotenv
from flask import Blueprint, request
from models import Picture
load_dotenv()
s3 = boto3.client("s3")
picture_routes = Blueprint('pictures', __name__)

@picture_routes.route('/', methods=["POST"])
def add_picture():
    file = request.files['file']
    result = s3.upload_fileobj(file, os.getenv('AWS_BUCKET_NAME'), file.filename, ExtraArgs={'ACL': 'public-read'})
    print(result)
    return {'message': 'got here'}


@picture_routes.route('/')
def all_pictures():
    return {'message': 'hello yooo'}

import os

from flask import Blueprint, jsonify, request
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

assets_bp = Blueprint('assets', __name__)

load_dotenv()

# Get the S3 bucket name and credentials from the .env file
s3_bucket = os.getenv("S3_BUCKET_NAME")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Create an S3 client object
s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Assets route
@assets_bp.route('/assets')
def assets():
    asset_list = [
        {"id": 1, "name": "Asset 1"},
        {"id": 2, "name": "Asset 2"},
        {"id": 3, "name": "Asset 3"},
    ]
    return jsonify(asset_list)

# Single asset route
@assets_bp.route('/asset/<int:asset_id>')
def asset(asset_id):
    assets = [
        {"id": 1, "name": "Asset 1"},
        {"id": 2, "name": "Asset 2"},
        {"id": 3, "name": "Asset 3"},
    ]
    asset = next((a for a in assets if a["id"] == asset_id), None)
    if asset:
        return jsonify(asset)
    else:
        return "Asset not found", 404

@assets_bp.route("/upload", methods=["POST"])
def upload_file():
    # Get the file from the request object
    file = request.files["file"]

    # Upload the file to S3
    try:
        s3_client.upload_fileobj(
            file,
            s3_bucket,
            file.filename
        )
        return "File uploaded successfully"
    except ClientError as e:
        print(e)
        return "Error uploading file"

@assets_bp.route('/download/<filename>')
def download_file(filename):
    # Get the file from S3
    try:
        response = s3_client.get_object(Bucket=s3_bucket, Key=filename)
        file_data = response["Body"].read()
    except ClientError as e:
        print(e)
        return f"Error: File '{filename}' not found"

    # Return the file to the user for download
    return send_file(
        io.BytesIO(file_data),
        as_attachment=True,
        attachment_filename=filename
    )
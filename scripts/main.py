import json
import uuid

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from dependencies import authenticate_app
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

bucket_name = os.getenv("AWS_S3_BUCKET")
event_file_key = "event.log"


class Event(BaseModel):
    event_type: str
    event_data: dict


@app.post("/events")
async def log_event(event: Event, app_data: dict = Depends(authenticate_app)):
    event_id = uuid.uuid4()
    event_data = json.dumps({"event_id": str(event_id), **event.dict()})

    # Get the current contents of the event log file
    response = s3.get_object(Bucket=bucket_name, Key=event_file_key)
    current_data = response["Body"].read().decode("utf-8")

    # Append the new event data to the file
    new_data = current_data + "\n" + event_data
    s3.put_object(Bucket=bucket_name, Key=event_file_key, Body=new_data)

    return {"event_id": event_id}

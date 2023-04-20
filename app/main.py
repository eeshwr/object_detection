from fastapi import FastAPI
#from app.channel import rm_client
import pickle
from app import config 
from app.rabbitmq.channel import create_channel
from app.rabbitmq import producer

app = FastAPI()

@app.post("/object_in_image")
async def detect_objects(image_url):
    message = {
        "type": "image",
        "url": image_url,
        "output_location": config.output_location,
    }
    channel=create_channel(host=config.host, port=config.port, user=config.username, password=config.password)
    producer.produce(channel=channel, body=pickle.dumps(message), queue=config.queue_name, exchange=config.exchange)
    return {"Your request has been submitted"}

from fastapi import FastAPI
# from channel import rm_client
import pickle
from app import config 

app = FastAPI()


# define your object detection API endpoint
# @app.post("/object_in_image")
# async def detect_objects(image_url):
#     message = {
#         "type": "image",
#         "url": image_url,
#         "output_location": config.output_location,
#     }
#     rm_client.basic_publish(
#         exchange=config.exchange,
#         routing_key=config.queue_name,
#         body=pickle.dumps(message),
#     )

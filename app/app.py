# from app.channel import rm_client
from app import config
from app.detect import detect_and_save
import pickle
from app.rabbitmq.channel import create_channel
from app.rabbitmq.consumer import consume


def call_back(ch, method, properties, body):
    message = pickle.loads(body)
    image_url = message.get("url")
    output_location = message.get("output_location")
    detect_and_save(image_url, output_location)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consuming():
    channel = create_channel(
        host=config.host,
        port=config.port,
        user=config.username,
        password=config.password,
    )
    consume(
        channel=channel,
        handler=call_back,
        queue=config.queue_name,
        prefetch_count=config.prefetch_count,
    )
    channel.start_consuming()


start_consuming()

from channel import rm_client
from app import config
from detect import detect_and_save
import pickle


def call_back(ch, method, body):
    message = pickle.loads(body)
    image_url = message.get("image_url")
    output_location = message.get("output_location")
    detect_and_save(image_url, output_location)
    ch.basic_ack(delivery_tag=method.delivery_tag)


rm_client.basic_qos(prefetch_count=1)
rm_client.basic_consume(queue=config.queue_name, on_message_callback=call_back)
rm_client.start_consuming()

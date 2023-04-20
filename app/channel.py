import pika  # type: ignore
from pika import PlainCredentials
from app import config

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=PlainCredentials(config.username, config.password),
    )
)
rm_client = connection.channel()
rm_client.queue_declare(queue=config.queue_name)

# this file is not in use. I will delete it later

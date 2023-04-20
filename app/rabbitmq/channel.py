import pika  # type: ignore
from pika import PlainCredentials


def create_channel(host, port, user, password):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=host,
            port=port,
            credentials=PlainCredentials(user, password),
        )
    )
    return connection.channel()

from app.rabbitmq import producer
from unittest.mock import Mock
from .__mocks__ import pika
from app import config


def test_sender_publish_new_message(monkeypatch):
    channel = pika.Channel()
    channel.basic_publish = Mock()

    producer.produce(channel, "ISHWOR", config.queue_name, config.exchange)

    channel.basic_publish.assert_called_once_with(
        routing_key=config.queue_name, exchange=config.exchange, body="ISHWOR"
    )

import pytest
from app.rabbitmq import producer
from unittest.mock import Mock
from tests.__mocks__ import pika
from app import config


@pytest.mark.unit
def test_sender_publish_new_message(monkeypatch):
    channel = pika.Channel()
    channel.basic_publish = Mock()

    producer.produce(channel, "ISHWOR")

    channel.basic_publish.assert_called_once_with(
        routing_key=config.queue_name, exchange=config.exchange, body="ISHWOR"
    )

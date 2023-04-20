import pytest
from app.rabbitmq import consumer
from unittest.mock import Mock
from tests.__mocks__ import pika
from app import config


def mocked_handler():
    pass


@pytest.mark.unit
def test_consumer_queue_declared(monkeypatch):
    channel = pika.Channel()
    channel.queue_declare = Mock()

    consumer.consume(channel, mocked_handler)

    channel.queue_declare.assert_called_once_with(
        queue=config.queue_name,
        durable=True,
    )


@pytest.mark.unit
def test_consumer_basic_qos(monkeypatch):
    channel = pika.Channel()
    channel.basic_qos = Mock()

    consumer.consume(channel, mocked_handler)

    channel.basic_qos.assert_called_once_with(
        prefetch_count=config.prefetch_count,
    )


@pytest.mark.unit
def test_consumer_basic_consume(monkeypatch):
    channel = pika.Channel()
    channel.basic_consume = Mock()

    consumer.consume(channel, mocked_handler)

    channel.basic_consume.assert_called_once_with(
        queue=config.queue_name,
        on_message_callback=mocked_handler,
    )

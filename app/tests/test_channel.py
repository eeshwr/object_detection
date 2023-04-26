import pytest
from app.rabbitmq import channel
from unittest.mock import Mock
from .__mocks__ import pika


@pytest.mark.unit
def test_channel_creates_connection(monkeypatch):
    mocked_pika = Mock()
    mocked_pika.BlockingConnection.return_value = pika.Connection()
    channel.create_channel("ISHWOR HOST", 123, "USER", "PASSWORD")

    mocked_pika.BlockingConnection.assert_called_once_with(
        host="ISHWOR HOST", port=123, user="USER", password="PASSWORD"
    )

import os

host = os.environ.get("RABBITMQ_HOST", "localhost")
port = os.environ.get("RABBITMQ_PORT", 5672)
username = os.environ.get("RABBITMQ_USERNAME", "guest")
password = os.environ.get("RABBITMQ_PASSWORD", "guest")
queue_name = os.environ.get("QUEUE_NAME", "my_queue")
exchange = os.environ.get("RABBITMQ_EXCHANGE", "")
prefetch_count = os.environ.get("RABBITMQ_PREFETCH_COUNT", 1)
output_location = os.environ.get("OUTPUTLOCATION", "/")

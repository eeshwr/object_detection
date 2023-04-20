def produce(
    channel,
    body,
    queue,
    exchange,
):
    channel.queue_declare(queue=queue)
    channel.basic_publish(routing_key=queue, exchange=exchange, body=body)

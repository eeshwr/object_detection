
def consume(
    channel,
    handler,
    queue,
    prefetch_count,
):
    channel.queue_declare(queue=queue)
    channel.basic_qos(prefetch_count=prefetch_count)
    channel.basic_consume(queue=queue, on_message_callback=handler)

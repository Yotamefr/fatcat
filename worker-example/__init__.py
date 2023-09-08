from fatcat_utils.rabbitmq import RabbitMQHandler, AckTime
import aio_pika
import json


rabbit = RabbitMQHandler()


@rabbit.subscribe("queue1", ack=AckTime.End)
async def queue1_message(message: aio_pika.IncomingMessage):
    print(f"Message Queue: {message.routing_key}")
    print("Message Content:")
    print(json.dumps(json.loads(message.body.decode("utf-8")), indent=2))


@rabbit.subscribe("queue2", ack=AckTime.End)
async def queue2_message(message: aio_pika.IncomingMessage):
    print(f"Message Queue: {message.routing_key}")
    print("Message Content:")
    print(json.dumps(json.loads(message.body.decode("utf-8")), indent=2))


@rabbit.subscribe("queue3", ack=AckTime.End)
async def queue3_message(message: aio_pika.IncomingMessage):
    print(f"Message Queue: {message.routing_key}")
    print("Message Content:")
    print(json.dumps(json.loads(message.body.decode("utf-8")), indent=2))


def setup_worker():
    print("This is the setup function. You must include it in your worker.")
    print("Modify this function to run stuff on start (or just leave it empty)")
    print("Note that this function can also be async.")

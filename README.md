# FatCat
A generic, modular worker system.

Uses RabbitMQ and MongoDB.

Also uses Elasticsearch for logs (but this is optional).

## [FatCat Worker](https://github.com/yotamefr/fatcat-worker)
Does executes the scripts. You can place the scripts in a git repo or a local directory (such as [this one](worker-example)).

## [FatCat Server](https://github.com/yotamefr/fatcat-server)
Listens to the `incoming` queue in the RabbitMQ, validates and modifies the messages according to the schemas in the MongoDB, and sends the result to the correct queue (according to the `FATCAT_QUEUE_TAG` key in the message).

Note that messages must be in a JSON format.

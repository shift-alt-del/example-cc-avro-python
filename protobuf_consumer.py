from confluent_kafka import DeserializingConsumer
from confluent_kafka.avro import SerializerError
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufDeserializer

from protobuf.sr_pb2 import Person

try:
    # import some credentials, please refer to readme and get your own security info.
    from env import *
except:
    pass

CONSUMER_GROUP_ID = 'xxxx4'
TOPIC_NAME = 'xxx'

# where to get the schema
sr_client = SchemaRegistryClient({
    'url': SR_URL,
    'basic.auth.user.info': SR_BASIC_AUTH_USER_INFO
})

# consumer configurations
# for full list of configurations, see:
# https://docs.confluent.io/platform/current/clients/confluent-kafka-python/#serializingproducer
conf = {}

# broker leve configurations
conf.update({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'sasl.username': SASL_USERNAME,
    'sasl.password': SASL_PASSWORD,
    'sasl.mechanisms': 'PLAIN',  # fixed to sasl_ssl, plain
    'security.protocol': 'SASL_SSL',  # fixed to sasl_ssl, plain
})

# serdes configurations
conf.update({
    # use default key.deserializer
    'value.deserializer': ProtobufDeserializer(Person),
})

# consumer specific configurations
conf.update({
    'auto.offset.reset': 'earliest',
    'group.id': CONSUMER_GROUP_ID,
})

# initialize consumer instance
consumer = DeserializingConsumer(conf)
consumer.subscribe([TOPIC_NAME])

while True:
    try:
        msg = consumer.poll(1.0)
        if msg is None:
            # No message available within timeout.
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting for message or event/error in poll()")
            continue
        elif msg.error():
            print('error: {}'.format(msg.error()))
        else:
            key_object = msg.key()
            person_object = msg.value()

            print((key_object, person_object))

    except KeyboardInterrupt:
        break
    except SerializerError as e:
        # Report malformed record, discard results, continue polling
        print("Message deserialization failed {}".format(e))
        pass

from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer

from protobuf.sr_pb2 import Person

try:
    # import some credentials, please refer to readme and get your own security info.
    from env import *
except:
    pass

TOPIC_NAME = 'xxx'

sr_client = SchemaRegistryClient({
    'url': SR_URL,
    'basic.auth.user.info': SR_BASIC_AUTH_USER_INFO,
})

# https://docs.confluent.io/platform/current/schema-registry/develop/api.html#put--config-(string-%20subject)
# BACKWARD, BACKWARD_TRANSITIVE, FORWARD, FORWARD_TRANSITIVE, FULL, FULL_TRANSITIVE, NONE
print(sr_client.get_compatibility('xxx-value'))
sr_client.set_compatibility(level='NONE', subject_name='xxx-value')

# producer configurations
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
    # 'key.serializer': ProtobufSerializer(Person, sr_client),
    'value.serializer': ProtobufSerializer(Person, sr_client),
})

# https://developers.google.com/protocol-buffers/docs/pythontutorial
# http://google.github.io/proto-lens/installing-protoc.html
person = Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = Person.HOME

# initialize producer instance
producer = SerializingProducer(conf)
producer.produce(
    topic=TOPIC_NAME,
    key=person.email,
    value=person
)
producer.poll(0)
producer.flush()

print('done')

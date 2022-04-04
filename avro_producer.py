from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

try:
    # import some credentials, please refer to readme and get your own security info.
    from env import *
except:
    pass

TOPIC_NAME = 'xxx'

value_schema_str = """
{
   "namespace": "my.test",
   "name": "value",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     },
     {
        "name" : "xxxxx",
        "type": "string",
        "default" : "1234"
     }
   ]
}
"""

key_schema_str = """
{
   "namespace": "my.test",
   "name": "key",
   "type": "record",
   "fields" : [
     {
       "name" : "name",
       "type" : "string"
     }
   ]
}
"""

sr_client = SchemaRegistryClient({
    'url': SR_URL,
    'basic.auth.user.info': SR_BASIC_AUTH_USER_INFO,
})

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
    'key.serializer': AvroSerializer(sr_client, schema_str=key_schema_str),
    'value.serializer': AvroSerializer(sr_client, schema_str=value_schema_str),
})

# initialize producer instance
producer = SerializingProducer(conf)
producer.produce(
    topic=TOPIC_NAME,
    key={'name': 'keykey'},
    value={'name': 'valuevalue', 'abc': 'ss'}
)
producer.poll(0)
producer.flush()

print('done')

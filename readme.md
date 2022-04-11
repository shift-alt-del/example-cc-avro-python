# Schema Registry example with Confluent Cloud

How to work with Schema registry. Trying to make is simple and straightforward in this example. You can
also refer to the [Official example](https://github.com/confluentinc/examples/tree/7.0.1-post/clients/cloud/python).

[Blog: Schemas, Contracts, and Compatibility](https://www.confluent.io/blog/schemas-contracts-compatibility/)

## Confluent Cloud Prep:

- Visit https://confluent.cloud to create an account ($400 free credit available.)
- Install python3
- Install requirements by `pip install -r requirements.txt`
- Create environment / Cluster / Tokens
- Create env.py file as below:
- ```
  BOOTSTRAP_SERVERS = '(server)'
  SASL_USERNAME = '(key)'
  SASL_PASSWORD = '(password)'
  SR_URL = '(SR server)'
  SR_BASIC_AUTH_USER_INFO = '(SR key):(SR password)'
  ```

## Avro demo:

```
python3 sr_producer.py
python3 sr_consumer.py
```

## ProtoBuf demo:

```
python3 protobuf_producer.py
python3 protobuf_consumer.py
```
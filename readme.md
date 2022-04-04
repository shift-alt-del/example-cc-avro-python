# Schema Registry example with Confluent Cloud

How to work with AVRO message to Confluent cloud. Trying to make is simple and straightforward in this example. You can
also refer to the [Official example](https://github.com/confluentinc/examples/tree/7.0.1-post/clients/cloud/python).

## Prep:

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

## Run:

```
python3 avro_producer.py
python3 avro_consumer.py
```
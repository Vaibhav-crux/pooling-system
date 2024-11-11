from kafka import KafkaProducer, KafkaConsumer
from app.config.db_config import Config

producer = KafkaProducer(bootstrap_servers=[Config.KAFKA_BROKERS], value_serializer=lambda v: v.encode('utf-8'))
consumer = KafkaConsumer(Config.KAFKA_TOPIC, bootstrap_servers=[Config.KAFKA_BROKERS], auto_offset_reset='earliest', enable_auto_commit=True, group_id='poll-group')

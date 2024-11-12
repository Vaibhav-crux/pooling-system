from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient

KAFKA_BROKERS = "localhost:9092"
KAFKA_TOPIC = "polls-topic"

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS)
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS)
admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKERS)

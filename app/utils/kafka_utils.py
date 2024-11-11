from app.config.db_config import Config
from app.config.kafka import producer

def send_vote_to_kafka(vote_data: dict):
    producer.send(Config.KAFKA_TOPIC, value=vote_data)

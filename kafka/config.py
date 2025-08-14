from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

SRC_KAFKA_CONFIG = {
    "bootstrap.servers" : os.getenv("SRC_BOOTSTRAP_SERVERS"),
    "security.protocol" : os.getenv("SRC_SECURITY_PROTOCOL"),
    "sasl.mechanism" : os.getenv("SRC_SASL_MECHANISM"),
    "sasl.username": os.getenv("SRC_SASL_USERNAME"),
    "sasl.password": os.getenv("SRC_SASL_PASSWORD"),
    "auto.offset.reset": os.getenv("DST_AUTO_OFFSET_RESET", "earliest"),
    "group.id": "remote-consumer-group"
}

SRC_KAFKA_TOPIC = os.getenv("SRC_TOPIC")


DST_KAFKA_CONFIG = {
    "bootstrap.servers": os.getenv("DST_BOOTSTRAP_SERVERS"),
    "security.protocol": os.getenv("DST_SECURITY_PROTOCOL", "PLAINTEXT"),  
    "group.id": os.getenv("DST_GROUP_ID", "local-consumer-group"),  
    "auto.offset.reset": os.getenv("DST_AUTO_OFFSET_RESET", "earliest"), 
}

DST_KAFKA_TOPIC = os.getenv("DST_TOPIC")

MONGO_CONFIG = {
    "uri": os.getenv("MONGO_URI"),
    "db": os.getenv("MONGO_DB"),
    "collection": os.getenv("MONGO_COLLECTION")
}
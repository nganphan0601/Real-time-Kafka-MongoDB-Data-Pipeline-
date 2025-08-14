from confluent_kafka import Consumer
from pymongo import MongoClient
from config import DST_KAFKA_CONFIG, MONGO_CONFIG, DST_KAFKA_TOPIC
import json

# Consumer to get the messages from local Kafka
consumer = Consumer(DST_KAFKA_CONFIG)
consumer.subscribe([DST_KAFKA_TOPIC])

# Connect to MongoDB database
db_url = MONGO_CONFIG["uri"]
db_name = MONGO_CONFIG["db"]
db_collection = MONGO_CONFIG["collection"]

client = MongoClient(db_url)
db = client[db_name]
collection = client[db_collection]

# Batch settings
batch = []
BATCH_SIZE = 10

try:
    # test connection
    client.admin.command('ping')
    print("Connected successfully to MongoDB!")

    while True:
        msg = consumer.poll(1.0) # Poll for 1 second

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        try:
            # Decode message
            raw = msg.value().decode("utf-8")

            # Try to parse as JSON 
            try:
                doc = json.loads(raw) 
            except json.JSONDecodeError:
                # If not JSON, wrap as text
                doc = {"message": raw}

            batch.append(doc)

            if len(batch) >= BATCH_SIZE:
                collection.insert_many(batch)
                print(f"Inserted batch of {len(batch)} messages.")
                batch.clear()

        except Exception as e:
            print(f"Error processing message: {e}")
            continue
    
except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    if batch:
        collection.insert_many(batch)
    consumer.close()
    client.close()
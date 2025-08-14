from confluent_kafka import Consumer, Producer
from config import SRC_KAFKA_CONFIG, SRC_KAFKA_TOPIC, DST_KAFKA_CONFIG, DST_KAFKA_TOPIC

# Consumer to read messages from source Kafka
src_consumer = Consumer(SRC_KAFKA_CONFIG)
src_consumer.subscribe([SRC_KAFKA_TOPIC])

# Producer to produce the messages into the destination Kafka cluster
producer = Producer(DST_KAFKA_CONFIG)

try:
    while True:
        msg = src_consumer.poll(1.0) # Poll for 1 second

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        
        message_value = msg.value()

        print(f"✅Received message: {message_value.decode('utf-8')}")

        # Produce the messages to local Kafka
        producer.produce(DST_KAFKA_TOPIC, value=message_value)
        producer.flush()

except KeyboardInterrupt:
    print("\n Stopped by user.")
finally:
    src_consumer.close()
    producer.flush()
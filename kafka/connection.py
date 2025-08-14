from confluent_kafka import Producer, Consumer

# Replace with your actual public IP and topic
VM_BOOTSTRAP = "184.65.102.67:9094"
TEST_TOPIC = "test_topic"

# Create a producer
p = Producer({"bootstrap.servers": VM_BOOTSTRAP})
p.produce(TEST_TOPIC, value="test from Python!")
p.flush()

# Create a consumer to verify
c = Consumer({
    "bootstrap.servers": VM_BOOTSTRAP,
    "group.id": "test-group",
    "auto.offset.reset": "earliest"
})
c.subscribe([TEST_TOPIC])
msg = c.poll(timeout=3.0)

if msg:
    print("✅ Received from VM:", msg.value().decode('utf-8'))
else:
    print("❌ No message received")

c.close()

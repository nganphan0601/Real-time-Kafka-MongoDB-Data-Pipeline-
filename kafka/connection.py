from confluent_kafka.admin import AdminClient
BOOTSTRAP = "184.65.102.67:9094,184.65.102.67:9194,184.65.102.67:9294"
a = AdminClient({"bootstrap.servers": BOOTSTRAP})
md = a.list_topics(timeout=5)
print("ClusterID:", md.cluster_id)
for b in md.brokers.values():
    print("Broker:", b.id, b.host, b.port)

from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

src_kafka_brokers = os.getenv("SRC_BOOTSTRAP_SERVERS")
src_security_protocol = os.getenv("SRC_SECURITY_PROTOCOL")
# print(src_kafka_brokers)
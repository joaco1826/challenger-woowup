import os
from dotenv import load_dotenv

load_dotenv()


class MongoConstants:
    URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    EMAIL_COLLECTION = "emails"

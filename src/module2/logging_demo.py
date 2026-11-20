import logging

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

logging.info("This is an info message")
logging.warning("low disk space")
logging.error("This is an error message")

print("logging completed successfully")
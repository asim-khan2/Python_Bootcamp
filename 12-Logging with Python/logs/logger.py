import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
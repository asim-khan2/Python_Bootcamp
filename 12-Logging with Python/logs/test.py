from logger import logging

def add(a,b):
    logging.debug("this is the debuge message")
    return a+b

logging.debug("this is the fucnction call")
add(4,5)
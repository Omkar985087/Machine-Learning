import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger=logging.getLogger("arthemetic app")

def add(a,b):
    result=a+b
    logger.debug(f"adding {a}+{b} ={result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"subtract {a}-{b} ={result}")
    return result

def mul(a,b):
    result=a*b
    logger.debug(f"mult {a}*{b} ={result}")
    return result

add(10,15)
subtract(10,5)
mul(4,5)

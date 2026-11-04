import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Calculator")
def sumof (var1):
    sum = 0
    for number in var1:
        sum = sum + number
        logger.info(("This function is returning sum of value:{}").format(sum))
    return sum
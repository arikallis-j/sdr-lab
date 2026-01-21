from loguru import logger
from MorseCodePy import encode, decode

encoded_string: str = encode('Python is fun!', language='english')
logger.info(encoded_string)

decoded_string: str = decode('****- **--- / *---- -----', language='english', dot='*', error='#')
logger.info(decoded_string)
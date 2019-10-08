import requests
import random
from rest_framework import status
from micro_service_one.settings import MICRO_SERVICE_URL
from commons.utils import get_logger

logger = get_logger()



def string_reverser(payload):
    """
    Get response from micro-service two
    :param payload:
    :return:
    """
    url = MICRO_SERVICE_URL + '/reverse'
    response = requests.post(url, payload)
    if response.status_code == status.HTTP_201_CREATED:
        logger.info("Auth user deleted")
        return response.json().get("message")
    else:
        logger.error("Auth user not deleted")
        return False


def random_number_generator():
    random_number = random.random()
    return random_number

from locust import HttpUser
import urllib3

from logger import init_logging
from task import PetTask

urllib3.disable_warnings()

init_logging()


class HelloWorldUser(HttpUser):
    tasks = [PetTask]
    min_wait = 5000
    max_wait = 9000

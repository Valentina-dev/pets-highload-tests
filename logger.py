import logging
from http.client import HTTPConnection


def init_logging():
    HTTPConnection.debuglevel = 0
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.INFO)
    requests_log.propagate = True

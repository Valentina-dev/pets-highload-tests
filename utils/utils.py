import random
import string


class StringUtils:
    @staticmethod
    def random_string():
        random_letters = string.ascii_letters
        return "".join(random.sample(random_letters, 5))


status_lst = ["available", "sold", "pending"]
body = {
    "id": 0,
    "category": {"id": 0, "name": "string"},
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}],
    "status": "available",
}

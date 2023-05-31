import random

import requests
from locust import task, TaskSet

from config import BASE_URL
from img import files
from utils.utils import StringUtils, status_lst, body


class PetTask(TaskSet):
    pets_ids = []
    """Create pets for tests"""

    def on_start(self):
        for i in range(2):
            pet = requests.post(url=BASE_URL + "/pet", json=body)
            self.pets_ids.append(pet.json()["id"])

    @task
    def create_pet(self):
        x = self.client.post("/pet", json=body, verify=False)
        self.pets_ids.append(x.json()["id"])

    @task(5)
    def get_pet(self):
        self.client.get(f"/pet/{random.choice(self.pets_ids)}")

    @task
    def add_pets_img(self):
        with open(random.choice(files.file), "rb") as file:
            return self.client.post(
                f"/pet/{random.choice(self.pets_ids)}/uploadImage", files={"file": file}
            )

    @task
    def find_by_status(self):
        return self.client.get(f"/pet/findByStatus?status={random.choice(status_lst)}")

    @task
    def update_pet(self):
        params = {
            "name": StringUtils.random_string(),
            "status": random.choice(status_lst),
        }
        return self.client.post(f"/pet/{random.choice(self.pets_ids)}", params=params)

    @task
    def delete_pet(self):
        create_pet_for_delete = requests.post(
            url=f"{BASE_URL}/pet", json=body, verify=False
        )
        return self.client.delete(f"/pet/{create_pet_for_delete.json()['id']}")

    """Clean DB after testing"""

    def on_stop(self):
        for i in set(self.pets_ids):
            requests.delete(f"{BASE_URL}/pet/{i}")

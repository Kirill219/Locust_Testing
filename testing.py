from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = 'https://petstore.swagger.io/v2'


    @task(6)
    def add_user(self):
        self.client.post("/user", json={
            "id": 1,
            "username": "Kir",
            "firstName": "Kir",
            "lastName": "Voit",
            "email": "Voit@gmail",
            "password": "vk3333",
            "phone": "0947574548",
            "userStatus": 1
        })


    @task(3)
    def add_pet(self):
        self.client.post("/pet", json={
            "id": 1,
            "category": {
                "id": 1,
                "name": "sheppard"
            },
            "name": "Spike",
            "photoUrls": ["string"],
            "tags": [{
                "id": 1,
                "name": "none"
            }],
            "status": "available"
        })


    @task(2)
    def update_pet(self):
        self.client.put("/pet", json={
            "id": 1,
            "category": {
                "id": 1,
                "name": "sheppard"
            },
            "name": "Spike",
            "photoUrls": ["string"],
            "tags": [{
                "id": 1,
                "name": "average"
            }],
            "status": "available"
        })


    @task(1)
    def log_user(self):
        self.client.get("/user/login", json={
            "username": "Kir",
            "password": "vk3333"
        })


    @task(7)
    def add_order(self):
        self.client.post("/store/order", json={
            "id": 1,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2021-12-02T13:21:44.667Z",
            "status": "placed",
            "complete": True
        })


    @task(1)
    def get_order(self):
        self.client.get("/store/order/1")


    @task(1)
    def delete_order(self):
        self.client.delete("/store/order/1")


    @task(2)
    def update_user_ByName(self):
        self.client.put("/user/Kir", json={
            "id": 1,
            "username": "Kir",
            "firstName": "Kirill",
            "lastName": "Voit",
            "email": "Voit@gmail",
            "password": "vk3333",
            "phone": "0947574548",
            "userStatus": 1
        })


    @task(1)
    def get_user(self):
        self.client.get("/user/Kir")


    @task(1)
    def logout_user(self):
        self.client.get("/user/logout")





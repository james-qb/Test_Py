import os
import sys

from locust import HttpUser, TaskSet, task
import subprocess
import json


class UserBehavior(TaskSet):
    def on_start(self):
        payload = {
            "username": "test_user",
            "password": "123456",
        }
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.36",
        }
        self.client.post("/login", data=payload, headers=header)

    @task(1)
    def list_header(self):
        r = self.client.get("/homepage/list_header.html")
        if json.loads((r.content))["result"] != 100:
            r.failure("Got wrong response:" + r.content)

    @task(2)
    def list_goods(self):
        r = self.client.get("/homepage/list_goods.html")
        if json.loads((r.content))["result"] != 100:
            r.failure("Got wrong response:" + r.content)


class WebUserLocust(HttpUser):
    weight = 1  # The taskset class name is the value of the task_set.
    tasks = [UserBehavior]  # Wait time between the execution of tasks.
    min_wait = 5000
    max_wait = 15000  # This is another HttpLocust class.


class MobileUserLocust(HttpUser):
    weight = 3
    tasks = [UserBehavior]
    min_wait = 3000
    max_wait = 6000  #


if __name__ == '__main__':
    f_name = os.path.basename(sys.argv[0])
    subprocess.Popen("locust -f .\%s --host=http://api.g.caipiao.163.com"%f_name, shell=True)

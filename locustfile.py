from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task
    def get_root_path(self):
        self.client.get("/")
    
    @task
    def get_predictions(self):
        self.client.get("/predictions")

class MyLocust(HttpLocust):
    task_set = MyTask

    min_wait = 1000
    max_wait = 2000
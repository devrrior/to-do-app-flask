import unittest

from flask import current_app

from app import db, User, Task
from app import create_app

from config import config


class TestUserModel(unittest.TestCase):
    def setUp(self):
        config_class = config["test"]
        self.app = create_app(config_class)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.id = 1

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        self.app_context.pop()

    # def test_create_task(self):
    #     task = Task.create_task(
    #         "hola mundo", "hello everyone, hare otra prueba", 1)
    #     user = User.create_user('fernando@', "hola@gmail.com", "21@!hoafoha")
    #     self.assertTrue(task.id == self.id)

    def test_create_user(self):
        user = User.create_user('fernando@', "hola@gmail.com", "21@!hoafoha")
        self.assertTrue(user.id == self.id)

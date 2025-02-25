"""

This module contains the unit tests.
It uses Python's built-in unittest framework.
"""

import unittest
from APIs import UserAPI, HouseAPI, RoomAPI, DeviceAPI

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.APIs = UserAPI()

    def test_create_user(self):
        result = self.APIs.create_user("osama", "osama@gmail.com")
        self.assertEqual(result["status"], "User created successfully!")

    def test_get_user(self):
        result = self.APIs.get_user(1)
        self.assertEqual(result["status"], "User fetched successfully!")

    def test_update_user(self):
        result = self.APIs.update_user(1, username="osama_new")
        self.assertEqual(result["status"], "User updated successfully!")

    def test_delete_user(self):
        result = self.APIs.delete_user(1)
        self.assertEqual(result["status"], "User deleted successfully!")


class TestHouseAPI(unittest.TestCase):
    def setUp(self):
        self.APIs = HouseAPI()

    def test_create_house(self):
        result = self.APIs.create_house("233 Broadway St", owner_id=1)
        self.assertEqual(result["status"], "House created successfully!")

    def test_get_house(self):
        result = self.APIs.get_house(1)
        self.assertEqual(result["status"], "House fetched successfully!")

    def test_update_house(self):
        result = self.APIs.update_house(1, address="938 Oak St")
        self.assertEqual(result["status"], "House updated successfully!")

    def test_delete_house(self):
        result = self.APIs.delete_house(1)
        self.assertEqual(result["status"], "House deleted successfully!")


class TestRoomAPI(unittest.TestCase):
    def setUp(self):
        self.APIs = RoomAPI()

    def test_create_room(self):
        result = self.APIs.create_room(1, "Bedroom")
        self.assertEqual(result["status"], "Room created successfully!")

    def test_get_room(self):
        result = self.APIs.get_room(1)
        self.assertEqual(result["status"], "Room fetched successfully!")

    def test_update_room(self):
        result = self.APIs.update_room(1, name="Master Bedroom")
        self.assertEqual(result["status"], "Room updated successfully!")

    def test_delete_room(self):
        result = self.APIs.delete_room(1)
        self.assertEqual(result["status"], "Room deleted successfully!")


class TestDeviceAPI(unittest.TestCase):
    def setUp(self):
        self.APIs = DeviceAPI()

    def test_create_device(self):
        result = self.APIs.create_device(1, "Thermostat", status="off")
        self.assertEqual(result["message"], "Device created successfully!")

    def test_get_device(self):
        result = self.APIs.get_device(1)
        self.assertEqual(result["message"], "Device fetched successfully!")

    def test_update_device(self):
        result = self.APIs.update_device(1, device_type="Camera", status="on")
        self.assertEqual(result["message"], "Device updated successfully!")

    def test_delete_device(self):
        result = self.APIs.delete_device(1)
        self.assertEqual(result["message"], "Device deleted successfully!")


if __name__ == '__main__':
    unittest.main()

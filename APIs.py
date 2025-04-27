"""
This module provides implementations for :
- User
- House
- Room
- Device 

...APIs

Each API class here contains methods for CRUD operations.
Each method returns dummy data and a status message.
"""

class UserAPI:
    def create_user(self, username, email):
        """Create a new User."""
        return {"id": 1, "username": username, "email": email, "status": "User created successfully!"}
    
    def get_user(self, user_id):
        """Retrieve a User by ID."""
        return {"id": user_id, "username": "jane_doe", "email": "jane123@gmail.com", "status": "User fetched successfully!"}
    
    def update_user(self, user_id, username=None, email=None):
        """Update the User's details."""
        return {"id": user_id, "username": username or "jane_doe", "email": email or "jane123@example.com", "status": "User updated successfully!"}
    
    def delete_user(self, user_id):
        """Delete a User."""
        return {"id": user_id, "status": "User deleted successfully!"}


class HouseAPI:
    def create_house(self, address, owner_id):
        """Create a new house."""
        return {"id": 1, "address": address, "owner_id": owner_id, "status": "House created successfully!"}
    
    def get_house(self, house_id):
        """Retrieve a house by ID."""
        return {"id": house_id, "address": "123 Main St", "owner_id": 1, "status": "House fetched successfully!"}
    
    def update_house(self, house_id, address=None):
        """Update a house's details."""
        return {"id": house_id, "address": address or "123 Main St", "status": "House updated successfully!"}
    
    def delete_house(self, house_id):
        """Delete a house."""
        return {"id": house_id, "status": "House deleted successfully!"}


class RoomAPI:
    def create_room(self, house_id, name):
        """Create a new room in a house."""
        return {"id": 1, "house_id": house_id, "name": name, "status": "Room created successfully!"}
    
    def get_room(self, room_id):
        """Retrieve a room by ID."""
        return {"id": room_id, "house_id": 1, "name": "Living Room", "status": "Room fetched successfully!"}
    
    def update_room(self, room_id, name=None):
        """Update a room's details."""
        return {"id": room_id, "name": name or "Living Room", "status": "Room updated successfully!"}
    
    def delete_room(self, room_id):
        """Delete a room."""
        return {"id": room_id, "status": "Room deleted successfully!"}


class DeviceAPI:
    def create_device(self, room_id, device_type, status="off"):
        """Create a new device in a room."""
        return {"id": 1, "room_id": room_id, "device_type": device_type, "status": status, "message": "Device created successfully!"}
    
    def get_device(self, device_id):
        """Retrieve a device by ID."""
        return {"id": device_id, "room_id": 1, "device_type": "Light", "status": "off", "message": "Device fetched successfully!"}
    
    def update_device(self, device_id, device_type=None, status=None):
        """Update a device's details."""
        return {"id": device_id, "device_type": device_type or "Light", "status": status or "off", "message": "Device updated successfully!"}
    
    def delete_device(self, device_id):
        """Delete a device."""
        return {"id": device_id, "message": "Device deleted successfully!"}


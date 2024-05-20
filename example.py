#!/usr/bin/python3
from models import storage
from models.user import User

# Create a new user instance
new_user = User()
new_user.email = "john.doe@example.com"
new_user.password = "password123"
new_user.first_name = "John"
new_user.last_name = "Doe"

# Save the new user instance
new_user.save()

# Print the new user instance
print(new_user)

# Print all objects stored in FileStorage
print(storage.all())

# Modify the user's first name
new_user.first_name = "Jonathan"
new_user.save()

# Print the updated user instance
print(new_user)

# Save all objects to the JSON file
storage.save()

# Reload objects from file
storage.reload()

# Print all objects to verify persistence
print(storage.all())


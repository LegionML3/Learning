# Question: Add "Jake" to the phonebook with the phone number 938273443,
# and remove Jill from the phonebook.

# Code:

phonebook = {
    "John": 938477566,
    "Jack": 100202340,
    "Jill": 947662781
    }
phonebook.pop("Jill")  # Remove Jill from the phonebook
phonebook["Jake"] = 938273443  # Add Jake to the phonebook with the phone number 938273443

for item in phonebook.items():
    print(item)
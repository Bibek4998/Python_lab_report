# Write a program to demonstrate the set operation in python.
sets={"Kathmandu","Dhangadhi","Lalitpur","Bhaktapur","Morang"}
print(f"Original set: {sets}")
sets.add("Pokhara")
print(f"Adding item: {sets}")
sets.remove("Kathmandu")
print(f"Removing the item: {sets}")
districts={"Kailali","Chitwan","Kaski"}
sets.update(districts)
print(f"Updating the sets: {sets}")
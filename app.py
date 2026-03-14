import random

business = input("Enter business type: ")

ads = [
"Limited time discount!",
"Best service in the city!",
"Visit today and enjoy special offers!"
]

print("🔥 Promotion for", business)
print(random.choice(ads))

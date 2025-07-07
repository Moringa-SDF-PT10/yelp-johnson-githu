from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

Customer.create_table()
Restaurant.create_table()
Review.create_table()

#Customer property first_name and Customer property last_name.
alice = Customer("Alice", "Akinyi")
bob = Customer("Bob", "Ken")

#Customer property first_name and Customer property last_name.
print(alice.first_name)
print(alice.last_name)
alice.first_name = "Angel"
print(alice.first_name)

#Restaurant.__init__(self, name)
johnson = Restaurant("Johnson Cafe")
java = Restaurant("Java House")

#Restaurant property name
print(johnson.name)
johnson.name = "Johnson's Cafe"
print(johnson.name)

#Review.__init__(self, customer, restaurant, rating)
r1 = Review(alice, johnson, 5)
r2 = Review(alice, java, 1)
r3 = Review(bob, johnson, 2)

#Review property rating
print(r1.rating)

#Review property restaurant
print(r1.restaurant)
print(r2.restaurant)
print(r3.restaurant)

# Restaurant method reviews()
print(johnson.reviews())

# Restaurant method customers()
print(johnson.customers())

# Restaurant method reviews()
print(johnson.reviews())

#Customer method restaurants()
print(alice.restaurants())

#Customer method num_negative_reviews()
print(alice.num_negative_reviews())

#Customer method has_reviewed_restaurant(restaurant)
print(alice.has_reviewed_restaurant(johnson))

# Customer method has_reviewed_restaurant(restaurant)
print(bob.has_reviewed_restaurant(johnson))


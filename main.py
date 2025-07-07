from models.customer import Customer
from models.restaurant import Restaurant
from models.review import Review

Customer.create_table()
Restaurant.create_table()
Review.create_table()

alice = Customer("Alice", "Wanjiku")
bob = Customer("Bob", "Omondi")

mama = Restaurant("Mama Oliech")
java = Restaurant("Java House")

r1 = Review(alice, mama, 5)
r2 = Review(alice, java, 1)
r3 = Review(bob, mama, 2)

print(alice.restaurants())  # [Mama Oliech, Java House]
print(mama.customers())     # [Alice, Bob]
print(mama.average_star_rating())  # 3.5
print(Restaurant.top_two_restaurants())  # [Mama Oliech, Java House]
print(alice.has_reviewed_restaurant(mama))  # True

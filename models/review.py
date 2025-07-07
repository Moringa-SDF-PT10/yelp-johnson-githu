from database import CURSOR, CONN

class Review:
    def __init__(self, customer, restaurant, rating, id=None):
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating
        self.id = id
        self.save()

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            restaurant_id INTEGER,
            rating INTEGER,
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
        );
        """)
        CONN.commit()

    def save(self):
        if not self.id:
            CURSOR.execute(
                "INSERT INTO reviews (customer_id, restaurant_id, rating) VALUES (?, ?, ?)",
                (self.customer.id, self.restaurant.id, self._rating))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute(
                "UPDATE reviews SET customer_id = ?, restaurant_id = ? WHERE id = ?",
                (self.customer.id, self.restaurant.id, self.id))
        CONN.commit()

    @property
    def rating(self):
        return self._rating

    @property
    def customer(self):
        from models.customer import Customer
        return self._customer

    @customer.setter
    def customer(self, value):
        from models.customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise TypeError("customer must be an instance of Customer.")

    @property
    def restaurant(self):
        from models.restaurant import Restaurant
        return self._restaurant

    @restaurant.setter
    def restaurant(self, value):
        from models.restaurant import Restaurant
        if isinstance(value, Restaurant):
            self._restaurant = value
        else:
            raise TypeError("restaurant must be an instance of Restaurant.")

    @classmethod
    def find_by_customer_id(cls, cust_id):
        CURSOR.execute("SELECT * FROM reviews WHERE customer_id = ?", (cust_id,))
        from models.customer import Customer
        from models.restaurant import Restaurant
        rows = CURSOR.fetchall()
        return [
            cls(Customer.find_by_id(row[1]), Restaurant.find_by_id(row[2]), row[3], row[0])
            for row in rows
        ]

    @classmethod
    def find_by_restaurant_id(cls, rest_id):
        CURSOR.execute("SELECT * FROM reviews WHERE restaurant_id = ?", (rest_id,))
        from models.customer import Customer
        from models.restaurant import Restaurant
        rows = CURSOR.fetchall()
        return [
            cls(Customer.find_by_id(row[1]), Restaurant.find_by_id(row[2]), row[3], row[0])
            for row in rows
        ]

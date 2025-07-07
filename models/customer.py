from database import CURSOR, CONN
from models.review import Review

class Customer:
    def __init__(self, first_name, last_name, id=None):
        self._first_name = first_name
        self._last_name = last_name
        self.id = id
        self.save()

    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.first_name} {self.last_name}')"

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );
        """)
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM customers WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None

    def save(self):
        if not self.id:
            CURSOR.execute(
                "INSERT INTO customers (first_name, last_name) VALUES (?, ?)",
                (self.first_name, self.last_name))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute(
                "UPDATE customers SET first_name = ?, last_name = ? WHERE id = ?",
                (self.first_name, self.last_name, self.id))
        CONN.commit()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._first_name = value
            self.save()
        else:
            raise ValueError("First name must be a string between 1 and 25 characters.")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._last_name = value
            self.save()
        else:
            raise ValueError("Last name must be a string between 1 and 25 characters.")

    def reviews(self):
        return Review.find_by_customer_id(self.id)

    def restaurants(self):
        from models.restaurant import Restaurant
        return list({review.restaurant for review in self.reviews()})

    def num_negative_reviews(self):
        return len([r for r in self.reviews() if r.rating <= 2])

    def has_reviewed_restaurant(self, restaurant):
        return any(r.restaurant.id == restaurant.id for r in self.reviews())

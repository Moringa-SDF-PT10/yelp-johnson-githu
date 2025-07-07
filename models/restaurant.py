from database import CURSOR, CONN
from models.review import Review

class Restaurant:
    def __init__(self, name, id=None):
        self._name = name
        self.id = id
        self.save()    

    def __repr__(self):
        return f"Restaurant(id={self.id}, name='{self.name}')"

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        """)
        CONN.commit()

    def save(self):
        if not self.id:
            CURSOR.execute("INSERT INTO restaurants (name) VALUES (?)", (self.name,))
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE restaurants SET name = ? WHERE id = ?", (self.name, self.id))
        CONN.commit()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
            self.save()
        else:
            raise ValueError("Restaurant name must be a non-empty string.")

    def reviews(self):
        return Review.find_by_restaurant_id(self.id)

    def customers(self):
        from models.customer import Customer
        return list({review.customer for review in self.reviews()})

    def average_star_rating(self):
        ratings = [r.rating for r in self.reviews()]
        if ratings:
            return round(sum(ratings) / len(ratings), 1)
        return 0.0

    @classmethod
    def top_two_restaurants(cls):
        CURSOR.execute("SELECT id FROM restaurants")
        ids = [row[0] for row in CURSOR.fetchall()]
        all_restaurants = [Restaurant.find_by_id(i) for i in ids]
        rated = [(r, r.average_star_rating()) for r in all_restaurants if r.reviews()]
        sorted_rated = sorted(rated, key=lambda x: x[1], reverse=True)
        return [r for r, _ in sorted_rated[:2]] if sorted_rated else None

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM restaurants WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

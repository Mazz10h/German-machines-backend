from app.database import SessionLocal, Base, engine
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order

# Create all tables
Base.metadata.create_all(bind=engine)

# Start a session
db = SessionLocal()

# -------------------- CATEGORIES --------------------
categories = [
    Category(name="Electric"),
    Category(name="SUV"),
    Category(name="Sports"),
]

db.add_all(categories)
db.commit()

# Refresh to get IDs
for cat in categories:
    db.refresh(cat)

# -------------------- PRODUCTS --------------------
products = [
    # Existing products
    Product(
        name="Tesla Model S",
        brand="Tesla",
        price=90000,
        category_id=categories[0].id,
        image_url="https://images.unsplash.com/photo-1716558964076-1abe07448abf?w=900&auto=format&fit=crop&q=60",
    ),
    Product(
        name="Porsche Cayenne",
        brand="Porsche",
        price=35000,
        category_id=categories[0].id,
        image_url="https://images.unsplash.com/photo-1654159866298-e3c8ee93e43b?w=900&auto=format&fit=crop&q=60",
    ),
    Product(
        name="BMW X5",
        brand="BMW",
        price=60000,
        category_id=categories[1].id,
        image_url="https://images.unsplash.com/photo-1604249553999-3b422c3d1ff6?w=900&auto=format&fit=crop&q=60",
    ),
    Product(
        name="Audi Q7",
        brand="Audi",
        price=65000,
        category_id=categories[1].id,
        image_url="https://images.unsplash.com/photo-1590509278793-032529995158?w=900&auto=format&fit=crop&q=60",
    ),
    Product(
        name="BMW M3",
        brand="BMW",
        price=120000,
        category_id=categories[2].id,
        image_url="https://images.unsplash.com/photo-1616455263449-0bd3aac04029?w=900&auto=format&fit=crop&q=60",
    ),
    # -------- German cars added --------
    Product(
        name="Mercedes EQC",
        brand="Mercedes",
        price=70000,
        category_id=categories[0].id,
        image_url="https://images.unsplash.com/photo-1742702596008-5a02e0a8ad49?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bWVyY2VkZXMlMjBlcWN8ZW58MHx8MHx8fDA%3D",
    ),
    Product(
        name="Volkswagen Golf",
        brand="Volkswagen",
        price=50000,
        category_id=categories[0].id,
        image_url="https://images.unsplash.com/photo-1607853203100-69829c08b88e?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8dm9sa3N3YWdlbnxlbnwwfHwwfHx8MA%3D%3D",
    ),
    Product(
        name="Audi Q5",
        brand="Audi",
        price=55000,
        category_id=categories[1].id,
        image_url="https://images.unsplash.com/photo-1590216255831-05e9541dd22a?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8YXVkaSUyMHE1fGVufDB8fDB8fHww",
    ),
    Product(
        name="BMW X3",
        brand="BMW",
        price=58000,
        category_id=categories[1].id,
        image_url="https://images.unsplash.com/photo-1677961019377-d45643fde74f?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym13JTIweDN8ZW58MHx8MHx8fDA%3D",
    ),
    Product(
        name="Mercedes S class",
        brand="Mercedes",
        price=150000,
        category_id=categories[2].id,
        image_url="https://images.unsplash.com/photo-1629019879059-2a0345f93aea?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bWVyY2VkZXMlMjBzJTIwY2xhc3N8ZW58MHx8MHx8fDA%3D",
    ),
]

db.add_all(products)
db.commit()

# Refresh to get IDs
for prod in products:
    db.refresh(prod)

# -------------------- ORDERS (Optional) --------------------
orders = [
    Order(product_id=products[0].id, quantity=1),
    Order(product_id=products[3].id, quantity=2),
]

db.add_all(orders)
db.commit()

# Close session
db.close()

print("Database seeded successfully with categories, products, orders, and German cars!")

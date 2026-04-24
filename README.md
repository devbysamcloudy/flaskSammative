# Inventory Management System

A **Flask-based Inventory Management System** designed for small retail companies. This application allows employees to manage product inventory with full CRUD operations and real-time product data fetching from the OpenFoodFacts API.

## Features

- **Complete CRUD operations**: Create, Read, Update, and Delete inventory items
- **External API integration**: Fetch product details automatically from OpenFoodFacts by product name
- **CLI interface**: Command-line tool for easy inventory management
- **Flask Shell**: Interactive shell for direct database interaction
- **Database**: SQLite for lightweight, file-based data storage
- **Unit Testing**: pytest suite for reliability

## Project Structure

```
flaskSammative/
│
├── app.py                 # Flask application, routes, and database models
├── models.py              # Database model definitions
├── cli.py                 # CLI interface for API interaction
├── tests/
│   └── test_app.py        # Unit tests
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
```

## Setup & Installation

### Prerequisites
- Python 3.7 or higher
- Git

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/devbysamcloudy/flaskSammative
cd flaskSammative
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Flask application**
```bash
python app.py
```

The application will start at `http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/items` | Add a new inventory item |
| GET | `/items` | Get all inventory items |
| PATCH | `/items/<id>` | Update an item by ID |
| DELETE | `/items/<id>` | Delete an item by ID |
| GET | `/fetch/<product_name>` | Fetch product from OpenFoodFacts and add to inventory |

### Example Requests

**Add an item**
```bash
curl -X POST http://127.0.0.1:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Milk", "quantity": 10, "price": 1.99, "barcode": "123456"}'
```

**Get all items**
```bash
curl http://127.0.0.1:5000/items
```

**Update an item**
```bash
curl -X PATCH http://127.0.0.1:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"quantity": 20, "price": 2.49}'
```

**Delete an item**
```bash
curl -X DELETE http://127.0.0.1:5000/items/1
```

**Fetch from OpenFoodFacts**
```bash
curl http://127.0.0.1:5000/fetch/nutella
```

## Using the CLI

Make sure the Flask app is running first, then in a separate terminal:
```bash
python cli.py
```

### CLI Options:
- `1` - View all items
- `2` - Add a new item
- `3` - Delete an item by ID
- `4` - Fetch a product from OpenFoodFacts by name

Follow the interactive prompts to manage your inventory.

## Flask Shell

Use the Flask shell to interact with the database directly:
```bash
export FLASK_APP=app.py
flask shell
```

Inside the shell:
```python
from app import db, Item

# Create tables
db.create_all()

# Add an item
item = Item(name="Milk", quantity=10, price=1.99, barcode="123456")
db.session.add(item)
db.session.commit()

# Query all items
Item.query.all()

# Query one item
Item.query.get(1)

# Delete an item
item = Item.query.get(1)
db.session.delete(item)
db.session.commit()
```

## Running Tests

Execute the test suite:
```bash
pytest
```

**Note:** Ensure the Flask app is not running when executing tests to avoid port conflicts.

## Git Workflow

This project was developed using feature branches:
- `feature-crud` - CRUD operations implementation
- `feature-api` - OpenFoodFacts API integration
- `feature-cli` - Command-line interface development

All pull requests were merged before final submission.

## Important Notes

- The database file (`inventory.db`) will be automatically created inside the `instance/` folder on first run
- An active internet connection is required when fetching data from OpenFoodFacts
- Product prices and quantities can be modified via PATCH requests or the CLI
- The system uses SQLite, so no separate database server is needed

## Troubleshooting

**Issue:** Database not found
- **Solution:** The system will create `inventory.db` automatically on first run

**Issue:** API fetch failing
- **Solution:** Check your internet connection and verify the product name exists in OpenFoodFacts

**Issue:** Port 5000 already in use
- **Solution:** Change the port in `app.py` or stop the application using that port

**Issue:** CLI not connecting
- **Solution:** Make sure the Flask app is running before starting the CLI

## Author

**Samuel Nganga**
- Email: [snganga685@gmail.com](mailto:snganga685@gmail.com)
- GitHub: [devbysamcloudy/flaskSammative](https://github.com/devbysamcloudy/flaskSammative)

## License

This project is for educational purposes as part of a software development assessment.

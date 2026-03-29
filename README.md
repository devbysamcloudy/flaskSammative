# Inventory Management System

A **Flask-based Inventory Management System** designed for small retail companies. This application allows employees to manage product inventory with full CRUD operations and real-time product data fetching from the OpenFoodFacts API using barcode scanning.

## Features

- **Complete CRUD operations**: Create, Read, Update, and Delete inventory items
- **External API integration**: Fetch product details automatically from OpenFoodFacts by barcode
- **CLI interface**: Command-line tool for easy inventory management
- **Database**: SQLite for lightweight, file-based data storage
- **Unit Testing**: Comprehensive pytest suite for reliability

## Project Structure

```
inventory-system/
│
├── app.py                 # Flask application entry point
├── models.py              # Database model definitions
├── routes/
│   └── inventory.py       # CRUD operations + external API routes
├── cli.py                 # CLI interface for API interaction
├── tests/
│   └── test_app.py        # Unit tests
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore            # Git ignore rules
```

## Setup & Installation

### Prerequisites
- Python 3.7 or higher
- Git

### Installation Steps

1. **Clone the repository**
```bash
git clone <your-repo-link>
cd inventory-system
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
| GET | `/fetch/<barcode>` | Fetch product from OpenFoodFacts and add to inventory |

## Using the CLI

Run the command-line interface:
```bash
python cli.py
```

### CLI Options:
- View all items
- Add a new item
- Delete an item
- Fetch a product from OpenFoodFacts by barcode

Follow the interactive prompts to manage your inventory.

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

- The database file (`inventory.db`) will be automatically created in the project folder
- An active internet connection is required when fetching data from OpenFoodFacts
- Product prices and quantities can be modified via PATCH requests or the CLI interface
- The system uses SQLite, so no separate database server is needed

## Troubleshooting

**Issue:** Database not found
- **Solution:** The system will create `inventory.db` automatically on first run

**Issue:** API fetch failing
- **Solution:** Check your internet connection and verify the barcode exists in OpenFoodFacts

**Issue:** Port 5000 already in use
- **Solution:** Change the port in `app.py` or stop the application using that port

## Author

**Samuel Nganga**  
- Email: [snganga685@gmail.com](mailto:snganga685@gmail.com)  
- GitHub: [devbysamcloudy](https://github.com/devbysamcloudy/flaskSammative)

## License

This project is for educational purposes as part of a software development assessment.
```

### Key improvements made:

1. **Better formatting**: Cleaner markdown structure with proper headings
2. **Added prerequisites section**: Clear system requirements
3. **Improved code blocks**: Consistent formatting with language specifiers
4. **Added troubleshooting section**: Helpful common issues and solutions
5. **Better organization**: Logical flow from setup to usage to troubleshooting
6. **Clarified notes**: More detailed explanations where needed
7. **Professional tone**: Cleaner language and better readability
8. **Fixed structure**: Proper indentation and consistent styling
9. **Added license note**: Clarified project purpose
10. **Better tables**: Cleaner API endpoint documentation

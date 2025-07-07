# Yelp ORM 

This is a custom Object-Relational Mapper (ORM) implemented in Python, modeling a Yelp-style application with Restaurants, Customers, and Reviews using SQLite.

## 🏗 Models

- **Customer**: Has a first name and last name. Can write multiple reviews.
- **Restaurant**: Has a name. Can receive many reviews from different customers.
- **Review**: Connects a customer to a restaurant and stores a rating (1-5).

## ⚙ Prerequisites

Make sure you have:

- Python 3.8 or higher installed
- `pipenv` installed globally

### 📦 Install pipenv (if not already installed)

Open your terminal (Command Prompt or PowerShell) and run:

```bash
pip install pipenv


## ⚙ Setup

1. Clone this repo:
   ```bash
   git clone <your-private-repo-url>
   cd yelp-johnson-githu

2. Install dependencies using Pipenv:
   ```bash
   pipenv install

3. Run the program:
   ```bash
   pipenv run python main.py

4. After first run, a database file yelp-levy-ochieng.db will be created in your directory.

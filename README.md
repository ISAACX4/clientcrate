============================================================
                 ClientCrate - Project Overview
============================================================

ClientCrate is a Django-based web application designed to help small 
businesses manage their customer relationships, handle orders, and 
streamline day-to-day operations through a modern web dashboard.

------------------------------------------------------------
FEATURES
------------------------------------------------------------

- Customer Management: Add, update, and delete customer records.
- Order Management: Track and manage customer orders efficiently.
- Admin Dashboard: View recent activity, summaries, and key stats.
- Authentication: Secure user login and registration system.
- Tailwind CSS UI: Responsive, clean interface using Tailwind.
- Modular Templates: Organized and reusable Django template structure.

------------------------------------------------------------
TECHNOLOGIES USED
------------------------------------------------------------

- Python 3.x
- Django Web Framework
- Tailwind CSS (via CDN or npm)
- SQLite (for development)
- Git & GitHub for version control

------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------

clientcrate/
│
├── core/               -> Django app: views, models, URLs, forms
├── templates/          -> Tailwind-styled HTML templates
├── static/             -> Static files (CSS, JS, images)
├── manage.py           -> Django management script
└── requirements.txt    -> Project dependencies

------------------------------------------------------------
SETUP INSTRUCTIONS
------------------------------------------------------------

1. Clone the repository:
   git clone https://github.com/ISAACX4/clientcrate.git
   cd clientcrate

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate      (on Windows)

3. Install dependencies:
   pip install -r requirements.txt

4. Apply database migrations:
   python manage.py migrate

5. Run the development server:
   python manage.py runserver

6. Open your browser and go to:
   http://127.0.0.1:8000/

------------------------------------------------------------
NEXT FEATURES TO ADD
------------------------------------------------------------

- Customer search & filter
- Email/SMS notifications
- Order status tracking
- Export customer and order data
- Analytics dashboard

------------------------------------------------------------
CONTRIBUTING
------------------------------------------------------------

You're welcome to contribute! Please open an issue or fork the project 
and submit a pull request with a clear explanation of your changes.



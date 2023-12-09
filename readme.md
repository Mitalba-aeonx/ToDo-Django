## ToDo List

## Prerequisites

- Python 3.11 installed on your system

## Getting Started

- Follow these steps to set up and run the project locally.


1. Create a Virtual Environment
- **On Windows**
- python -m venv venv

- **On macOS/Linux**
- python3 -m venv venv


2. Activate the Virtual Environment
-  **On Windows**
- venv\Scripts\activate

-  **On macOS/Linux**
- source venv/bin/activate


3. Install Dependencies
- pip install -r requirements.txt


4. Run Migrations
- python manage.py migrate


5. Create a Superuser (Optional)
- python manage.py createsuperuser


6. Run the Development Server
- python manage.py runserver
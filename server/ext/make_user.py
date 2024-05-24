import os
import sys
import django
from django.contrib.auth.hashers import make_password
from uuid import uuid4


project_path = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

password = "qwerty"
hashed_password = make_password(password)
verification_code = str(uuid4())

print("password: ", hashed_password)
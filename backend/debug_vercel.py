
import sys
import os
from pathlib import Path

# Simulate Vercel environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Simulate what we did in wsgi.py
file_path = Path(__file__).resolve()
backend_dir = file_path.parent
sys.path.append(str(backend_dir))

print(f"Current Working Directory: {os.getcwd()}")
print(f"Script Location: {file_path}")
print(f"Backend Directory added to sys.path: {backend_dir}")

try:
    print("Attempting to import config.settings...")
    import config.settings
    print("SUCCESS: config.settings imported.")
    print(f"DOMAIN_PATH calculated in settings: {config.settings.DOMAIN_PATH}")
    
    print("Attempting to import domain_layer...")
    import domain_layer
    print("SUCCESS: domain_layer imported.")
    
    print("Attempting to import application from config.wsgi...")
    from config.wsgi import application
    print("SUCCESS: WSGI application loaded.")

except Exception as e:
    print("\nFAILED with error:")
    print(e)
    import traceback
    traceback.print_exc()

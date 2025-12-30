"""
WSGI config for config project.
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application  # ✅ ESTE ES EL CAMBIO CLAVE

# Add backend directory to sys.path
file_path = Path(__file__).resolve()
backend_dir = file_path.parent.parent
sys.path.append(str(backend_dir))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()

app = application



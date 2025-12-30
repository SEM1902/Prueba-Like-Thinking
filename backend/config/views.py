
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound

def serve_react(request):
    try:
        # Use REACT_APP_DIR defined in settings or fallback
        react_dir = getattr(settings, 'REACT_APP_DIR', settings.BASE_DIR / 'react_build')
        file_path = os.path.join(react_dir, 'index.html')
        
        with open(file_path, 'r') as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        return HttpResponseNotFound(f"React Build not found at: {file_path}. Did you git add backend/react_build?")

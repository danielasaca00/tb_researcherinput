
import os
import sys

# Añade la ruta a tu proyecto
project_home = '/home/tu_usuario/tb_researcherinput'
if project_home not in sys.path:
    sys.path.append(project_home)

# Indica tu archivo settings.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'tb_researcherinput.settings'

# Carga la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

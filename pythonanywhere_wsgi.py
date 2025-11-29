"""
WSGI configuration for PythonAnywhere deployment.

This file exposes the WSGI callable as a module-level variable named 'application'.
For more information on this file, see:
https://help.pythonanywhere.com/pages/Flask/
"""

import os
import sys

# Import and configure the application
from dash_lite.app import create_app

# Add your project directory to the sys.path
project_home = "/home/YOUR_USERNAME/dash-lite"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Add the src directory to sys.path
src_path = os.path.join(project_home, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Set environment variables
os.environ["DASH_LITE_PORT"] = "8000"
os.environ["DASH_LITE_DEBUG"] = "false"

application = create_app().server

# For debugging (remove in production)
# print(f"Python path: {sys.path}", file=sys.stderr)
# print(f"Application: {application}", file=sys.stderr)

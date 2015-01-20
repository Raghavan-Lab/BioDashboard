import os


# List of Tools available to the user.  Added tools immediately show up in main menu
TOOLS = [{'title': 'Find Orthologs', 'link': 'find_orthologs'},
         {'title': 'Another Tool', 'link': '/'}]

# Set Base directory to wherever the script is
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
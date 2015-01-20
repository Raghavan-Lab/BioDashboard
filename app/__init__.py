from flask import Flask, request, url_for

# General Configuration
app = Flask(__name__)

from app.views import contents, find_orthologs_view
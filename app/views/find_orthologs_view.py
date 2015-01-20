import os
from flask import render_template, flash, redirect, url_for
from app import app
from app.config import BASE_DIR, UPLOAD_FOLDER

print("-----> BASE DIR: {}".format(BASE_DIR))

#Configure Flask process
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB Limit

@app.route('/find_orthologs', methods=['GET', 'POST'])
def find_orthologs_view():
    return render_template('find_orthologs.html')

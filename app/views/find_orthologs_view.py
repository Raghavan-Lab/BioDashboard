import os
from flask import render_template, flash, request
from subprocess import check_output
from uuid import uuid1
from app import app
from app.config import UPLOAD_FOLDER, SECRET_KEY
from werkzeug.utils import secure_filename


app.secret_key = SECRET_KEY
ALLOWED_EXTENSIONS = ['faa', 'txt', 'fasta', 'fa']
print("Uploads folder: {}".format(UPLOAD_FOLDER))


#Configure Flask process
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB Limit


# A utility function. We only want some types of files uploaded.  This returns a boolean if the file extensions matches.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# A utility function to save a file object that has been put into our web form.
def save_file(request_file_obj, batch_id):
    if request_file_obj and allowed_file(request_file_obj.filename):
        ## Gotta make sure it doesn't have a name like "../../../etc/passwd"
        filename = secure_filename(request_file_obj.filename)
        ## makes the full path using our batch id
        full_file_path = os.path.join(app.config['UPLOAD_FOLDER'], batch_id, filename)
        ## Save our file
        request_file_obj.save(full_file_path)
        #Return the path so we know where
        return full_file_path


@app.route('/find_orthologs', methods=['GET', 'POST'])
def find_orthologs_view():
    # If we have already filled in our form below we are going to POST those files into our web server.
    if request.method == 'POST':
        # Generate a new Batch ID for this upload so we don't overwrite anything.
        batch_id = str(uuid1())

        # Make our batch folder.
        os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], batch_id))

        # Pull the files from our Web Form
        file_a = request.files['file1']
        file_b = request.files['file2']

        # Call the utility function from earlier on those files.
        path_a = save_file(file_a, batch_id)
        path_b = save_file(file_b, batch_id)
        print("PathA is: {}, PathB is: {}".format(path_a, path_b))

        # Check if we can use both files, if not then redirect to here to try again
        if path_a is None or path_b is None:
            print("File Check Failed.  Paths are missing")
            flash("Please check the file type and try again.  Supported extensions: {}".format(ALLOWED_EXTENSIONS))
        else:
            #-------------  Run Ortholog Script  -------------------

            # Calling a shell command on the files that we uploaded just to show you we can.  :)
            return '''Our Batch # was <b>{}</b> <br> Concatenated files:<br> {}'''.format(batch_id,
                                                                                          check_output(["cat",
                                                                                                        path_a,
                                                                                                        path_b]))
    return render_template('find_orthologs.html')
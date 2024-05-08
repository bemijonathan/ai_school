from flask import Flask, request
from pathlib import Path
import os

#receive pdf file and save it in user folder
def saveThePdf(request):
    # check if the post request has the file part
    print(request.files)
    if 'test' not in request.files:
        return 'No file part'
    
    file = request.files['test']
    if file.filename == '':
        return 'No selected file'
        
    filename =file.filename;
    # Save the file to the UPLOAD_FOLDER
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = '/upload/'
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    #save file
    currentdirectory = os.getcwd() +'/uploads'
    file_path = os.path.join(currentdirectory,filename)
    file.save(file_path) 
    return file_path
    
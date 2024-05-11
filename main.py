from flask import Flask, request

import pdf_hanlder  #handlers related to pdf


app = Flask("ai_school")

@app.route("/uploadpdf", methods = ['POST', 'DELETE'])
def upload_pdf():
    if request.method == 'POST':   
        result = pdf_hanlder.saveThePdf(request)
    #error checking
    
    return result


@app.route("/")
def hello_world():
    return "<p>Welcome to AI - SCHOOL</p>"


from flask import Flask, request

import pdf_hanlder  #handlers related to pdf


import powerpoint
import ai


def power_point_logic():
    powerpoints = powerpoint.PowerPoint("uploads/pdf.pdf")
    document_pages = powerpoints.disintegrate_powerpoint()
    images = powerpoints.convert_to_images(document_pages)
    print(images)
    ai.explain_power_point_image(images)

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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

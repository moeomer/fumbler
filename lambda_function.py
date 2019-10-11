import json
import os
import pdfkit
import base64

def generate_pdf(event, context):
    input = '/tmp/input.html'
    output = '/tmp/output.pdf'
    with open(input, "wb") as f:
        f.write(base64.b64decode(event['body']))

    config = pdfkit.configuration(wkhtmltopdf="binary/wkhtmltopdf")

    pdfkit.from_file(input, output, configuration=config, toc={
        'xsl-style-sheet': 'toc.xsl'
    })

    with open(output, "rb") as f:
        r = base64.b64encode(f.read())
        encoded_pdf = r.decode("utf-8")

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
            "Content-Type": "application/pdf"
        },
        "statusCode": 200,
        "body": encoded_pdf,
        'isBase64Encoded': True
    }

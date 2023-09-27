#!/usr/bin/env python

###

import json

from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin

##

##

app = Flask(__name__)

###

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

###

@app.route('/', methods=["GET"])
@cross_origin()
def handleRootRequestGET():

	statusMessage = "hello from / *GET*"

	print(statusMessage)

	return statusMessage

@app.route('/health-check', methods=["GET"])
@cross_origin()
def handleHealthCheckGET():

	statusMessage = "standard text API Is Up! [flask]"

	print(statusMessage)

	return statusMessage

###

@app.route('/rewrite-text-rytr', methods=["POST"])
@cross_origin()
def handlePOSTRewriteTextWithRytr():

	print("enter :: handlePOSTRewriteTextWithRytr()")

	contentToRewrite = request.get_json()

	leftSideText = contentToRewrite["originalContent"]

	leftSideText = leftSideText.replace("\n", "")

	print("param - content: ", leftSideText)

	print("sending text off to be rewritten")

	return rewrittenTextFromRytr

###

@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"

    return response

def main():

	print()
	print("###")

	print("### This is the Text Rewrite Dashboard API")
	
	print("###")
	print()

if __name__ == "__main__":
    
	#main()
    
	app.run(host='0.0.0.0', port=8080, debug=True)

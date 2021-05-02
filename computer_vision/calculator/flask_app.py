from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET','POST']) # To render Home Page
def home_page():
    return 'Home Page'

@app.route('/via_postman', methods=['POST']) # For calling the API
def calculator():
    if (request.method=='POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if (operation=='add'):
            r = num1 + num2
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)

        if (operation=='subtract'):
            r = num1 - num2
            result = "The difference of " + str(num1) + " and " + str(num2) + " is " + str(r)

        if (operation=='multiply'):
            r = num1 * num2
            result = "The product of " + str(num1) + " and " + str(num2) + " is " + str(r)

        if (operation == 'divide'):
            r = num1 / num2
            result = "The quotient of " + str(num1) + " is divided by " + str(num2) + " is " + str(r)

        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask


# Get request
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

languages = [{'name':'nodejs'},{'name':'Python'},{'name':'Ruby'}]


# Get request with a route to get all records:
@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages':languages})

# To GET only one record
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

# To use POST
@app.route('/lang', methods=['POST'])
def addOne():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages' : languages})

# PUT request
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language' : langs[0]})

# DELETE request
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages' : languages})


if __name__ == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode

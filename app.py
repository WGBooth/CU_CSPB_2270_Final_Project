from flask import Flask, render_template, request, jsonify
import scripts.radix_trie as rt

app = Flask(__name__)

# Crates the radix trie data structure
names_trie = rt.generate_trie()

# Creates the index file from html
@app.route('/')
def index():
    return render_template('index.html')

# Creates the autocomplete function to create a list of possible names 
# auto-completing a user's query
@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    html = ''
    # Gets the user's query
    data = request.get_json()
    # Searches the trie for possible names
    possible_name = data.get('possible_name')
    # Returns the possible names in a list from radix_trie.py
    results = names_trie.search(possible_name)
    # Creates the list of possible names in the frontend
    for result in results:
        html += '<li id="search_results-item">' + result.upper() + '</li>'
    return html

if __name__ == '__main__':
    app.run(debug=True)
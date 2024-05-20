from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to FrontEnd</h1>
        <form action="/submit" method="post">
            <label for="university">University:</label><br>
            <input type="text" id="university" name="university"><br>
            <label for="email">Email:</label><br>
            <select id="email" name="email">
                <option value="email1@example.com">email1@example.com</option>
                <option value="email2@example.com">email2@example.com</option>
                <option value="email3@example.com">email3@example.com</option>
                <option value="email4@example.com">email4@example.com</option>
                <option value="email5@example.com">email5@example.com</option>
            </select><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    university = request.form['university']
    email = request.form['email']
    return f'<h1>University: {university}</h1><h1>Email: {email}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

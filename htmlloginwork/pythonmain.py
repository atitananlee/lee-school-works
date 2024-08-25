from flask import Flask, render_template as rt, request, redirect, url_for

app = Flask(__name__)

valid_members = ['leelee', 'samson', 'hungty', 'leewahlahwee', 'yunkinsrm']
validspass = ['leelostick', 'samsy', 'hungtyy', 'lahwee12', 'yunkinkung']

@app.route('/')
def home():
    return redirect(url_for('askin'))

@app.route('/form', methods=['GET', 'POST'])
def askin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in valid_members:
            index = valid_members.index(username)
            if password == validspass[index]:
                return redirect(url_for('welcome', username=username))
            else:
                text = 'Incorrect password.'
                return rt('login.html', Text=text)
        else:
            text = 'You are not in the LEE Family.'
            return rt('login.html', Text=text)
    return rt('login.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return rt('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)









    
    
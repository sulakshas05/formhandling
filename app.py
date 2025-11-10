from flask import Flask,render_template,request,session,redirect,url_for
app=Flask(__name__)
users=[]
@app.route('/')
def home():
    return redirect(url_for('login'))
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        for user in users:
            if(user['email']==email):
                return "User already exists!"
        users.append({'email':email,
                     'password':password})
        return redirect(url_for('login'))
    return render_template('signup.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        for user in users:
            if(user['email']==email and user['password']==password):
                return render_template('home.html',email=email)
    return render_template('login.html')
if __name__=='__main__':
    app.run(debug=True)
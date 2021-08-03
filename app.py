from flask import Flask, render_template,request
import joblib

#initialise the app
app = Flask(__name__)
model = joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contacts')
def contact():
    return render_template('index.html')

@app.route('/submit',methods =["POST"]) #data entered in UI will be bought here via POST method
def form_data():
    print('reached here')
    # fname = request.form.get('fname') #getting the data entered in UI and storing in variables
    # lname = request.form.get('lname')
    # phonenumber = request.form.get('phone')
    # email = request.form.get('email')
    # print(fname,lname,phonenumber,email)

    preg = request.form.get('preg') #getting the data entered in UI and storing in variables
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    mass = request.form.get('mass') #getting the data entered in UI and storing in variables
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    test = request.form.get('test')
    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    print(output)

    if output[0] == 1:
        out = 'diabetic'
    else:
        out = 'not diabetic'

    return render_template('index.html',data = f'Person is {out}')



if __name__=='__main__':
    app.run(debug=True)
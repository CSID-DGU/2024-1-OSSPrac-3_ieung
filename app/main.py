from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
       result=dict()
       result['Name']=request.form.get('name')
       result['Student Number'] = request.form.get('StudentNumber')
       result['University'] = request.form.get('University')
       result['Major'] = request.form.get('major')
       result['Gender'] = request.form['gender']
       result['Email'] = request.form.get('Email')+'@'+request.form.get('Email_sel')
       result['Programming_lang'] = request.form.getlist('prog_lang')
       
       return render_template('result.html',result=result)  
       
if __name__ =='__main__':
     app.run(host="0.0.0.0", debug=True, port=80)

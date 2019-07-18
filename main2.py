from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calci.html')


@app.route('/add',methods=['GET','POST'])
def index3():
    v1=int(request.form.get('val1'))
    v2=int(request.form.get('val2'))
    s=v1.__add__(v2)

    return "Sum is "+str(s)

@app.route('/sub',methods=['GET','POST'])
def index4():
    v1=request.form.get('val1',type=int)
    v2=request.form.get('val2',type=int)
    s=v1-v2

    return "Difference is "+str(s)

@app.route('/mul',methods=['GET','POST'])
def index5():
    v1=request.form.get('val1',type=int)
    v2=request.form.get('val2',type=int)
    s=v1*v2

    return "Product is "+str(s)

@app.route('/div',methods=['GET','POST'])
def index6():
    v1=request.form.get('val1',type=int)
    v2=request.form.get('val2',type=int)
    s=v1/v2

    return "Quotient is "+str(s)

if __name__=="__main__":
    app.run()
from flask import Flask,render_template,request,flash
'''


render_template:   返回一个模板页面


flash:  给模板发送消息   模板中需要遍历   需要对内容加密   需要设置secret_key ，做一个加密消息的混淆


'''

app = Flask(__name__)

app.secret_key = 'ite'

#如何返回一个网页
#如何给模板填充数据
@app.route('/',methods=['GET','POST'])
def index():
    #request  :  是请求对象

    #判断请求方式
    if request.method =='POST':

        #获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([username,password,password2]):
            print('参数不完整')
            flash('参数不完整')
        elif password != password2:
            print('密码不一致')
            flash('密码不正确')
        else:
            return 'success'




    #通常，模板中使用的变量名要和传递的数据的变量名保持一致
    return render_template('index.html',


                           )

if __name__ == '__main__':
    app.run(debug=True)



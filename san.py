from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo
'''


render_template:   返回一个模板页面


flash:  给模板发送消息   模板中需要遍历   需要对内容加密   需要设置secret_key ，做一个加密消息的混淆


试用wtf实现表单
    自定义一个表单类


'''
# print(__name__)
app = Flask(__name__)

app.secret_key = 'ite'
#
#
#
# class longin(FlaskForm):
#     name = StringField(u'名字',validators=[DataRequired()])
#     pwd = PasswordField(u'密码')
#     pwd2 = PasswordField(u'请确认密码',validators=[DataRequired(),EqualTo('pwd')])
#     sub = SubmitField(u'提交')



# @app.route('/from',methods=['POST','GET'])
# def long():
#     form_list = longin()
#     if request.method == 'POST':
#         username = request.form.get('name')
#         password = request.form.get('pwd')
#         password2 = request.form.get('pwd2')
#         if  form_list.validate_on_submit():
#             print(username,password)
#             return 'seccess'
#         else:
#             flash('参数错误')
#
#     return render_template('index1.html',form=form_list)
#
#


# 如何返回一个网页
# 如何给模板填充数据



@app.route('/',methods=['GET','POST'])
def index():
    #request  :  是请求对象

    #判断请求方式
    if request.method =='POST':

        #获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)

        if  username=='' and password=='':
            flash('参数不完整')
        else:
            return 'success'

    #通常，模板中使用的变量名要和传递的数据的变量名保持一致
    return render_template('index1.html', )



@app.route('/i',methods=['GET','POST'])
def i():
    return '123'

@app.route('/s',methods=['GET','POST'])
def s():
    return '456'

@app.route('/e',methods=['GET','POST'])
def e():
    return '789'

if __name__ == '__main__':
    app.run(debug=True)








from flask import Flask,render_template

app = Flask(__name__)

#如何返回一个网页
#如何给模板填充数据
@app.route('/')
def index():

    #比如 需要传入网址
    url_str= 'www.baidu.com'

    my_list = [1,3,5,7,9,10]

    #通常，模板中使用的变量名要和传递的数据的变量名保持一致
    return render_template('index.html',
                           url_str=url_str,
                           my_list=my_list,

                           )

if __name__ == '__main__':
    app.run(debug=True)



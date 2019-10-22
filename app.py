#导入Flask扩展
from flask import Flask,render_template

#创建Flask应用程序实例
#需要传入__name__，作用是为了确定资源所在的路径
app = Flask(__name__)

#定义路由以及视图函数
#Flask总定义路由是通过装饰器实现的
#路由默认只支持get 如果需要增加   需要自行指定   列表形式
@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'Hello World!'

#<>定义路由的参数，<>内需要起一个名字
    #有的时候，需要对路由做访问优化 参数只能是int类型的
    #@app.route('/orders/<int:order_id>')
@app.route('/orders/<order_id>')
def get_order_id(order_id):
    #需要在试图函数（）内填入参数名，那么后面的代码才能去使用
    return 'order_id %s'%order_id

if __name__ == '__main__':
    #启动程序
    #执行了之后  就会将Flask程序运行在一个简易的服务器上（用于测试）
    app.run()












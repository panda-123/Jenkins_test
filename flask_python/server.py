#ecoding=utf-8
# author:herui
# time:2021/4/12 18:57
# function:

from flask import Flask
from flask import request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []

class TestCaseServer(Resource):
    def get(self):
        # print(request.args["a"])
        if "id" in request.args:
            for i in app.config["testcase"]:
                if i["id"] == request.args["id"]:
                    return i
        else:
            return app.config["testcase"]
        # return "Hello!!!"

    def post(self):
        """
        作用：存案例
        1、每条case需要有： ID、Name、description, steps
        :return:
        """
        if "id" not in request.json:
            return {"error":"nedd ID","errcode":"404"}
        app.config["testcase"].append(request.json)
        return {"status":"OK","errCode":"0"}

api.add_resource(TestCaseServer, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)

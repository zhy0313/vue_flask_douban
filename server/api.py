from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Todos(Resource):
    def get(self):
        return tasks

api.add_resource(HelloWorld, '/')
api.add_resource(Todos, '/todos')

if __name__ == '__main__':
    app.run(debug=True)
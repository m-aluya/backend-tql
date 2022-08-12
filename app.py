from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from datetime import date, datetime
import dateutil.parser
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
api = Api(app)

dob = reqparse.RequestParser()
dob.add_argument('dob', type=str, required=True, help='Date of Birth is required')
def limiter():
    _limiter = Limiter(
        app,
        key_func=get_remote_address
    )
    return _limiter

class DateOfBirth(Resource):
    decorators = [limiter().limit("3/second")]
    def get(self):
        rdob = reqparse.request.args.get('dob')
        format = '%Y-%m-%d'
        fd = dateutil.parser.parse(rdob)
        fd = fd.strftime(format)

        dob = datetime.strptime(fd, format)
        today = date.today()
        age = today.year - dob.year - \
            ((today.month, today.day) < (dob.month, dob.day))
        return {'age': age}


api.add_resource(DateOfBirth, '/howold')





if __name__ == "__main__":
    app.run(debug=True)


from flask_frozen import Freezer
from grupy_intercon2016 import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

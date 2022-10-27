from app import app
from views import SumView, CountView
from urls import add_urls


if __name__ == '__main__':

    add_urls(app, SumView, CountView)
    app.run()

from app import app
from views import SumView
from urls import add_urls


if __name__ == '__main__':

    add_urls(app, SumView)
    app.run()

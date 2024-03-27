import os

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Default handler")


def make_app():
    public_path = os.path.join(os.path.dirname(__file__), "public")
    return tornado.web.Application(
        [
            ("/post", MyPostHandler),
            (
                r"/(.*)",
                tornado.web.StaticFileHandler,
                {
                    "path": public_path,
                    "default_filename": "index.html",
                },
            ),
            (r"/", MainHandler),
        ]
    )


class MyPostHandler(tornado.web.RequestHandler):
    def post(self):
        # Retrieve data from the POST request
        data = self.get_argument("data", default=None)

        if data is not None:
            self.write(f"Received POST request with data: {data}")
        else:
            self.write("No data provided in the POST request")


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

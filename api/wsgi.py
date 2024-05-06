from app import create_app
from flask_debugtoolbar import DebugToolbarExtension


toolbar = DebugToolbarExtension()
app = create_app()
app.config["SECRET_KEY"] = "1111"
toolbar.init_app(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "1111"

    # extensions
    from utils import logger
    from werkzeug.middleware.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app)

    # blueprints
    from views import reports

    app.register_blueprint(reports, url_prefix="/reports")

    # redirect to reports
    @app.route("/")
    def index():
        return redirect(url_for("reports.get_reports"))

    return app

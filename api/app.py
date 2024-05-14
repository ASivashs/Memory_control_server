from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)

    # extensions
    from utils import logger

    # blueprints
    from views import reports

    app.register_blueprint(reports, url_prefix="/reports")

    # redirect to reports
    @app.route("/")
    def index():
        return redirect(url_for("reports.get_reports"))

    return app

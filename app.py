from flask import Flask
from app.api.v1.endpoints import api_v1


app = Flask(__name__, 
            template_folder='app/templates', 
            static_folder='app/static')

app.register_blueprint(api_v1, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

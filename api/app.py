from flask import Flask, request, Response
from database.db import initialize_db
from ressources.routes import initialize_routes
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True


app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://dbuser:dbpassword@cluster0-ozesa.mongodb.net/scraper_db?retryWrites=true&w=majority'
    }

CORS(app)

initialize_db(app)
initialize_routes(app)

app.run()
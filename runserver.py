from repo import create_app
from settings import config

app = create_app(config, enable_frontend=True)
app.run(debug=True)

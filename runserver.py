from repo import create_app
from settings import DevConfig

app = create_app(DevConfig, enable_frontend=True)
app.run(debug=True)

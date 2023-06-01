from .bootstrap import app
from .cfg import config

app.run(
    host="0.0.0.0",
    port=config.APP_RUNNING_PORT,
    workers=1,
    debug=True,
    access_log=False,
    auto_reload=True
)

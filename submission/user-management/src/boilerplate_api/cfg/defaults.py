from fii.setup import env

APPLICATION_NAME = env("APPLICATION_NAME", "boilerplate-app")
DB_DSN = None
EXPOSE_SWAGGER_DOCS = False

BOILERPLATE_API_DOMAIN = None
BOILERPLATE_API_ENDPOINT = None

APP_RUNNING_PORT = None
BOILERPLATE_SCHEMA = None


# Swagger
OPENAPI_EXPOSE_SWAGGER_DOCS = True
OPENAPI_URL_PREFIX = "gotecq.user-management"
OPENAPI_FILE_META = "tmpl/openapi.yml"
OPENAPI_TITLE = "User Management docs"
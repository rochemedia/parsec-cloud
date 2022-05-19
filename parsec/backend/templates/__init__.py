# Parsec Cloud (https://parsec.cloud) Copyright (c) BSLv1.1 (eventually AGPLv3) 2016-2021 Scille SAS

from jinja2 import Environment, BaseLoader, TemplateNotFound, StrictUndefined
import importlib.resources


class PackageLoader(BaseLoader):
    def __init__(self, path):
        self.path = path

    def get_source(self, environment, template):
        from parsec.backend import templates  # Self import \o/

        try:
            source = importlib.resources.files(templates).joinpath(template).read_text()
        except FileNotFoundError as exc:
            raise TemplateNotFound(template) from exc
        return source, self.path, lambda: True


# Env config is also needed to configure the ASGI app
JINJA_ENV_CONFIG = {
    "loader": PackageLoader("parsec.backend.http.templates"),
    "undefined": StrictUndefined,
}
JINJA_ENV = Environment(**JINJA_ENV_CONFIG)  # type: ignore


def get_template(name):
    return JINJA_ENV.get_template(name)

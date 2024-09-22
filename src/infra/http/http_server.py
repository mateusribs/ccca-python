from abc import ABCMeta, abstractmethod

from flask import Flask, jsonify, request


class HttpServer(metaclass=ABCMeta):
    @abstractmethod
    def register(self, method: str, url: str, callback: callable) -> None:
        raise NotImplementedError

    @abstractmethod
    def listen(self, host: str, port: int) -> None:
        raise NotImplementedError


class FlaskAdapter(HttpServer):
    def __init__(self) -> None:
        self.app = Flask(__name__)

    def register(self, method: str, url: str, callback: callable) -> None:
        def endpoint(**path_params):
            try:
                params = request.view_args
                body = request.get_json(silent=True)
                output = callback(params, body)
                return jsonify(output)
            except Exception as e:
                return jsonify({'message': str(e)}), 422

        endpoint_name = f"{method.lower()}_{url.replace('/', '_')}"

        self.app.route(url, methods=[method.upper()], endpoint=endpoint_name)(endpoint)

    def listen(self, host: str, port: int) -> None:
        self.app.run(host=host, port=port)

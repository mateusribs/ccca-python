class Mediator:
    def __init__(self):
        self.handlers = []

    def register(self, event: str, callback: callable) -> None:
        self.handlers.append({'event': event, 'callback': callback})

    def notify(self, event: str, data: any) -> None:
        for handler in self.handlers:
            if handler['event'] == event:
                handler['callback'](data)

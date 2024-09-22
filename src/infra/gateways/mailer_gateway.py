from abc import ABCMeta, abstractmethod


class MailerGateway(metaclass=ABCMeta):
    @abstractmethod
    def send(self, recipient: str, subject: str, message: str) -> None:
        raise NotImplementedError()


class MailerGatewayMemory(MailerGateway):
    def send(self, recipient: str, subject: str, message: str) -> None:
        return f'{recipient} {subject} {message}'

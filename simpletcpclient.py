from twisted.internet import reactor, protocol
import sys


class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result
    """
    def connectionMade(self):
        print("connection made")
        sys.stdout.flush()
        self.transport.write("Hello, world!".encode('utf-8'))

    def dataReceived(self, data):
        """As soon as any data is received, write it back
        """
        print("Server said:", data)
        sys.stdout.flush()
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print("Connection lost.")


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()


if  __name__ == '__main__':
    main()

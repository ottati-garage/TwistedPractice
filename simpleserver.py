from twisted.internet import reactor, protocol
import sys
import time


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        """"
        As soon as any data is received, write it back
        """
        print("recieved data")
        sys.stdout.flush()
        time.sleep(3)
        self.transport.write(data)


def main():
    """This runs the protocol on port 8000
    """
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000, factory)
    reactor.run()
    print("hi")


if __name__ == '__main__':
    main()

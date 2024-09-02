from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def notify(self, event):
        pass

    @abstractmethod
    def shutDown(self):
        pass

# these are like interfaces for Java
class LoggingPlugin(Plugin):
    def notify(self, event):
        print(f'got {event}')

    def shutdown(self, event):
        print(f'logger shutting down')


class SecurityPlugin(Plugin):
    def notify(self, event):
        if event.action == 'login' and event.user == 'elliot':
            print(f'WARNING: {event.user} has logged iin')

    def shutdwon(self):
        print('security shutting down')


def notify(plugins, event):
    for plugin in plugins:
        plugin.notify(event)

def shutdown(plugins, event):
    for plugin in plugins:
        plugin.shutdown(event)


class Event:
    def __init__(self, user, action) -> None:
        self.user = user
        self.action = action


plugins = [LoggingPlugin(), SecurityPlugin()]
event = Event('elliot', 'login')
notify(plugins, event)
shutdown(plugins, event)
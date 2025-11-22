from abc import ABC, abstractmethod

class BrowserManager(ABC):
    @abstractmethod
    def start(self):
        print("Browser Manager started.")

    def stop(self):
        print("Browser Manager stopped.")

class ChromeBrowser(BrowserManager):
    def start(self):
        print("Browser Manager started for Chrome.")

tc = ChromeBrowser()
tc.start()
tc.stop()
import signal
import gi
import subprocess
from gi.repository import GLib

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

__version__ = '0.0.1'


class screen:
    def __init__(self):
        APPINDICATOR_ID = 'screen'
        self.indicator = AppIndicator.Indicator.new("screen-indicator", "screen-indicator",
                                                    AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)

        self.indicator.set_menu(self.build_menu())
        self.indicator.set_icon_full("media-playback-start", "")

    def build_menu(self):
        menu = Gtk.Menu()
        startm = Gtk.MenuItem.new_with_label("Start")
        startm.connect('activate', self.start)
        menu.append(startm)

        stopm = Gtk.MenuItem.new_with_label("Stop")
        stopm.connect('activate',  self.stop)
        menu.append(stopm)

        item_quit = Gtk.MenuItem.new_with_label("Quit")
        item_quit.connect('activate', quit)
        menu.append(item_quit)

        menu.show_all()

        return menu

    def quit(self, source):
        Gtk.main_quit()

    def start(self, source):
        self.indicator.set_icon_full("media-playback-pause", "")
        subprocess.Popen('./script.sh')
        print("sa")

    def stop(self, source):
        self.indicator.set_icon_full("media-playback-start", "")
        subprocess.Popen(['killall', 'ffmpeg'])
        print("Gidiyom ben ya!")

def main():
    ob = screen()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()


if __name__ == '__main__':
    main()

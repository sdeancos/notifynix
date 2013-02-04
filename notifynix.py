import dbus

class notification(object):

    def __init__ (self, appname):
        self.appname = appname

        self.actions = []
        self.hints = {}
        self.expire = -1

        bus = dbus.SessionBus()
        obj = 'org.freedesktop.Notifications'
        n_obj = bus.get_object(obj, '/org/freedesktop/Notifications')
        self.n_inter = dbus.Interface(n_obj, obj)

    def configure(self, actions = [], hints = {}, expire = -1):
        self.actions = actions
        self.hints = hints
        self.expire = expire

    def notify(self, summary, body, icon):
        notify_id = self.n_inter.Notify(self.appname, 0, icon,
                                        summary, body,
                                        self.actions, self.hints,
                                        self.expire)
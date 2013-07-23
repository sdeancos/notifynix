#!/usr/bin/env python

from notifynix import notification

notification_object = notification('notif.py')
notification_object.notify('Titulo', 'Mensaje', 'gtk-ok')

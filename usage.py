#!/usr/bin/env python

from notifynix import notification

notifiaction_object = notification('notif.py')
notifiaction_object.notify('Titulo', 'Mensaje', 'gtk-ok')
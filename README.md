notifynix.py
============

A very simple wrapper of dbus org.freedesktop.Notifications in python

Usage
-----

	from notifynix import notification

	notification_object = notification('notifynix.py')
	notification_object.notify('Titulo', 'Mensaje', 'gtk-ok')

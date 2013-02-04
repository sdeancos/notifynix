notifynix.py
============

A very simple wrapper of dbus org.freedesktop.Notifications in python

Usage
-----

	from notifynix import notification

	notifiaction_object = notification('notifynix.py')
	notifiaction_object.notify('Titulo', 'Mensaje', 'gtk-ok')

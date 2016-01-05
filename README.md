# mailinabox-disable-owncloud
>Disable and delete ownCloud after the mailinabox setup

The fantastic [mailinabox](https://github.com/mail-in-a-box/mailinabox) comes bundeled with the messy owncloud for *DAV handling.

If you don't want owncloud, you can disable it manually. But mailinabox will re-enable it on upgrade, which works the same way as a fresh install, thus reverting your changes.

To save some time, i've written a Python script to manage this, which i can **run just after the mailinabox setup**:

	git clone https://github.com/jsphpl/mailinabox-disable-owncloud
	cd mailinabox-disable-owncloud
	python disable-owncloud.py

I'm quite sure one could do this with one line of sed. If you know how, please tell me!

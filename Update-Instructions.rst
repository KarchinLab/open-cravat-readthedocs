===================
Update instructions
===================

Updating OpenCRAVAT should be done with one of the following methods,
depending on how your OpenCRAVAT was installed on your system.

Determining version number
==========================

The currently installed version of OpenCRAVAT is shown in the upper
right-hand side of the graphical interface. On the on the command line
terminal, type the following:

::

    oc version

New software updates are announced on our Twitter and shown on the
graphical interface in bold red text.

Updating OpenCRAVAT installed with pip
======================================

::

    pip install open-cravat --upgrade --no-cache-dir

All of your modules should remain installed. If your modules directory
is in a non-default location, you may have to point OpenCRAVAT to it
again. Do this using ``oc config md [path]``.

Make sure to launch ``oc gui`` and see if there are any system updates
or module updates available, since a new open-cravat version's web
interface can work only with up-to-date widget modules.

Updating OpenCRAVAT installed with a Windows installer
======================================================

Uninstall open-cravat using Programs and Features under Control Panel or
using Apps and Features.

Download the latest Windows installer at `Installation
Instructions <./1.-Installation-Instructions>`__ and run the installer.

Only open-cravat core programs will be updated while keeping modules,
jobs, and configurations intact.

Updating OpenCRAVAT with a Mac installer
========================================

Open Finder. Click "Applications" folder. Move OpenCRAVAT app to Trash.

Download the latest Mac installer at `Installation
Instructions <./1.-Installation-Instructions>`__ and open the installer.

Only open-cravat core programs will be updated while keeping modules,
jobs, and configurations intact.

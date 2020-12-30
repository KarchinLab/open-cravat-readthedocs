=======
Publish
=======

This section explains how to publish an annotator to the OpenCRAVAT
store.

Creating an Account
===================

Publishing an annotator to the OpenCRAVAT store requires an account. To
create an account, use the command ``oc store new-account``.

.. code:: bash

    oc store new-account user@example.com pw1234

Upon creating an account, a confirmation email will be sent to the user.
The email contains a one-time use password verification link that must
be clicked to verify the account's creation.

Publishing
==========

Once an account has been created and verified, publish an OpenCRAVAT
module with:

::

    oc store publish -u user@example.com -p pw1234 -d|c module_name

The option -d and -c are mutually exclusive and one of them is
mandatory. If your module has data (under your\_module/data folder), -d
option should be given. If no data, then -c option should be used.

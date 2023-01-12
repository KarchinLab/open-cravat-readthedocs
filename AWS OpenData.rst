AWS OpenDATA
============

Amazon Web Services hosts the OpenCRAVAT store through their `Open Data
program <https://aws.amazon.com/opendata>`__. The data is a direct
mirror of the typical OpenCRAVAT store at
https://store.opencravat.org. It is recommended that users on AWS
download data from AWS directly for faster installation speeds.

Using the AWS mirror
--------------------

AWS hosts two mirrors of the store. One for US users in the us-east-1
region, and one for EU users in the eu-west-2 region.

To change the module download URL, must update the ``cravat-system.yml``
config file. To find it, run ``oc config system``. The first line in the
output is the location of the file.

Update the file to include the line

::

   store_url: https://opencravat-store-aws.s3.us-east-1.amazonaws.com

Or, to use the EU mirror

::

   store_url: https://opencravat-store-eu-west-2.s3.eu-west-2.amazonaws.com

Test this my listing the available modules

::

   oc module ls -a

GUI users must must restart the GUI server to load the new store.

You can now use OpenCRAVAT as normal.

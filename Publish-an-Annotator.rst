=======
Publish
=======

This section explains how to publish an annotator to the OpenCRAVAT
store.

Before Publishing 
=================

The following list includes several of the most important pieces of a module that should be checked before publishing. 

Markdown
--------
In the markdown be sure to describe the data, why someone would want it, what the values mean. Include a link to the source text or more advanced documentation, when available. 


Test files
----------
Each module has a test. Tests help you catch mistakes when modules are updated. If the output of a module changes after an update, the test will fail. Tests consist of two files, an input and a key. The input is a cravat formatted [link to cravat format] input file with variants to test against. The key is the output of the text reporter.
To make a test:

#. Make sure the output from your module is correct
#. Pick some variants that represent the data in the module. Choose a few variants that get data, and a few that do not. Try to pick variants that represent a variety of different situations. For example, if your annotator supports both insertion and deletion variants, include one of each. Also include some variants that don’t get annotation from your module. More complicated modules should include more variants.
#. Make a subdirectory in the module directory called “test”. In that directory, make an input file called “input” with the variants you want.
#. Run the input file as shown ``oc run input -t text -a modulename``
#. Rename “input.tsv” to “key”
#. Remove all files other that “input” and “key”
#. In a different directory than your module, run ``oc util test -m modulename``. The test should pass. There will be a file created names something like “cravat_test_12345”. You can safely delete this.
#. When you make updates to your module, run the test again. If the test fails, investigate why. Sometimes the test fails because the key is out of date. Other times, the test fails because there is a mistake in the new version fo the module. If the key is out of date, update it before publishing the new version. Otherwise, fix the module so that the test passes.



Logo
----
While not required, a logo can help users recognize the tool more quickly. The file should be named logo.png. 

YML File
--------

- The output_columns are the columns that will be shown in the viewer. There are 3 main fields: name, title, and type. The name should match the output in the python file. The title is what you want displayed, ideally something short and sweet. The type should also match the output in the python file, such as int, float, or string.
   - Something to consider is the **width** of the column. If you’re not happy with the default you can add this field to either lengthen or shorten the column.
   - The **desc** field is used to include a short description that will be seen when hovering the mouse over the column heading.
   - To choose which columns are always displayed, use the **hidden: true** to hide that field by default. These columns can be viewed by pressing the plus button in the interactive results viewer.  
- **Tags** can be used to group modules together, valid tags can be found in the store.
- The **description** field is used to describe the annotator as a whole, around 140 characters is ideal. It will be displayed when hovering over the name of the annotator.
- The **developer** section is used to describe the name and organization of the tool, as well as a contact email, website link, and MLA citation from the paper. 
- The **datasource** field let’s users know what version of the data was used in making the module. If there is no version number for the tool, a date can be used.
- If necessary **smartfilters** can be added.
- Additionally, the module may require a widget. In this case, the **requires** field will enable the widget to be installed along with the module.
- When it comes time to publish, **private: true** can be added so the module is private. If this is not added, the module will be shared publicly in the store.
 
For syntax pointers, the markdown file for the ClinVar annotator can be used as an example. 




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

Un-publishing
=============

If you are the author of a module, you can un-publish the module you have published. 
Send DELETE request to the following URL to delete a specific version of a module.
The username and password for the author of the module should be sent as well.

::

   http://<store URL>/<module name>/<version>

A python example is below.

::

   import requests
   username = "user"
   password = "password"
   requests.delete("http://karchinlab.org/cravatstore/example_module/1.0.0", auth=(username, password))


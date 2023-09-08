.. role:: raw-latex(raw)
   :format: latex
..

=======================
Command line quickstart
=======================

Installing Python Package manually
----------------------------------

If Python version 3.6 or newer is installed, run the following command
to install the OpenCRAVAT pip package.

::

    pip install open-cravat

Depending on your python configuration, the base command for pip may be
be ``pip3`` instead of ``pip``. ``sudo`` should be avoided in installing
OpenCRAVAT.

If you use Windows and your Python 3 is installed inside of a
system-level folder such as "C::raw-latex:`\Program `Files", you may
have a problem with running OpenCRAVAT without admin privilege. In this
case, we recommend installing Python 3 outside of system-level folders
and then installing OpenCRAVAT.

Install Base Components
-----------------------

Now that the OpenCRAVAT python package is installed, you must install
the base OpenCRAVAT modules. Run the following command.

``oc module install-base``

One of the base components, hg38 gene mapper, requires downloading 2 Gb
of data.

Install an Annotator
--------------------

You can search for annotators to install with the command

``oc module  ls -a -t annotator``

This also tells you which annotators you have installed.

You can also use regular expressions to filter annotators by their
names.

``oc module  ls -a cosmic.* -t annotator``

To install an annotator use:

``oc module  install <annotator name>``

For this Quickstart, we install the ClinVar annotator as an example. Run
the following command

``oc module  install clinvar``

Test Run
--------

OpenCRAVAT is now ready to use. With the base components installed,
OpenCRAVAT can annotate variants with genes and sequence ontology. We've
also installed the ClinVar annotator.

If you want, you can test if OpenCRAVAT is working properly using a
built-in test input. Create a new directory, and make it the working
directory. Make the test input file with

``oc new example-input .``

which will create example\_input in the current working directory. If
you want to create the file in another directory, replace "." with the
path to the directory.

Then, run OpenCRAVAT on the test input file with

``oc run ./example_input -l hg38``

If example\_input is not in the current working directory, use the full
path to example\_input instead of just "example\_input". The run will
create many files, all with the prefix "example\_input.".

Once the job is finished, it will create a sqlite database with the
results. This sqlite database can be opened in the OpenCRAVAT web viewer
with the command

``oc gui example_input.sqlite``

Instructions for using ``oc gui`` and the web viewer are
`here <5.-GUI-usage.rst>`__.

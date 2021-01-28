===================
Annotator reference
===================

This section provides detailed reference documentation for each
component of an annotator. An annotator consists of a python file, a
YAML file, a data directory, and a markdown file (optional). The file
structure is as follows:

.. code:: text

    annotator/
        |───annotator.md
        |───annotator.yml
        |───annotator.py
        └───data/

In an actual annotator, the name 'annotator' would be substituted for
the annotator's name. Also note that the annotator's data source (the
directiory ``annotator/data``) will be filled with some configuration of
data files. More info on the data source can be found at
```data`` <#data>`__.

``annotator.md``
================

The markdown file describes the module to prospective users. It is not
required to run an annotator; however, it is required when publishing an
annotator to the OpenCRAVAT store.

``annotator.yml``
=================

The YAML file defines the input and output interfaces between an
annotator and the rest of OpenCRAVAT. The YAML file specifies what data
will be fed to ``annotator.py`` from OpenCRAVAT, and what data
OpenCRAVAT should expect ``annotator.py`` to return. Below are the valid
keys a developer may use in their YAML file.

Properties
----------

+-----------------+-----------+-----------------------+------------------+
| **Property**    | Required  | Required to Publish   | **Description**  |
+=================+===========+=======================+==================+
| ``title``       | X         | X                     | The name of the  |
|                 |           |                       | module that will |
|                 |           |                       | be displayed to  |
|                 |           |                       | the user.        |
+-----------------+-----------+-----------------------+------------------+
| ``version``     | X         | X                     | The version      |
|                 |           |                       | number of the    |
|                 |           |                       | annotator. It is |
|                 |           |                       | primarily used   |
|                 |           |                       | when publishing  |
|                 |           |                       | a module, but is |
|                 |           |                       | required for all |
|                 |           |                       | modules.         |
+-----------------+-----------+-----------------------+------------------+
| ``type``        | X         | X                     | The module type, |
|                 |           |                       | in this case     |
|                 |           |                       | 'annotator'.     |
+-----------------+-----------+-----------------------+------------------+
| ``level``       | X         | X                     | Either 'variant' |
|                 |           |                       | or 'gene'.       |
+-----------------+-----------+-----------------------+------------------+
| ``input_format` |           |                       | The input file   |
| `               |           |                       | type. Accepted   |
|                 |           |                       | values are       |
|                 |           |                       | ``.crv``,        |
|                 |           |                       | ``.crx``, and    |
|                 |           |                       | ``.crg``. When   |
|                 |           |                       | omitted, the     |
|                 |           |                       | default is       |
|                 |           |                       | ``.crv``.        |
+-----------------+-----------+-----------------------+------------------+
| ``output_column | X         | X                     | A list of the    |
| s``             |           |                       | output columns   |
|                 |           |                       | from the         |
|                 |           |                       | annotator. See   |
|                 |           |                       | `Output          |
|                 |           |                       | Columns <#output |
|                 |           |                       | -columns>`__     |
|                 |           |                       | sub-section for  |
|                 |           |                       | more details.    |
+-----------------+-----------+-----------------------+------------------+
| ``description`` |           | X                     | A short          |
|                 |           |                       | description of   |
|                 |           |                       | the module's     |
|                 |           |                       | purpose and use. |
+-----------------+-----------+-----------------------+------------------+
| ``developer``   |           | X                     | Information      |
|                 |           |                       | about the        |
|                 |           |                       | developer.       |
|                 |           |                       | Subkeys: name,   |
|                 |           |                       | email,           |
|                 |           |                       | organization,    |
|                 |           |                       | website,         |
|                 |           |                       | citation.        |
+-----------------+-----------+-----------------------+------------------+

Output Columns
--------------

The ``output_columns`` property is a YAML list that enumerates the
expected keys of the dictionary returned by ``annotator.py``. The
preparation of this dictionary is explained in greater detail in
```annotator.py`` <#annotatorpy>`__. Each entry in the
``output_columns`` list requires three properties: ``name``, ``title``,
and ``type`` described in the table below.

+-----------------+-----------+-----------------------+------------------+
| **Property**    | Required  | Required to Publish   | **Description**  |
+=================+===========+=======================+==================+
| ``name``        | X         | X                     | The column's     |
|                 |           |                       | internal name.   |
|                 |           |                       | Used to identify |
|                 |           |                       | the column in    |
|                 |           |                       | the output       |
|                 |           |                       | dictionary from  |
|                 |           |                       | ``annotator.py`` |
|                 |           |                       | .                |
+-----------------+-----------+-----------------------+------------------+
| ``title``       | X         | X                     | The column's     |
|                 |           |                       | display name.    |
|                 |           |                       | Used in the      |
|                 |           |                       | final report.    |
+-----------------+-----------+-----------------------+------------------+
| ``type``        | X         | X                     | The data-type of |
|                 |           |                       | that column.     |
|                 |           |                       | Either           |
|                 |           |                       | ``string``,      |
|                 |           |                       | ``int``, or      |
|                 |           |                       | ``float``.       |
+-----------------+-----------+-----------------------+------------------+

``annotator.py``
================

The python module receives input data describing a single variant/gene,
and uses it to lookup additional information specific to that annotator.
An ``annotator.py`` works by extending a provided base class,
``BaseAnnotator``, and implementing three instance methods: ``setup``,
``annotate``, and ``cleanup``.

``setup``
---------

The ``setup`` method executes once before the main loop over the input
file. It is normally used to open file-handlers or database connections.
More information on accessing the data source can be found in
```data`` <#data>`__.

``annotate``
------------

The ``annotate`` method executes once per iteration of the main loop.
The ``annotate`` method will receive an ``input_data`` argument, and
possibly an optional ``secondary_data`` argument. These arguments
represent the input data for a single variant/gene. Both arguments will
be python dictionaries, whose format (including presence altogether for
``secondary_data``) is determined by the ``input_format`` property of
``annotate.yml``. The following table enumerates the possible keys of
``input_data``, and which keys will be present in relation to the value
of ``input_format``.

+----------------+------------+------------+------------+----------------+--------------+
| **Key**        | **``.crv`` | **``.crx`` | **``.crg`` | **Description* | **Example**  |
|                | **         | **         | **         | *              |              |
+================+============+============+============+================+==============+
| ``uid``        | X          | X          |            | An id.         | 1, 2         |
+----------------+------------+------------+------------+----------------+--------------+
| ``chrom``      | X          | X          |            | The            | 'chr1',      |
|                |            |            |            | chromosome,    | 'chr23',     |
|                |            |            |            | with prefix    | 'chrX'       |
|                |            |            |            | 'chr'. 1-based |              |
|                |            |            |            | indexing.      |              |
+----------------+------------+------------+------------+----------------+--------------+
| ``pos``        | X          | X          |            | An integer     | 112501307,   |
|                |            |            |            | genomic        | 104770363    |
|                |            |            |            | position.      |              |
+----------------+------------+------------+------------+----------------+--------------+
| ``ref_base``   | X          | X          |            | The reference  | 'A', 'GCC'   |
|                |            |            |            | base.          |              |
+----------------+------------+------------+------------+----------------+--------------+
| ``alt_base``   | X          | X          |            | The alternate  | 'G', 'AT',   |
|                |            |            |            | base.          | '-'          |
+----------------+------------+------------+------------+----------------+--------------+
| ``hugo``       |            | X          | X          | The gene name  | TP53         |
+----------------+------------+------------+------------+----------------+--------------+
| ``transcript`` |            | X          |            | The predicted  | ENST00000617 |
|                |            |            |            | primary        | 185.4        |
|                |            |            |            | transcript     |              |
+----------------+------------+------------+------------+----------------+--------------+
| ``so``         |            | X          | X          | Most severe    | MIS          |
|                |            |            |            | sequence       |              |
|                |            |            |            | ontology       |              |
+----------------+------------+------------+------------+----------------+--------------+
| ``all_mappings |            | X          |            | All affected   | `Examples    |
| ``             |            |            |            | transcripts.   | here <#Input |
|                |            |            |            | `Details       | -Formats#all |
|                |            |            |            | here <#Input-F | -mappings>`_ |
|                |            |            |            | ormats#all-map | _            |
|                |            |            |            | pings>`__      |              |
+----------------+------------+------------+------------+----------------+--------------+
| ``num_variants |            |            | X          | Number of      | 5            |
| ``             |            |            |            | variants on    |              |
|                |            |            |            | this gene      |              |
+----------------+------------+------------+------------+----------------+--------------+
| ``all_so``     |            |            | X          | Sequence       | STL(1),MIS(3 |
|                |            |            |            | ontologies and | )            |
|                |            |            |            | counts for     |              |
|                |            |            |            | this gene      |              |
+----------------+------------+------------+------------+----------------+--------------+

OpenCRAVAT expects ``annotator.py`` to return a python dictionary. The
keys present in this dictionary, and the data-types of their values are
both determined by the ``output_columns`` property in ``annotator.yml``.

``cleanup``
-----------

The ``cleanup`` method executes once after the main loop has finished.
It is normally used to close any database connection or file-handlers
opened in ``setup``.

``data``
========

The sub-directory ``data`` contains the data source for the annotator.
This can be a flat-data file, a sqlite database, or a combination of
multiples data files. To access the data, the developer will open a
file-handler or database connection depending on the file type. This
should be done in the instance method ``setup`` in
```annotate.py`` <#annotatepy>`__. The developer should then store the
opened data-accessor as a ``self`` instance property to be accessible
during the ``annotate`` method.

Note that there is special support for a sqlite database which shares
the name of the annotator module. In this case, a database connection
and cursor are automatically opened in the ``BaseConverter`` of
``annotate.py``. The connection and cursor are stored as ``self.dbconn``
and ``self.cursosr`` respectively. This functionality is intened to aid
a primary use case where the data source is a single sqlite database. A
developer can safely overwrite ``self.dbconn`` and ``self.cursor`` if
they wish, albeit at the loss of the automatic functionality.

The developer should close any active database connections or
file-handlers during the ``cleanup`` method of ``annotate.py``.
Automatically opened database connections will also be automatically
closed.

Secondary Inputs
================

Annotators can be piped together so that the output of one annotator can
be used in the input of another annotator. This can be useful to create
annotators that summarize groups of other annotators, or to use the data
from another annotator in a query.

For example, lets say we have data that is indexed on ClinVar IDs. We
can make an annotator that depends on the clinvar annotator, then use
the ID to lookup our values.

Edit ``annotator.yml`` and add a secondary data input.

.. code:: yaml

    secondary_inputs:
      clinvar: {}

Now, in the ``annotate`` method of ``annotator.py``, the
``secondary_data`` argument will sometimes contain data from clinvar.

.. code:: python

    if secondary_data['clinvar']:
        clinvar_id = secondary_data['clinvar'][0]['id']
    else:
        clinvar_id = None

We also want to make sure that users who install our annotator have
clinvar installed. Do do this, we need to add an install requirement to
our annotator's config.

.. code:: yaml

    requires:
    - clinvar

If you need to require certain version of the secondary annotator, you
can do so with boolean expressions similar to those in pip install.

.. code:: text

    clinvar==2.0.0
    clinvar>=2.0.0
    clinvar<2.0.0

Specifying a version is discouraged unless **absolutely needed**.
OpenCRAVAT has very limited ability to resolve dependency issues between
modules.

Table-in-table output
=====================

Originally, an output field of an OpenCRAVAT annotator module was supposed to be one of string, integer, and float types. However, from OpenCRAVAT 2.2.1, an output field can contain a table of values. This way, table-in-table output is possible for annotation modules. This feature is useful for organizing complex data. For example, VEST4 annotation module's "All transcripts" column used to have such a string as "ENST00000612895.4(0.884:0.04118), *ENST00000614428.4(0.928:0.02102), ENST00000617649.4(0.866:0.05418)". This string contains the VEST score and p-value for three different transcripts for a variant. To get the score and p-value of a specific transcript, parsing the string and extracting the values was necessary. However, the new VEST annotation module which works with OpenCRAVAT 2.2.1 and later has the following data instead of the string: [[ENST00000612895.4, 0.884, 0.04118], [ENST00000614428.4, 0.928, 0.02102], [ENST00000617649.4, 0.866, 0.05418]], which shows the transcript-score-pvaule organization of data much more clearly. This type of data is still stored as string in result databases, but OpenCRAVAT automatically performs the conversion between string and JSON object as it communicates with annotator modules. Thus, in writing an annotation module, the return dictionary of an annotate method can have a dictionary as the value of an output field. No conversion to a JSON string is necessary.

To enable table-in-table output support for an output column, add `table: true` property to the definition of the column in the module's configuration yml file. There is another property, `table_headers`, but this one is optional. With these two new properties, "All annotations" (previously "All transcripts") column of VEST module is defined as below.

\- name: all

title: All annotations

type: string

table: true

table_headers:
\- name: transcript

title: Transcript

type: string

\- name: score

title: Score

type: float

\- name: pval

title: p-value

type: float
  ...

When an output column with table data is used by a reporter module, the reporter module will receive a JSON object instead of a string, as OpenCRAVAT does the conversion automatically. In the same way, widget modules will also receive JSON objects instead of strings for output columns with table data. (edited) 


 

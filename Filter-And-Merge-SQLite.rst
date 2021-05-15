============
Filter and Merge Result Databases
============

Filter Result Databases
~~~~~~~~~~~~~~~~~~~~~~~

OpenCRAVAT jobs produce result database files which are SQLite files. 
The variants and samples in these result databases can be filtered into new result databases.

Syntax
-------

.. code:: text

 oc util filtersqlite INPUT [INPUT]... -o OUTDIR -s SUFFIX -f FILTERPATH --filtersql FILTERSQL --includesample SAMPLE [SAMPLE]... --excludesample SAMPLE [SAMPLE]...


+----------+----------------------------------------------------------+
|INPUT     |Path to a result database file to filter                  |
+----------+----------------------------------------------------------+
|OUTDIR    |Path to a folder where new database files will be created |
+----------+----------------------------------------------------------+
|SUFFIX    |Suffix for new database files. Default is `filtered`.     |
|          |For example, if INPUT is `example.sqlite` and SUFFIX is   |
|          |`new`, `example.new.sqlite` will be created with filtered |
|          |variants and samples.                                     |
+----------+----------------------------------------------------------+
|FILTERPATH|Path to a filter JSON file                                |
+----------+----------------------------------------------------------+
|FILTERSQL |SQL-format string of filters (see Filter SQL section)     |
+----------+----------------------------------------------------------+
|SAMPLE    |Sample names to include or exclude                        |
+----------+----------------------------------------------------------+

Example
--------

.. code:: text

 oc util filtersqlite example.sqlite another_result.sqlite --filtersql '(v.base__so=="MIS" and v.clinvar__sig=="Pathogenic")' --excludesample badsample1 badsample2

``example.filtered.sqlite`` and ``another_result.filtered.sqlite`` will be created with the default ``filtered`` suffix and with filtered variants which are missense variants 
in representative transcripts (MANE transcripts by default) and have ``Pathogenic`` ClinVar significance. 
Samples ``badsample1`` and ``badsample2`` and variants from them will be excluded.

.. code:: 

 oc util filtersqlite result.sqlite -f filter.json --suffix new -o ~/filtered_results

``result.new.sqlite`` will be created in ``~/filtered_results`` folder with the filters defined in `filter.json` file.
 
Merge Result Databases
~~~~~~~~~~~~~~~~~~~~~~

OpenCRAVAT result database files which were produced with exactly the same set of annotators can be merged with the following command.

Syntax
------

.. code:: text

 oc util mergesqlite INPUT [INPUT]... -o OUTPUT

+--------+--------------------------------------------------+
|INPUT   | Path to an OpenCRAVAT result database file       |
+--------+--------------------------------------------------+
|OUTPUT  | Path to a merged OpenCRAVAT result database file |
+--------+--------------------------------------------------+

Example
-------

.. code:: text

 oc util mergesqlite result.sqlite another_result.sqlite -o merged.sqlite

The variants and samples in ``result.sqlite`` and ``another_result.sqlite`` will be merged and written to ``merged.sqlite``.



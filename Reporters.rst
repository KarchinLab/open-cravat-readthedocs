==================
OpenCRAVAT reports
==================

OpenCRAVAT can output annotation results in various formats to support different ways of viewing results, and integration with downstream analysis.

Outputs are created by running the ``oc report`` command on an OpenCRAVAT sqlite database.

::

    oc report job.sqlite -t tsv excel

The ``-t`` flag is required to select one or more reporters to run. Multiple formats can be generated in a single command. The exact output files created are listed in the terminal output:

::

    $ oc report job.sqlite -t tsv excel
    Generating tsv report... report created: job.variant.tsv
    Generating excel report... report created: job.xlsx

Output files are created in the same directory as the sqlite database. Use ``-d`` to write to a different directory, and ``-n`` to set the output filename prefix.

Discovering and installing reporters
-------------------------------------

List reporters you have installed::

    oc module ls -t reporter

Browse all available reporters in the store::

    oc module ls -a -t reporter

Install a reporter::

    oc module install reporter_module_name

``oc report`` options
---------------------

+------------------------------------------+--------------------------------------------------------------------------+
| Option                                   | Description                                                              |
+==========================================+==========================================================================+
| -t [FORMAT [FORMAT ...]]                 | Report type(s) to generate: ``excel``, ``tsv``, ``vcf``, ``text``,       |
|                                          | ``csv``                                                                  |
+------------------------------------------+--------------------------------------------------------------------------+
| -d OUTPUT_DIR                            | Directory for output files (default: directory of the sqlite file)       |
+------------------------------------------+--------------------------------------------------------------------------+
| -n RUN_NAME                              | Output filename prefix (default: input filename)                         |
+------------------------------------------+--------------------------------------------------------------------------+
| -f FILTERPATH                            | Path to a filter file                                                    |
+------------------------------------------+--------------------------------------------------------------------------+
| -F FILTERNAME                            | Name of a filter stored in the sqlite database                           |
+------------------------------------------+--------------------------------------------------------------------------+
| --nogenelevelonvariantlevel              | Prevent gene-level results from being added to the variant-level output  |
+------------------------------------------+--------------------------------------------------------------------------+
| --separatesample                         | Write each variant-sample pair on a separate line                        |
+------------------------------------------+--------------------------------------------------------------------------+
| --module-option MODULE.KEY=VALUE         | Pass a configuration option to a specific reporter module,               |
|                                          | e.g. ``--module-option csvreporter.pages=sample``                        |
+------------------------------------------+--------------------------------------------------------------------------+
| -c CONFPATH                              | Path to a configuration file                                             |
+------------------------------------------+--------------------------------------------------------------------------+
| --confs CONFS                            | Configuration string                                                     |
+------------------------------------------+--------------------------------------------------------------------------+

Report formats
--------------

excel
-----

Produces a ``.xlsx`` spreadsheet. This is the default reporter included with a base installation.

tsv
---

Produces a tab-separated values file per requested level. By default only the variant level is written (``job.variant.tsv``). To include other levels, use ``--module-option tsvreporter.pages=variant,gene`` (any combination of ``variant``, ``gene``, ``sample``, ``mapping`` is accepted). Each requested level produces a separate file.

text
----

Writes all four levels (variant, gene, sample, mapping) to a single file by default.

csv
---

Produces a comma-separated values file. Accepts the same options as the TSV reporter.

vcf
---

Produces an annotated VCF file with OpenCRAVAT annotations added to the INFO field.

Note that if the input was not a VCF file, the output will lack fields such as zygosity or read depth. If you are annotating a VCF input and want a fully annotated VCF output, see :doc:`VCFAnno`.

Building your own reporter
--------------------------

See the :doc:`Custom-Reporter` page for documentation on writing a custom reporter module.
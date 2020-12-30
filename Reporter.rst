=================
Reporter tutorial
=================

Reporters are used to generate output files from an OpenCRAVAT output
database.

Example
=======

Readers who prefer to learn by reading code should see the example
reporter in
`open-cravat-modules-karchinlab <https://github.com/KarchinLab/open-cravat-modules-karchinlab/blob/master/reporters/examplereporter/examplereporter.py>`__.

The rest of this document will explain how reporters are structured, and
the meaning of some low-level data.

Overview
========

Levels
------

OpenCRAVAT data is structured into 4 levels: variant, gene, sample, and
mapping. These levels correspond directly to four tables in the output
database. The first two levels, variant and gene, contain information
about variants and genes that OpenCRAVAT generates, and data from
annotators. The sample level keeps track of which samples contain a
certain variant, and can include information about specific ocurrences
of a variant, such as zygosity. Finally, the mapping level keeps track
of where in the original input files a variant was found.

Most reporters will be concerned with the variant and gene level data,
and that will be the focus of this page. Sample and mapping level data
can be handled in a similar way.

Structure of a reporter
-----------------------

Reporters must define four functions: ``setup``, ``write_header``,
``write_table_row``, and ``end``.

``setup`` is called once. It is used to open file handlers and do other
such initialization tasks.

``write_header`` is called once per level. It is used to write
information about the data that will be in that level.

``write_table_row`` is called once per "row" of data. In the variant
level this means once per variant. In the gene level, once per gene.

``end`` is used to close file handlers and do other such cleanup tasks.

Most of the work of a reporter is done in ``write_header`` and
``write_table_row``. The following two sections will cover the data
structures of those two functions.

Low level
=========

``write_table_row`` takes a single argument, ``row``, which is a list of
the values for that row. For example, at the variant level, the first
part of row might be:

::

    [1, 'chr3', 41266113, 'C', 'T', None, None, 'ULK4', 'ENST00000301831.9', ...]

Each of these columns is identified in a attribute called
``self.colinfo``, a multi-level dict with information about all the
columns in the job. A summary of it's structure is below.

::

    self.colinfo = {
        'variant': {
            'columns': [
                {
                    'col_name': 'base__uid',
                    'col_title': 'UID',
                    'col_type': 'int',
                    ...
                },
                {
                    'col_name': 'base__chrom',
                    'col_title': 'Chrom',
                    'col_type': 'string',
                    ...
                },
                {
                    'col_name': 'base__pos',
                    'col_title': 'Position',
                    'col_type': 'int',
                    ...
                },
                ...
            ]
            'colgroups': [
                {
                    'name': 'base',
                    'displayname': 'Variant Annotation',
                    'count': 16,
                    'lastcol': 16,
                    ...
                },
                {
                    'name': 'clinvar',
                    'displayname': 'ClinVar',
                    'count': 5,
                    'lastcol': 21,
                    ...
                }
            ]
        },
        'gene':{...},
        'sample':{...},
        'mapping':{...}
    }

At the top, ``self.colinfo`` is divided into each level, then into
``'columns'`` and ``'colgroups'``. The list
``self.colinfo['level']['columns']`` matches up with the ``row`` list
passed to ``write_table_row``. Columns from the same annotator are
located next to each other. The list ``colgroups`` contains information
about each annotator, and can be used to select data from that
annotator.

In practice
-----------

Generally, ``write_header`` reads information from ``self.colinfo`` and
write descriptions of each column to the output file. Then
``write_table_row`` writes the value of each cell.

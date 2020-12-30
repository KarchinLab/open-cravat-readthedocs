============
File Formats
============

CRAVAT Input Format
-------------------

OpenCRAVAT has a custom tab separated input file format, that can be
used in place of vcf. Each row in a CRAVAT input file describes a
genomic variant by the following sequential columns: Chromosome,
Position, Strand, Reference-Base, Alternate-Base, and, optionally,
Sample. The table below describes each field:

Columns
~~~~~~~

+---------+--------------+----------+
| Column  | Description  | Example  |
+=========+==============+==========+
| Chromos | The          | ``'chr22 |
| ome     | chromosome,  | '``,     |
|         | prefixed     | ``'chrX' |
|         | with         | ``       |
|         | ``'chr'``.   |          |
+---------+--------------+----------+
| Positio | The 1-based  | 11250130 |
| n       | position of  | 7,       |
|         | the first    | 1804372  |
|         | affected     |          |
|         | nucleotide.  |          |
+---------+--------------+----------+
| Strand  | The strand   | ``'+'``/ |
|         | the variant  | ``'-'``  |
|         | is on.       |          |
|         | Either       |          |
|         | ``'+'`` or   |          |
|         | ``'-'``.     |          |
+---------+--------------+----------+
| Referen | The affected | ``'G'``, |
| ce-Base | nucleotide(s | ``'AG'`` |
|         | ),           | ,        |
|         | or a ``'-'`` | ``'TTCC' |
|         | for an       | ``,\ ``' |
|         | insertion.   | -'``     |
+---------+--------------+----------+
| Alterna | The          | ``'A'``, |
| te-Base | alternate    | ``'TTC'` |
|         | nucleotide(s | `,       |
|         | ),           | ``'-'``  |
|         | or ``'-'``   |          |
|         | for a        |          |
|         | deletion.    |          |
+---------+--------------+----------+
| Sample  | The sample   | ``'s1'`` |
|         | identifier.  | ,        |
|         |              | ``'s25'` |
|         |              | `        |
+---------+--------------+----------+
| Tag     | Optional:    | ``'var00 |
|         | Arbitrary    | 1'``,    |
|         | identifiers  | ``'TR93; |
|         | or category  | cancer'` |
|         | tags         | `        |
|         | associated   |          |
|         | with the     |          |
|         | variant -    |          |
|         | delimited by |          |
|         | semi-colon.  |          |
+---------+--------------+----------+

Example
~~~~~~~

The following is a basic example of a CRAVAT input file:

.. code:: txt

    chr2    112501307   +   C   A   s1    var001
    chr14   104770363   +   T   A   s1    var002
    chrX    71127984    +   A   G   s2    var003
    chr14   91974629    +   T   G   s3    var004
    chr12   57094662    +   G   T   s4    var005
    ...

Internal Files
--------------

OpenCRAVAT uses a variety of text based file formats to pass data
internally between modules. Most of these internal files are temporary,
and are deleted at the end of a successful run. They can be preserved by
passing the ``--temp-files`` flag to ``oc run`` .

In general, OpenCRAVAT files are tab separated tabular text files with
self defined columns, similar to a vcf. They start with a series of
comment lines describing the columns in the tabular section, then a
header row for the table, then the table itself. A basic example can be
seen here:

.. code:: text

    #column=0,Column0,col0,string
    #column=1,Col 1,column_1,int
    #column=2,Col-2,c2,float
    #Column0    Col 1   Col-2
    row1    1   1.0
    row2    2   2.0
    row3    3   3.0

column definition
~~~~~~~~~~~~~~~~~

The column definition lines define four commas separated values:

1. Index: which column in the table this column definition refers to.
2. Title: a display only title for the column. Used as a header when
   presenting data to the user. Can be changed at any point without
   affecting cravat.
3. Name: the internal name of the column, used to refer to it in code.
   Should only be changed carefully.
4. Type: The type of data in this column. Data will be cast to this type
   when read from the file.

header row
~~~~~~~~~~

This is a header row for the table, typically using the column titles.
It is not needed for OpenCRAVAT to function, and is included for
readability.

table
~~~~~

Tab separated values. Blank columns should be represented by an empty
string.

.crv Files
----------

crv files (.crv) are basic OpenCRAVAT files that describe variants based
on their genomic position and effect. They are produced by OpenCRAVAT
converters.

crv example
~~~~~~~~~~~

.. code:: text

    #column=0,UID,uid,int
    #column=1,Chrom,chrom,string
    #column=2,Position,pos,int
    #column=3,Ref Base,ref_base,string
    #column=4,Alt Base,alt_base,string
    #UID    Chrom   Position    Ref Base    Alt Base
    1   chr19   10156403    G   C
    2   chr7    140834746   A   T

crv columns
~~~~~~~~~~~

+-------------+-----------------------------------------------------+------------+---------------------+
| **name**    | **Description**                                     | **Type**   | **Example(s)**      |
+=============+=====================================================+============+=====================+
| uid         | Unique id of variant.                               | int        | 13                  |
+-------------+-----------------------------------------------------+------------+---------------------+
| chrom       | Chromosome                                          | string     | chr1, chr17, chrX   |
+-------------+-----------------------------------------------------+------------+---------------------+
| pos         | Genomic position of first affected base (1-based)   | int        | 1234                |
+-------------+-----------------------------------------------------+------------+---------------------+
| ref\_base   | Reference base(s)                                   | string     | A, AT, -            |
+-------------+-----------------------------------------------------+------------+---------------------+
| alt\_base   | Alternate base(s)                                   | string     | G, GC, -            |
+-------------+-----------------------------------------------------+------------+---------------------+

Deletions are written with an ref of the bases to be deleted, and an alt
of '-'.

.. code:: text

    1  chr1    1234    A   -

Insertions are written with an ref of '-' and an alt of the bases to be
inserted.

.. code:: text

    1  chr1    1234    -   A

.crx Files
----------

crx files (.crx) are an e\ **x**\ tended version of .crv files. They
describe variants based on their affect on the genome, but also on
genes, transcripts, and proteins. They are produced by OpenCRAVAT
mappers.

crx example
~~~~~~~~~~~

.. code:: text

    #column=0,UID,uid,int
    #column=1,Chrom,chrom,string
    #column=2,Position,pos,int
    #column=3,Ref Base,ref_base,string
    #column=4,Alt Base,alt_base,string
    #column=5,Hugo,hugo,string
    #column=6,Transcript,transcript,string
    #column=7,All Mappings,all_mappings,string

    #UID    Chrom   Position    Ref Base    Alt Base    Hugo    Transcript  All Mappings
    1   chr19   10156403    G   C   DNMT1   ENST00000340748.8   {"DNMT1":[["P26358","P447A","MIS","ENST00000340748.8","C1339G"]]}
    2   chr7    140834746   A   T   BRAF    ENST00000288602.10  {"BRAF":[["P15056","S123T","MIS","ENST00000288602.10","T367A"]]}

All Mappings
^^^^^^^^^^^^

The all mappings column contains a json object describing the genes,
transcripts, and proteins that a variant affected. It has the following
schema,

.. code:: json

    {
      "gene": [
        [
          "protein 1",
          "amino acid change 1",
          "sequence ontology 1",
          "transcript 1",
          "rna change 1"
        ],
        [
          "protein 2",
          "amino acid change 2",
          "sequence ontology 2",
          "transcript 2",
          "rna change 2"
        ]
      ]
    }

Sequence ontologies are encoded with three letter abbreviations.

+------------+-------------------------------+
| **Abbv**   | **Sequence Ontology**         |
+============+===============================+
| 2KD        | 2 Kb downstream from gene     |
+------------+-------------------------------+
| 2KU        | 2 Kb upstream from gene       |
+------------+-------------------------------+
| UT3        | In the 3' UTR                 |
+------------+-------------------------------+
| UT5        | In the 5' UTR                 |
+------------+-------------------------------+
| INT        | In an intron                  |
+------------+-------------------------------+
| UNK        | Unknown sequence ontology     |
+------------+-------------------------------+
| SYN        | Synonomous                    |
+------------+-------------------------------+
| MIS        | Missense                      |
+------------+-------------------------------+
| CSS        | Complex substitution          |
+------------+-------------------------------+
| IDV        | Inframe deletion              |
+------------+-------------------------------+
| IIV        | Inframe insertion             |
+------------+-------------------------------+
| STL        | Stoploss                      |
+------------+-------------------------------+
| SPL        | Splice site affected          |
+------------+-------------------------------+
| STG        | Stopgain                      |
+------------+-------------------------------+
| FD2        | 2 base frameshift deletion    |
+------------+-------------------------------+
| FD1        | 1 base frameshift deletion    |
+------------+-------------------------------+
| FI2        | 2 base frameshift insertion   |
+------------+-------------------------------+
| FI1        | 1 base frameshift insertion   |
+------------+-------------------------------+

.var/.gen Files
---------------

Every OpenCRAVAT annotator will produce an output file with the suffix
``[annotatorName].var`` for a variant level annotator, and
``[annotatorName].gen`` for gene level.

As an example, running the ``vest`` and ``go`` annotators on
``input.vcf``:

.. code:: bash

    oc run input.vcf -a vest go --temp-files

Will produce ``input.vcf.vest.var`` and ``input.vcf.go.gen``.

The annotator ouput files will contain a header that defines the
annotator's internal name display name, and column definitions.
Following the header will be rows of tab separated data values.

An example snippet from ``input.vcf.vest.var`` is as follows:

::

    #name=vest
    #displayname=VEST
    #column=0,UID,uid,int
    #column=1,VEST score transcript,transcript,string
    #column=2,VEST score,score,float
    #column=3,VEST p-value,pval,float
    #column=4,VEST score (missense),score_mis,float
    #column=5,VEST score (frameshift),score_fsv,float
    #column=6,VEST score (inframe indel),score_inv,float
    #column=7,VEST score (stop gain),score_stg,float
    #column=8,VEST score (stop loss),score_stl,float
    #column=9,VEST score (splice site),score_spl,float
    #column=10,All transcripts,all_results,string
    #column=11,HUGO,hugo,string
    #no_aggregate=hugo
    #UID    VEST score transcript   VEST score  VEST p-value    VEST score (missense) ...
    1   ENST00000233336.6   0.773   0.0417  0.773 ...
    2   ENST00000554848.5   0.707   0.06973 0.707 ...
    3   ENST00000374080.7   0.143   0.65145 0.143 ...
    4   ENST00000267622.8   0.541   0.16344 0.541 ...
    5   ENST00000342556.6   0.321   0.31889 0.321 ...

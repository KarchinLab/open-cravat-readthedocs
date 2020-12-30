==================
Running OpenCRAVAT
==================

OpenCRAVAT can be run via the `Web Interface <./5.-Web-Interface>`__ or
`Command line <./2.-Running-cravat>`__. Upon completion of an annotation
run, results be viewed in the `Interactive
Viewer <./3.-Viewing-Results>`__ or by viewing the outputted files.

Input of multiple files
=======================

Submitting multiple input files is supported by OpenCRAVAT. The system
will automatically merge and deduplicate your input files, and will only
process each unique variant once. As a result, expected runtime for
multiple input files depends on the uniqueness of the variants in each
file. Runtimes will be the same as if each unique variant was submitted
in a single file. OpenCRAVAT can process arbitrarily large numbers of
input files. However, it may be hard to navigate the web viewer when
more than 10 input files are used.

There are two input file formats currently supported by default: VCF and
CRAVAT.

VCF Input Format
================

Variant Call Format (VCF) is a standard variant file format that is
produced by sequencing centers and by variant calling software packages.
A specification of the format is available
`here <https://samtools.github.io/hts-specs/VCFv4.2.pdf>`__.

VCF files sometimes contain multiple variants on a single line
(separated by commas in the ALT column). These variants can have
different scores and annotations so the converter will split these into
individual variants (e.g Reference base C Alternate base T and Reference
base C Alternate base G).

Example
-------

.. code:: txt

    ##fileformat=VCFv4.1
    ##fileDate=20090805
    ##source=myImputationProgramV3.1
    ##reference=file:///seq/references/1000GenomesPilot-NCBI36.fasta
    ##contig=<ID=20,length=62435964,assembly=B36,md5=f126cdf8a6e0c7f379d618ff66beb2da,species="Homo sapiens",taxonomy=x>
    ##phasing=partial
    ##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">  
    ##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth"> 
    ##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">  
    ##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">  
    ##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">  
    ##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">  
    ##FILTER=<ID=q10,Description="Quality below 10">  
    ##FILTER=<ID=s50,Description="Less than 50% of samples have data">  
    ##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">  
    ##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">  
    ##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">  
    ##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">  
    #CHROM  POS ID  REF ALT QUAL    FILTER  INFO    FORMAT  NA00001 NA00002 NA00003  
    20  85729   rs6054257   G   A   29  PASS    NS=3;DP=14;AF=0.5;DB;H2 GT:GQ:DP:HQ:AD  0|0:48:1:51,51:0,1  1|0:48:8:51,51:4,4  1/1:43:5:.,.:1,4  
    20  1130053 rs6040355   A   G,T 67  PASS    NS=2;DP=10;AF=0.333,0.667;AA=T;DB   GT:GQ:DP:HQ 1|2:21:6:23,27  2|1:2:0:18,2    2/2:35:4  
    20  1249593 .   T   .   47  PASS    NS=3;DP=13;AA=T GT:GQ:DP:HQ 0|0:54:7:56,60  0|0:48:4:51,51  0/0:61:2  
    20  1253923 microsat1   GTC G,GTCT  50  PASS    NS=3;DP=9;AA=G  GT:GQ:DP:AD 0/1:35:4:2,2    0/2:17:5:2,3    1/1:40:3:2,1  
    22  30025797    TR1 A   T   29  PASS    NS=3;DP=14;AF=0.5;DB;H2 GT:GQ:DP:HQ:AF  0|0:48:1:51,51:0    1|0:48:8:51,51:0.7  1/1:43:5:.,.:0.5  
    22  29050091    .   A   G   67  PASS    NS=2;DP=10;AF=0.333,0.667;AA=T;DB   GT:GQ:DP:HQ 1|0:21:6:23,27  0|0:2:0:18,2    1/1:35:4  
    22  40418496    TR3 T   C   3   q10 NS=3;DP=11;AF=0.017 GT:GQ:DP:HQ 0|0:49:3:58,50  0|1:3:5:65,3    0/0:41:3  
    22  40419252    .   C   T   47  PASS    NS=3;DP=13;AA=T GT:GQ:DP:HQ 1|0:54:7:56,60  0|1:48:4:51,51  0/0:61:2  
    12  122981745   TRI GGAAGAAGAA  G,GGAA,GGAAGAA  50  PASS    NS=3;DP=13;AA=T GT:GQ:HQ:AD 0|1:48:51,51:3,1    1|2:21:23,27:2,4    3|1:48:51,51:3,5

CRAVAT Input Format
===================

OpenCRAVAT currently supports two input formats: CRAVAT format and VCF.
The current version of OpenCRAVAT provides mappings and annotations
based on the human genome reference sequence GRCh38. There is a feature
in the OpenCRAVAT program to automatically convert hg18 or hg19 input
files into GRCh38 coordinates.

The basic CRAVAT variant input file is a tab separated text file. Each
row in a describes a genomic variant by the following sequential
columns: Chromosome, Position, Strand, Reference-Base, Alternate-Base,
[Sample], [Tags]. The table below describes each field:

Columns
-------

+---------+--------------+----------+
| Column  | Description  | Example  |
+=========+==============+==========+
| Chromos | The          | ``'chr22 |
| ome     | chromosome,  | '``,     |
|         | prefixed     | ``'chrX' |
|         | with         | ``       |
|         | ``'chr'``.   |          |
+---------+--------------+----------+
| Positio | The          | 11250130 |
| n       | numerical    | 7,       |
|         | position of  | 1804372  |
|         | the          |          |
|         | nucleotide   |          |
|         | along the    |          |
|         | chromosome   |          |
|         | transcript.  |          |
+---------+--------------+----------+
| Strand  | The strand   | ``'+'``, |
|         | the variant  | ``'-'``  |
|         | is on.       |          |
|         | Either       |          |
|         | ``'+'`` or   |          |
|         | ``'-'``.     |          |
+---------+--------------+----------+
| Referen | The          | ``'G'``, |
| ce-Base | reference    | ``'AG'`` |
|         | nucleotide,  | ,        |
|         | or a ``'-'`` | ``'TTCC' |
|         | for an       | ``,\ ``' |
|         | insertion.   | -'``     |
|         | Can be left  |          |
|         | empty for    |          |
|         | substitution |          |
|         | if reference |          |
|         | is unknown   |          |
+---------+--------------+----------+
| Alterna | The          | ``'A'``, |
| te-Base | alternate    | ``'TTC'` |
|         | nucleotide,  | `,       |
|         | or ``'-'``   | ``'-'``  |
|         | for a        |          |
|         | deletion.    |          |
+---------+--------------+----------+
| Sample  | Optional:    | ``'s1'`` |
|         | Sample       | ,        |
|         | identifier   | ``'s25'` |
|         | for cohort   | `        |
|         | studies.     |          |
+---------+--------------+----------+
| Tags    | Optional:    | ``'var00 |
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

Note if you wish to include tags but not sample ids, an extra tab
character is needed between the alternate base and tag.

OpenCRAVAT processes a list of unique variants extracted from the input
file. If the same variant is present in multiple samples, the variant
will be presented as a single line in the results but the sample and
mapping information can be used to identify all of the samples and
original input lines associated with a line in the output.

Example
-------

The following is a basic example of a CRAVAT input file:

.. code:: txt

    chr2    112501307   +   C   A  var001
    chr14   104770363   +   T   A  s1 var002
    chrX    71127984    +   A   G  s2 var003;control
    chr14   91974629    +   T   G  s1 var004;test
    chr12   57094662    +   G   T  s1 var005

The fields in the above sample must be tab delimited and may not get
tabs if you copy / paste it.

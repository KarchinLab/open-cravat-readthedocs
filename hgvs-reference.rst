Getting Started with HGVS in OpenCRAVAT
============

OpenCRAVAT now supports HGVS as an input type for annotation. To get
started, you just need to install the HGVS converter module:

``oc module install hgvs-converter``

The HGVS converter uses the `python hgvs <https://hgvs.readthedocs.io/en/stable/>`_ 
package and the `cdot <https://github.com/SACGF/cdot>`_ data source to convert 
HGVS strings to genomics coordinates, which are then annotated by OpenCRAVAT. To 
reduce the installation requirements of this feature, the HGVS converter utilizes
a proxy API hosted by OpenCRAVAT to do the conversion, so *you need an active 
internet connection to run this converter.*

HGVS File Format
--------------------

To run a job with HGVS input, you need to create an input file in our HGVS file format.
This file should be plain-text with one HGVS string per line. Optionally, you can add
tab-separated columns for a sample identifier and tags. Comment lines can be added with
a # symbol at the beginning of the line. See the example file below:

::

        ## HGVS input format
        # One HGVS string per line
        # Optional tab-separated values for sample and tags, sample MUST come first and tags second.
        # Comment lines must start with a # symbol

        NM_004006.2:c.4375C>T   s0  tag
        ENST00000536005.7:c.145C>T  s1  ensembl,bean1
        NM_177402.5:c.1197C>T   s0  more,tags

Once you have an HGVS file, you can run a job like normal:

``oc run input.hgvs -l hg38``

GUI Usage
--------------------

The HGVS converter can also be used with the :doc:`GUI <5.-GUI-usage>`. Simply go to the
store page, search for 'HGVS' and install the HGVS Converter. Then from the Jobs page, 
select your HGVS input file and annotate!

HGVS support has also been added for the :doc:`Single Variant Page <OpenCRAVAT-Variant-Report>`.




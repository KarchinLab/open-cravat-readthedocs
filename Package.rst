=======
Package
=======

``Package`` is a module which defines module installation and job parameters. For example, if you use the below process often:

- Install ClinVar and COSMIC modules.
- Annotate with ClinVar and COSMIC modules.
- Collect missense mutations only.
- Make VCF-format reports.

This process can be defined in a package module and you can tell OpenCRAVAT to do exactly the same process by giving the package's name to OpenCRAVAT as an option.

Making a Package
~~~~~~~~~~~~~~~~~~~~~~~

A package is a regular OpenCRAVAT module. In your OpenCRAVAT modules directory (you can find it with ``oc config md``), make ``packages`` 
if it does not exist, and then create a package directory with a package name of your choice (should be unique among all modules) under the ``packages`` directory
(for example, ``mypackage``). Then, create a .py and a .yml file with the package name. For example,

.. code:: text

 OpenCRAVAT modules directory/
 |
 +- packages/
    |
    +- mypackage/
       |
       +- mypackage.py
          mypackage.yml

The .py file can be empty and is not used by OpenCRAVAT, but it needs to exist for administrative purposes. 
The .yml file defines the dependency and process of the package. An example of ``mypackage.yml`` is below.

.. code:: yaml

 title: Allele Frequency Package
 description: Population allele frequency package with 1000 Genomes, ESP6500, gnomdAD, and gnomAD3
 type: package
 version: 0.0.1
 # Modules for this package
 requires:
 - thousandgenomes
 - esp6500
 - gnomad
 - gnomad3
 # oc run and oc report settings
 run:
     # Annotators
     annotators:
     - thousandgenomes - esp6500
     - gnomad
     - gnomad3
     # Reports
     reports:
     - vcf
     # Filters
     filtersql: >
       (
         (v.base__so = 'IND')
         or
         (v.base__so = 'INI')
         or
         (v.base__so = 'MIS')
       )
       and
       (g.base__hugo = 'BRAF')
     includesample:
     - sample1
     excludesample:
     - sample2

Yon can use a package as an option to ``oc run`` and ``oc report``.

Using a Package
~~~~~~~~~~~~~~~

Use ``--package`` option with ``oc run`` or ``oc report`` command to apply a package's settings to run a job or create a report. For example,

.. code:: sh

 oc run input --packge mypackage

This will run ``thousandgenomes``, ``esp6500``, ``gnomad``, and ``gnomad3`` annotator modules on ``input`` and create a VCF-format output file 
only with the variants that are in the gene ``BRAF``, produce either inframe insertion, inframe deletion, or missense protein sequence consequence, 
exist in ``sample1``, and do not exist in ``sample2``.

.. code:: sh

 oc report input.sqlite --package mypackage

This will create a VCF-format output file only with the variants, among the variants in ``input.sqlite``, 
that are in the gene ``BRAF``, produce either inframe insertion, 
inframe deletion, or missense protein sequence consequence, exist in ``sample1``, and do not exist in ``sample2``.

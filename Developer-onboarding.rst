===================
Devloper onboarding
===================

Introduction
------------

OpenCRAVAT is a python package that performs genomic variant interpretation including variant impact, annotation, and scoring. There is a web-based version of OpenCRAVAT (https://run.opencravat.org) but it can also be installed locally and is easy to integrate into bioinformatics pipelines. OpenCRAVAT has a modular architecture with a wide variety of analysis modules that can be selected and installed/run based on the needs of a given study. The modules are made available via the CRAVAT Store and are developed both by the CRAVAT team and the broader variant analysis community. OpenCRAVAT is a product of the Karchin Lab at Johns Hopkins University in collaboration with In Silico Solutions with funding provided by the National Cancer Institute's ITCR program.

An annotation for a particular variant is essentially a piece of extra information to accompany if in the output file. The codebase is open to published annotators – allowing you to pick and install your own annotators in a modular fashion. There are some “Base Components”  as well such as gene mapping and file conversion utilities. 

On the command line, all arguments begin with “oc” for OpenCRVAT. ``oc gui`` starts up the interactive interface, which will be pulled up in the default web browser. The command window that you run oc gui from will also show status of jobs in progress and processing of OpenCRAVAT.

CRAVAT github Projects
----------------------


1. open-cravat: This is the main project for running single user CRAVAT jobs.  For this project we work in branches and merge those branches to the master after testing and verification.

2. open-cravat-aux: This project supports the annotator store.  Work is done and checked in on the Master branch

3. open-cravat-multiuser:  This project is for the multiuser version of CRAVAT.  Work is done and checked in on the Master branch
 
Components required for job submission
--------------------------------------

* Genome: The first selection is reference genome (hg18, hg19, and hg38). This is an agreed upon genome that will be compared (referred) against when comparing a given individual’s genome.  The most common are h19 and h38, this information can often be found in the ##header lines of the VCF.  You must choose a reference to run a CRAVAT job.
* Variant File: Second selection is the variant file that you are going to process.  Variants are variations in one genome compared to a reference genome.  They can be: deletions, substitutions, or insertions. Variant files are supplied by the user and may be in various formats.  VCF is the most common format.
* Annotators: [optional] Outside vendor annotation tools.  They are added to a job to annotate the differences found between the reference and the comparator.  There are many annotators available within CRAVAT and they can be selected and installed within the tool from the “STORE” tab.  To use they must be installed within the users CRAVAT environment  AND selected for a given job.  Annotators get installed in the modules\ directory.
 
Building and deploying a local DEV instance of OpenCRAVAT
----------------------------------------------------------

1. Uninstall any previous version of OpenCRAVAT from your system, whether through pip or Mac/Windows installer.

2. Git pull the newest commits for the development branch

3. In the git directory for open-cravat, run pip install -e .

4. Run `oc module update`  This command will update the open-cravat modules in your local system with the newest version if available. 

5. Run `oc gui` to start up an interactive instance of OpenCRAVAT
 


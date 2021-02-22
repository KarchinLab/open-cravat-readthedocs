=============
Release notes
=============

2.2.2
=====

February 15, 2021

Core

- Filter performance has been improved by optimizing database queries.
- Annotation module's output can have table-format column values.
- Removed ``yarl`` dependency's version requirement.

GUI
- Module information dialog appears with mouse-over on a module name on the job submission page.
- Annotation modules are grouped by tags for easier navigation among them on the job submission page.
- Shows an ASCII banner with ``oc gui``.
- Fixed a bug on the module groups on the Store tab.

Modules
- Published a bug fix version of hg38.
- Published Aloft annotation module.
- Improved summary tab widgets.
- Updated ``clinvar_acmg`` annotation module.
- Updated ``pharmgkb`` annotation module.
- Updated the following annotation modules with table-format columns: ``cancer_hotspots``, ``cosmic``, ``cosmic_gene``, ``encode_tfbs``, ``interpro``, ``pharmgkb``, ``polyphen2``, and ``swissprot_ptm``.
- Updated the Protein Diagram widget (``wglollipop``) for better mapping among UniProt, TCGA, and user variants through canonical transcripts.
- Published PangaloDB annotation module.
- Published a rank score widget which will combine and show all the rank scores produced in the job.

Pipeline
- OpenCRAVAT Snakemake wrapper has been published.

Multi-user add-on
- "Try as Guest" feature with open-cravat-multiuser: Users can test OpenCRAVAT multi-user version without first creating an account. 
- Updated the login page design.

2.2.0
=====

December 10, 2020

Core 

- Improved format of ``oc module ls -a`` 
- ``oc module info`` with a non-existing module name will gracefully end. 
- Secondary input data will always be an empty list if it does not have any data. 
- ``oc store publish`` will ask for a password if missing. 
- ``pyvcf`` has been included in the installation requirement of OpenCRAVAT. 
- ``oc module install`` with a version number (``-v`` option) will skip installation if the same version of the requested module(s) already exists on the user's system. 
- Reporters are now not run by default unless ``reporter=`` option is defined in ``cravat.yml``. 
- Post-aggregators will be announced in the output of ``oc run`` only if they are run. 
- Fixed bugs related to doing ``oc run`` with an OpenCRAVAT result sqlite file. 
- An annotator can provide a list of supported chromosomes to the base annotator for more graceful handling of alternate chromosomes which the annotator does not cover. 
- ``oc run --silent`` will be more completely silent. 
- ``oc run`` with ``--mp`` option will enforce the correct number of processes for the gene mapper. 
- ``oc run`` and ``oc report`` can receive ``--concise-report`` option to tell reporters to produce reports only with the default columns defined by annotators. 
- Exact report file paths will be shown after ``oc report``. 
- The versions of OpenCRAVAT, gene mapper, annotators, and reporters will be written to job log files with ``oc run``. 
- ``oc run`` will stop if there is no valid input after the converter step. 
- Minor bug fixes.

GUI 

- Case-control analysis option has been added. 
- In the multi-user mode, temporary passwords will be randomly generated. 
- If a job result cannot be viewed, a more graceful message will be shown. 
- Minor bug fixes.

Result Viewer 

- Filters for a job can be exported into json files and then imported to another job's result with buttons on the Interactive Result Viewer.

Modules 

- ``casecontrol``, a case-control analysis module has been published.

2.1.1
=====

September 17, 2020

Core 

- OpenCRAVAT runs on Python 3.8 on Windows machines. 
- Improved the stability of downloading input files over the internet through ``oc run http://...``. 
- Better error message when a result database file does not exist. 
- Fixed a bug on converting the genomic positions the orientation of which is different between assemblies. 
- Fixed the number of unique input variants when multiple input files are given to ``oc run``. 
- Module-specific options can be given to converter modules through ``oc run``.

GUI 

- Result SQLite files can be imported into the job table on GUI. 
- Jobs can be deleted even when an interactive result viewer is open for the same job. 
- Improved the UI of the report download section in the job table.

Result Viewer 

- Fixed in-table, range and dropdown filters on result tables.

Modules 

- Fixed the handling of variants without any sample in VCF-format input files.

2.1.0
=====

August 18, 2020

Core 

- cravat.run\_reporter in Python scripts can be run with keyword arguments. 
- cravat.run and cravat.run\_reporter can be run inside Jupyter Notebook. 
- cravat.run and cravat.run\_reporter will return the output by reporter modules as a dictionary. 
- Filters can be applied through a command-line argument. 
- Indices for all smart filter columns will be added in each run. 
- Modules can be independently run and debugged. 
- Improved the speed of the runs with large input files in UTF-8 encoding.

GUI 

- Fixed race condition between loading and filtering variants on large jobs

Interactive Result Viewer 

- Improved the speed of opening the result viewer. 
- Improved the result table with scientific number notation and alignment of cell values.

2.0.1
=====

July 16, 2020

Core 

- System options can be given to ``oc run`` with ``--system-option`` option. 
- ``oc module install`` now has ``-f`` option to force install even if the same version exists. 
- ``oc module install-base`` will re-install any existing base modules.

2.0.0
=====

July 15, 2020

Modules 

- A new version of ``hg38`` mapper produces cDNA and protein sequence changes in HGVS format, annotates with non-coding transcripts, reports multiple sequence ontologies for each transcript, and uses MANE transcripts as primary transcript. 
- ``hgvs`` module is now deprecated since ``hg38`` includes HGVS-format cDNA and protein changes. 
- ``vest`` and ``wglollipop`` modules have been updated to work with the new version of ``hg38``. 
- ``vcfreporter`` can handle VCF format input files without samples.

Core 

- Improved the speed of report generation. 
- OpenCRAVAT jobs can be run within a Python shell in such a way as ``from cravat import Cravat; cv = Cravat(inputs=['example_input'], genome='hg19', annotators=['clinvar']); runner.run()``.
- Improved exception logging by converter modules. 
- Re-running a job will starts with converter and regenerates intermediate files. 
- ``oc module install`` shows timestamp with each message. 
- master converter fills in missing reference bases in input files. 
- ``oc run`` now rejects input files with space character in their paths. 
- URLs starting with ``http:`` or ``https:`` can be used as input for ``oc run``. 
- Module-specific options can be given to ``oc run`` with ``--module-option`` option. 
- ``oc run`` can accept input from PIPE.

GUI 

- Improved the start-up speed of the GUI by locally caching the web store data. 
- Settings menu has a button to update the web store cache.
- Job list shows job IDs and the number of unique input variants. 
-Job list provides a button for upgrading the job result database so that job results from older version of OpenCRAVAT can be opened.

Result Viewer 

- Long sample names are correctly shown on the filter tab. 
- Improved the UI for selecting and excluding samples in the filter tab. 
- Improved the speed of filtering with samples. 
- Fixed "Export" feature of variant and gene tab tables.

1.8.0
=====

April 27, 2020

Gene mapper 

- New hg38 mapper speeds up gene model mapping by an order and can utilize multiple cores.

cravat core 

- Fixed pyyaml warning message. 
- Entire ``oc run`` can be run within Python as ``import cravat; cravat.run()``.

GUI 

- Failure message from job submission is reported back to the browser. 
- Input file size can be limited by settings.

VCF support 

- Annotations in VCF format input files are transferred into OpenCRAVAT result database. 
- VCF format output has been improved for better readability.

1.7.1
=====

March 11, 2020

cravat core 

- Bugfix: when pip installed by root and run by a non-root user, don't attempt to write to logs owned by root

GUI 

- Bugfix: variant reports work when running in https

1.7.0
=====

February 5, 2020

Featured 

- Added the variant report page which can be linked with a URL for a single variant and which shows the OpenCRAVAT annotation on the given variant with graphics. 
- New command line schema which combines all of the cravat command universe into the top command ``oc`` and sub-commands.

cravat core 

- cravat can process gzipped input files. 
- cravat cleans up temporary files after a successful run by default. 
- cravat can receive a cravat run result database file and add more annotation to the result database. 
- Redundant bases in the reference and alternate bases are trimmed.

GUI 

- gzipped input files can be used for job submission. 
- Input files from multiple folders can be chosen on the job submission page.

Result viewer 

- Fixed the export of the result table so that the chromosome column correctly shows.

util 

- Added a utility which can migrate a job result database into a user's job list.

multiuser 

- Added the support for basic authentication.

1.6.1
=====

November 27, 2019

open-cravat-server

cravat core 

- cravat runs with multiple cores even when secondary input is used. 
- Default maximum number of concurrently running annotators is set to be the number of cores minus 1. 
- Fixed various minor bugs.

GUI 

- Default maximum number of concurrently running jobs is set to be 3. 
- Genome version should be selected at first. 
- Generating job result reports and opening job result can happen simultaneously. 
- Fixed various minor bugs.

1.6.0
=====

November 8, 2019

open-cravat-server 

- An add-on pip package `open-cravat-server <https://github.com/KarchinLab/open-cravat-server>`__ has been released for supporting multiple users in OpenCRAVAT web server.

cravat core 

- ``cravat-admin install/uninstall/update`` has ``-y`` option to bypass confirmation. 
- Modules can have a warning message regarding commercial usage. 
- ``cravat`` terminates if absent module(s) are requested for a run. 
- Improved memory usage of the input format converter step. 
- Supports simpler secondary module definition without match and use columns. 
- ``aggregator`` uses an injection-safe way to execute sqlite3 commands. 
- Genome assembly is now a mandatory option for running ``cravat``, but a default value can be set in cravat.yml. 
- Minor bug fixes

GUI 

- Added support for HTTPS connection. 
- Number of concurrently running jobs can be set on OpenCRAVAT web interface. 
- Number of concurrently running annotators per job can be set on OpenCRAVAT web interface. 
- Aborted jobs show as "Aborted" on the job list. 
- Shows a progress bar for the upload of input files while a job is submitted. 
- OpenCRAVAT web interface functions without internet connection (Web store will be disabled. Job submission and the result viewer will be functional). 
- GUI can be open with the root URL and port. 
- Minor bug fixes

Web API 

- Added web API for job submission, checking the status of submitted jobs, generating report files for jobs, checking the presence of report files for jobs, and downloading generated report files.

Result Viewer 

- Result viewer URL does not show the internal path to result databases. 
- Gene list of Smart Filter can have empty lines. 
- Minor bug fixes

1.5.3
=====

September 3, 2019

cravat core 

- In report generation for a job, the gene level annotators used for the job do not need to exist on the system.

Result Viewer 

- Fixed a bug where the result loading spinner does not disappear if the number of input variants is more than 100,000. 
- Fixed the table header filter for "Coding" column.

1.5.2
=====

August 29, 2019

cravat core

-  Added result database migration utility which upgrades the
   open-cravat result sqlite files to be readable by OpenCRAVAT 1.5.2.
-  Presence or absence of a module is more correctly detected.
-  When update of a module fails in the middle, the module is correctly
   detected as uninstalled.
-  If modules directory is gone, ``cravat`` and ``cravat-admin``
   notifies and interactively resolve the issue with user input.

cravat GUI

-  If modules directory is gone, ``wcravat`` notifies and handles
   gracefully so that a new modules directory can be entered or the
   missing one can be attached again.
-  Clearing browser cache is not needed anymore to reflect new versions.
-  More detailed job status in the job list is provided when converters,
   aggregators, and post-aggregators run.
-  Minor UI improvements and bug fixes

Web Store 

- Clearing browser cache is not needed anymore to reflect new versions.

Result Viewer

-  Clearing browser cache is not needed anymore to reflect new versions.
-  Minor UI improvements and bug fixes

Modules

-  VCF format reporter which preserves input files' annotation
   information
-  GWAS Catalog annotator
-  Improved 23andme and ancestrydna converters so that they fill in
   reference bases.
-  UI improvements of widgets
-  Minor bug fixes

1.5.1
=====

August 14, 2019

cravat core 

- ``cravat-admin info`` shows data source version for each module version, if available, as well as the current version. 
- ``cravat`` options changed: ``--startat`` for setting the starting stage, ``--endat`` for setting the ending stage, ``--repeat`` for setting the stage(s) to repeat, and ``--skip`` for setting the stage(s) to skip. 
- ``cravat`` can receive a job configuration file which can direct any argument which can be given with command-line. 
- Revampled how column definitions are handled internally. 
- Gene level annotation is added to variant level annotation. 
- Gene level aggregation is done dynamically with filters. 
- ``cravat --version`` and ``cravat-admin --version`` show the version of open-cravat. 
- ``cravat-admin ls`` shows module titles. 
- ``cravat-admin info`` shows the explanation on module output columns as well as release note.

cravat GUI 

- Revampled the interface. 
- Annotation modules can be viewed and selected in groups and categories. 
- Connection to the server will not be lost even if the GUI browser tab is left open for a long time. 
- Fixed minor bugs.

Web Store 

- Revampled the interface. 
- Module detail panel shows required modules. 
- Fixed minor bugs.

Result Viewer 

- Revampled the interface. 
- Added Sample Filter which can filter with inclusion and exclusion of samples. 
- Added Gene Filter which can accept a list of HUGO symbols and filter the result with it.
- Added Smart Filter which can filter multiple columns with one selection. 
- Added Query Builder with which complex custom filters can be built. 
- Widget content can be exported to a png file. 
- Widgets can hide themselves if there is no data for them. 
- Module group names have tooltips which explains the modules. 
- Added module group context menu. 
- Module groups are alphabetically sorted. 
- Table export button will export what is shown and with load and table filter information. 
- A module can have a default set of columns to show, and the Result Viewer has small buttons in the header for each module for expanding, collaping, and bringing back to the default of the columns of the module. 
- Fixed minor bugs.

Modules 

- Added VCF format reporter which can preserve the annotations in the input VCF format file.

1.4.5
=====

July 16, 2019

-  Fix for bug preventing submission of multiple input files.

1.4.4
=====

June 17, 2019

Installers 

- The Mac installer is now a signed package installer.

cravat core 

- In Windows, Mac OS, and Linux, different default folders for modules, jobs, and configuration files are used to better suit their native folder architecture. 
- Python requirement has been increased to

Python 3.6 or higher. 

- Log file has non-redundant exception messages for better readability. 
- Record of annotation modules are correctly kept with multiple cravat runs on the same input. 
- For a job with multiple input files, output file names start with the first input file name plus \_and\_x\_files, where x is the number of input files minus 1.

cravat GUI 

- Job list is automatically updated when there are running jobs. 
- Running jobs can be cancelled from the GUI. 
- Warns if a job has more input lines than specified in Settings. 
- GUI remembers genome assembly selection. 
- Variout user interface improvements 
- Fixed various bugs.

Web Store 

- Module installation can be cancelled from the GUI. 
- Shows module group, a collection of the varieties of a module. 
- Warns with total size of installation for collective installation or update. 
- Module tile shows their module types if they are not annotation modules.

Result Viewer 

- hg19 and tagsampler results show next to Variant Annotation columns. 
- Less-informative widgets are hidden by default.

Modules 

- Protein Diagram widget on gene tab shows all variants for a gene on a table, whose rows when hovered will highlight corresponding variants on the protein diagram. 
- 1000 Genomes module group and CHASMplus module group have been published. 
- Comma-delimited format reporter and tab-delimited format reporter have been published.

1.4.3
=====

April 30, 2019

GUI 

- Improved the launch speed. 
- Detects the absence of the server and prevents further operation. 
- Multiple open-cravat GUI browser tabs work properly with install/update.

Web Store 

- Prevents installation/update of modules if free disk space is not enough.

1.4.2
=====

April 19, 2019

Installers 

- Releasing Windows and Mac installers. No more pip installation is needed if these installers are used.

cravat core 

- cravat can process multiple vcf-format input files at once. 
- cravat better handles status and error logging. 
- Annotation modules run in multiple execution of cravat with the same input are accummulatively logged in the job status file for the input.

cravat GUI 

- open-cravat command-line terminal can be launched from the GUI.

Web Store 

- Improved launch speed. 
- Fixed alphabetical name sorting of modules.

Result Viewer 

- Simplified and improved the default settings of the basic load-filter. 
- Added context menu to the column groups for each module on the result tables. 
- Improved the layout and user experience of the table columns and widgets. 
- Improved launching speed. 
- hg19 coordinates, samples, and tags appear right next to Variant Annotation columns. 
- Summary widgets without any result will hide themselves. 
- Fixed wrong drag-and-drop of column headers

Modules 

- Improved the speed of REVEL module. 
- Smarter detection of vcf input format (vcf-converter)

1.4.1
=====

March 21, 2019

Result Viewer 

- Revamped the Summary tab. 
- Fixed the load filter for the cases where samples were searched with "not". 
- Added context-menu to the result table columns. 
- Result table cell value area can be expanded to display large text strings. 
- Columns of the result table can no longer be nested in another column group. 
- Added new help dialog functionality for each widget (e.g. IGV widget). 
- Fixed issues with browser zoom. 
- Bug fixes

CRAVAT web GUI 

- Added functionality to navigate between different module dialogs in store using arrow keys. 
- Decluttered the interface of the web store by completely hiding base components. 
- Added separate input examples for hg18, hg19, and hg38. 
- Module detail panel in web store describes the output columns of the shown module. 
- Updated look and feel of the web submit and the web store. 
- Bug fixes

cravat 

- Dependencies (between modules and between open-cravat and modules) are resolved before module installation and update. 
- Decluttering of the log file for better readability. 
- Each run creates an .err file which explicitly reports each variant with an error. 
- Added the capability of cravat-admin to privately publish modules.

Others 

- Added web links to the ID columns of Clinvar, COSMIC, dbSNP, UniProt, and denovo-db. 
- Improved the default column size and widget layout for several modules.

1.3.2
=====

January 31, 2019

Updates on Interactive Result Viewer (cravat-view): 

- Data loading indicator 
- Local filter select box 
- Show-all and hide-all buttons for widgets 
- Load filter of cravat-view now has two modes, simple and advanced, and it shows only the filter operators relevant to the type of the filtered data. 
- Widgets can be hidden by default and its show/hide status can be saved and loaded.

Updates on cravat web GUI (wcravat): 

- Store now has a Front Page with Most Downloaded and Newest modules. 
- Store shows annotator modules' source data version for provenance. 
- Store can sort modules by their name, size, and date of post.

Updates on cravat: 

- cravat detects input files’ encoding and reads them correctly and writes output files always in UTF-8.

Others: 

- Module updates have been concurrently released. 
- Fixed various bugs.

1.3.1
=====

January 10, 2019

Patch release for bugs: 
- Fixed bug that prevented excel spreadsheet download in the wcravat jobs page. 
- Handle summary widget issues so that results will still be presented (filters on some jobs locking up results). 
- wcravat server stops cleanly with cntrl-C. 
- Updated Mac and Linux install instructions. 
- Fixed favicon.ico error on Chrome. 
- cravat detects and reads input files according to their encoding and always writes in UTF-8 across platforms.

1.3.0
=====

January 5, 2019

Improvements in wcravat, the web interface of open-cravat: 

- Revamped its design for a more modern look and better user experience. 
- Added job detail panel on the job list with various information on each job. 
- Added a button on the job list to view a job's log file. 
- Added a settings menu icon so that changing system setting is more convenient and safer. 
- Improved speed by eliminating synchronous web calls. 
- Implemented the check and prevention of redundantly running wcravat. 
- Fixed minor bugs.

Improvements in cravat-view: 

- Improved the user interface and the performance of the load and in-table filters. 
- Improved the layout save and load feature so that table columns' shown/hidden status is also saved and loaded. 
- Improved the opening time for large jobs 
- Improved the layout so that smaller screens display the result viewer well. 
- Improved speed by eliminating synchronous web calls. 
- Improved the readability of numbers in widgets by using 4 digits after the decimal point as the default. 
- Added selection boxes for filtering module output columns with "category" property set. 
- Fixed minor bugs.

Improvements in cravat: - Improved the column header, size, and
shown/hidden setting for each output column of all current annotator
modules. - "Category" property option has been added to the definition
of output columns of annotator modules. - One log file is produced for a
whole cravat run instead of one log file for each module. - Job status
and job information files are now one job status file. - Aggregator has
been included in the core package. - Fixed a bug which prevented using
secondary input source with multiprocessing. - Fixed minor bugs.

Improvements in modules (get them with cravat-admin install or wcravat's
Store): 

- Added Mutation Assessor annotation module (mutation\_assessor). 
- Added FATHMM annotation module (fathmm). 
- Added PhyloP annotation module (phylop). 
- Added phastcons annotation module (phastcons). 
- Added RVIS annotation module (rvis). 
- Added GHIS annotation module (ghis). 
- Added ExAC gene annotation module (exac\_gene). 
- Added Essential genes annotation module (ess\_gene). 
- Added GTEx annotation module (gtex). 
- Added UK10K Cohort annotation module (uk10k\_cohort). 
- Added Gerp++ annotation module (gerp). 
- Added LoFtool annotation module (loftool). 
- Improved ClinVar annotation module (clinvar). 
- Added new sequence ontology codes and display names to hg38 mapper module (hg38). 
- Added the functionality of handling empty reference bases to hg38 mapper module (hg38). 
- Improved VEST widget module (wgvest). 
- Fixed bugs in GRASP annotator module (grasp).
- Fixed Sequence Ontology Sample Summary widget module (wgsosamplesummary).

0.0.140
=======

December 5, 2018 

- Annotators run in parallel for faster analysis (# cores - 1 by default) 
- 'New' Icon when updates available for installed modules in CRAVAT Store 
- Protein Change column (base information) 
- Sequence Ontology - Codes translated to full terms (e.g. missense rather than MIS) 
- Selected Row Highlighted 
- New 'QuickSave" button on top right saves current filter and layout for when results are next opened.
- Fix so applying filter does not remove loaded IGV tracks 
- Filter panel fixes. 
- Consolidated Error Log

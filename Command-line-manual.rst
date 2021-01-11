===================
Command line manual
===================

The root command ``oc`` is used in combination with several keywords to
run OpenCRAVAT on the terminal.

+------------+------------------------------------------+
| Option     | Description                              |
+============+==========================================+
| -h         | Shows help message.                      |
+------------+------------------------------------------+
| run        | Run a job                                |
+------------+------------------------------------------+
| report     | Generate a report from a job             |
+------------+------------------------------------------+
| gui        | Start the GUI                            |
+------------+------------------------------------------+
| module     | Change installed modules                 |
+------------+------------------------------------------+
| config     | View and change configuration settings   |
+------------+------------------------------------------+
| new        | Create new modules                       |
+------------+------------------------------------------+
| store      | Publish modules to the store             |
+------------+------------------------------------------+
| util       | Utilities                                |
+------------+------------------------------------------+
| version    | Show version                             |
+------------+------------------------------------------+
| feedback   | Send feedback to the developers          |
+------------+------------------------------------------+

oc run | Run a job
===================

Positional argument: input - Input file(s). One or more variant files in
a supported format.

+------------+------------------------------------------+
|Optional arguments: |Option|Description|
|--------|---------------------------------| | -h, --help | show
this help message and exit| | -a ANNOTATORS [ANNOTATORS ...]. |
annotators to run| | -e EXCLUDES [EXCLUDES ...] | annotators to
exclude| | -n RUN\_NAME | name of cravat run| | -d OUTPUT\_DIR |
directory for output files| | --startat [STAGE] | starts at given
stage {converter,mapper,annotator,aggregator,postaggregator,reporter}|
| --repeat [STAGE] | forces re-running of given stage if it is in the
run chain.
{converter,mapper,annotator,aggregator,postaggregator,reporter}| |
--endat [STARGE] | ends after given
stage.{converter,mapper,annotator,aggregator,postaggregator,reporter}|
--skip [STAGE] | Skips given stage(s).
{converter,mapper,annotator,aggregator,postaggregator,reporter}| | -c
CONF | path to a conf file| | --cs CONFS | configuration string| |
-v | verbose| | -t {excel,tsv,vcf,text,csv} |
[{excel,tsv,vcf,text,csv} ...] report types. If omitted, default one in
cravat.yml is used.| | -l {hg38,hg19,hg18} | reference genome of
input. CRAVAT will lift over to hg38 if needed.| | -x | deletes the
existing result database and creates a new one.| | --newlog | deletes
the existing log file and creates a new one.| | --note NOTE | note
will be written to the run status file | | --mp MP | number of
processes to use to run annotators | | -i {cravat,vcf,oldcravat}, |
--input-format {cravat,vcf,oldcravat} Force input format| |
--temp-files | Leave temporary files after run is complete.| |
--writeadmindb | Write job information to admin db after job
completion| | --jobid JOBID | Job ID for server version| |
--version | Shows open-cravat version.| | --separatesample |
Separate variant results by sample|


report | Generate a report from a job
======================================

oc report is used to generate output reports

Positional argument: dbpath - Path to aggregator output

+------------+------------------------------------------+
|Optional arguments: |Option|Description|
|--------|---------------------------------| | -h, --help | show
this help message and exit| | -t [FORMAT] | report types,
{excel,csv,tsv,text,vcf}| | -f FILTERPATH | Path to filter file| |
-F FILTERNAME | Name of filter (stored in aggregator output)| | -s
SAVEPATH | Path to save file| | -c CONFPATH | path to a conf file|
| --module-name MODULE\_NAME | report module name| |
--nogenelevelonvariantlevel | Use this option to prevent gene level
result from being added to variant level result.| | --confs CONFS |
Configuration string| | --inputfiles INPUTFILES [INPUTFILES ...] |
Original input file path| | --separatesample | Write each
variant-sample pair on a separate line| | -d OUTPUT\_DIR | directory
for output files|


gui | Start the GUI
====================

Positional argument: result - Path to a CRAVAT result SQLite file

+------------+------------------------------------------+
|Optional arguments: |Option|Description|
|--------|---------------------------------| | -h, --help show this
help message and exit| | --multiuser | Runs in multiuser mode| |
--headless | do not open the cravat web page| | --http-only | Force
not to accept https connection| | --debug | Console echoes exceptions
written to log file|


module | Change installed modules
==================================

View, install, inspect, and uninstall modules

+------------+------------------------------------------+
|Commands: |Command|Description|
|--------|---------------------------------| | ls | List modules|
| install | Install modules| | uninstall | Uninstall modules| |
update | Update modules| | info | Module details| | install-base
| Install base modules|


config | Configuration settings
================================

View and change configuration settings

+------------+------------------------------------------+
|Commands: |Command|Description|
|--------|---------------------------------| | md | Change modules
directory| | system | Show system config| | cravat | Show cravat
config|


new | Create new modules
=========================

Create new annotator, and generate an example input file.

+------------+------------------------------------------+
|Commands: |Command|Description|
|--------|---------------------------------| | example-input | Make
example input file| | annotator | Create new annotator|


store | Publish modules to the store
=====================================

Publish modules to the store

+------------+------------------------------------------+
|Commands: |Command|Description|
|--------|---------------------------------| 
|publish|Publish a module| 
|new-account|Create an account| 
|change-pw|Change password| 
|reset-pw|Request password reset| 
|verify-email|Request email verification| 
|check-login|Check login credentials|
+------------+------------------------------------------+

util | Utilities
=================

Utilities to test modules, update results databases, and send command
line jobs to the GUI.

+------------+------------------------------------------+ 
|Commands: |Command|Description|
|--------|---------------------------------| 
| test| Test installed modules| 
| update-result| Update old result database to newer format| 
| send-gui| Copy a command line job into the GUI submission list|
+-----------------+----------------------+---------------+

version | Show version
=======================

``oc version`` displays the currently installed version of OpenCRAVAT

feedback | Send feedback to the developers
===========================================

``oc feedback`` opens the GitHub issues tracker at
https://github.com/KarchinLab/open-cravat/issues.

1.7.0 Command Deprecation
=========================

OpenCRAVAT 1.7.0 introduced a single command tree, ``oc``, which
centralizes functions that previously were spread across possible
through multiple command line tools: ``cravat``, ``wcravat``,
``cravat-admin``, ``cravat-report``, ``cravat-test``, and
``cravat-util``. The table below maps old commands to the ``oc`` tree.
Users are encouraged to shift to using ``oc``. Old root commands will be
deprecated in a later version.

+-----------------+----------------------+--------------------------+
| Old Program     | Command              | New Command              |
+=================+======================+==========================+
| cravat          |                      | oc run                   |
+-----------------+----------------------+--------------------------+
| wcravat         |                      | oc gui                   |
+-----------------+----------------------+--------------------------+
| cravat-view     |                      | oc gui job.sqlite        |
+-----------------+----------------------+--------------------------+
| cravat-report   |                      | oc report                |
+-----------------+----------------------+--------------------------+
| cravat-admin    | md                   | oc config md             |
+-----------------+----------------------+--------------------------+
|                 | install-base         | oc module install-base   |
+-----------------+----------------------+--------------------------+
|                 | install              | oc module install        |
+-----------------+----------------------+--------------------------+
|                 | update               | oc module update         |
+-----------------+----------------------+--------------------------+
|                 | uninstall            | oc module uninstall      |
+-----------------+----------------------+--------------------------+
|                 | info                 | oc module info           |
+-----------------+----------------------+--------------------------+
|                 | publish              | oc store publish         |
+-----------------+----------------------+--------------------------+
|                 | create-account       | oc store new-account     |
+-----------------+----------------------+--------------------------+
|                 | reset-password       | oc store reset-pw        |
+-----------------+----------------------+--------------------------+
|                 | verify-email         | oc store verify-email    |
+-----------------+----------------------+--------------------------+
|                 | check-login          | oc store check-login     |
+-----------------+----------------------+--------------------------+
|                 | make-example-input   | oc new example-input     |
+-----------------+----------------------+--------------------------+
|                 | new-annotator        | oc new annotator         |
+-----------------+----------------------+--------------------------+
|                 | report-issue         | oc feedback              |
+-----------------+----------------------+--------------------------+
|                 | show-system-conf     | oc config system         |
+-----------------+----------------------+--------------------------+
|                 | show-cravat-conf     | oc config cravat         |
+-----------------+----------------------+--------------------------+
|                 | version              | oc version               |
+-----------------+----------------------+--------------------------+
| cravat-test     |                      | oc util test             |
+-----------------+----------------------+--------------------------+
| cravat-util     |                      | migrate-result           |
+-----------------+----------------------+--------------------------+

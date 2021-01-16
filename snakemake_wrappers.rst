.. role:: raw-latex(raw)
   :format: latex
..

=============================
OpenCRAVAT Snakemake Wrappers
=============================

OpenCRAVAT snakemake wrappers enable using OpenCRAVAT in Snakemake pipelines. The wrappers are currently being included in the Snakemake wrapper repository, but meantime you can get the wrappers from `open-cravat-snakemake-wrappers.tar.gz`.

Requirements
------------

OpenCRAVAT should already be installed in your system.

Installation
------------

Decompress `open-cravat-snakemake-wrappers.tar.gz`, which will produce `open-cravat-snakemake-wrappers` folder. In it, there will be two folders, `module` and `run`. In each of these two folders, there will be one copy of `wrapper.py` which is the Snakemake wrapper for installing OpenCRAVAT modules and for running OpenCRAVAT jobs, respectively (from now on, they will be called "module wrapper" and "run wrapper").

How to use the wrappers
-----------------------

Example Snakemake files are in module/test/Snakemake and run/test/Snakemake. They are good as templates for your own Snakemake files. Since OpenCRAVAT Snakemake wrappers are not in the Snakemake wrapper repository yet, URLs starting with `file:` should be used for `wrapper` directive.

The module wrapper installs OpenCRAVAT modules. `output` directive of a Snakemake rule should define the locations of the OpenCRAVAT modules to install. `directory` command should be used for module locations. For example, assuming that the module wrapper is at /home/user1/open-cravat-snakemake-wrappers/module/wrapper.py,
::
  rule module:
    output:
      directory("modules/annotators/biogrid")
    wrapper:
      "file:/home/user1/open-cravat-snakemake-wrappers/module/wrapper.py"

will install `biogrid` OpenCRAVAT annotation module in `modules/annotators/biogrid` relative to the current working directory.

The run wrapper runs an OpenCRAVAT job. An example Snakefile using this wrapper is below:
::
  rule run:
      input:
          'example_input',
          'modules/commons/hg38wgs',
          'modules/converters/cravat-converter',
          'modules/mappers/hg38',
          'modules/annotators/biogrid', 
          'modules/annotators/clinvar',
          'modules/postaggregators/tagsampler',
          'modules/postaggregators/varmeta',
          'modules/postaggregators/vcfinfo',
          'modules/reporters/excelreporter',
          'modules/reporters/tsvreporter',
          'modules/reporters/csvreporter',
      output:
          'example_input.xlsx',
          'example_input.variant.tsv', 
          'example_input.variant.csv'
      params:
          cores=1
      log:
          "logs/open-cravat/run.log"
      wrapper:
          'file:../wrapper.py'


`input` directive receives the paths to input files and the folders of the OpenCRAVAT modules to run. The run wrapper will parse them and automatically set up `oc run` command. `output` directive includes the paths to the output files to check, but it does not have to include all output files. `params` directive can have three keys: `genome`, `cores`, and `extra`. The value of `genome` key will be translated to `-l` option of `oc run`. The value of `cores` key will be translated to `--mp` option of `oc run`. All other parameters to `oc run` can be given under `extra` directive, as in `extra="--temp-files --silent"`. 

In the above example Snakefile, 10 modules are supposed to run. If these modules are not installed already, the module wrapper can be used to automatically install them before running the job, as shown below:
::
  rule run:
      input:
          'example_input',
          'modules/commons/hg38wgs',
          'modules/converters/cravat-converter',
          'modules/mappers/hg38',
          'modules/annotators/biogrid', 
          'modules/annotators/clinvar',
          'modules/postaggregators/tagsampler',
          'modules/postaggregators/varmeta',
          'modules/postaggregators/vcfinfo',
          'modules/reporters/excelreporter',
          'modules/reporters/tsvreporter',
          'modules/reporters/csvreporter',
      output:
          'example_input.xlsx',
          'example_input.variant.tsv', 
          'example_input.variant.csv'
      params:
          cores=1
      log:
          "logs/open-cravat/run.log"
      wrapper:
          'file:../wrapper.py'

  rule installmodules:
      output:
          directory('modules/commons/hg38wgs'), 
          directory('modules/converters/cravat-converter'), 
          directory('modules/mappers/hg38'), 
          directory('modules/annotators/biogrid'), 
          directory('modules/annotators/clinvar'),
          directory('modules/postaggregators/tagsampler'),
          directory('modules/postaggregators/varmeta'),
          directory('modules/postaggregators/vcfinfo'),
          directory('modules/reporters/excelreporter'),
          directory('modules/reporters/tsvreporter'),
          directory('modules/reporters/csvreporter'),
      log:
          "logs/open-cravat/module.log"
      wrapper:
          'file:../../module/wrapper.py'

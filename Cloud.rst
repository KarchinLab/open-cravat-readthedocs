===========
Cloud Usage
===========

Microsoft Azure 
---------------

We recommend selecting the F2s v2 virtual machine (VM) for small jobs, and F16s zV2 VM for heavier loads that include multiple samples with whole genome sequencing. 
After the VM is started, ssh into the VM and then run a few commands to install all necessary components: 

* To install OpenCRAVAT, run ``pip3 install open-cravat``

We recommend that users pull the store modules from Genomic Data Lake when running a VM on Azure, this dataset is a mirror of the store at https://store.opencravat.org and https://run.opencravat.org. To facilitate this, we provide a small script for pulling and downloading the relevant modules. 

* `Download azcopy <https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10>`__
* Determine the annotation and analysis modules that you’d like to download. View all available options with ``oc module ls -a`` 
* `Download the import_modules.py script <https://github.com/KarchinLab/open-cravat-aux/blob/master/azure/import_modules.py>`__, and place it in the same directory as azcopy 
* To run the script, type ``python3 import_modules.py module1 module2`` 

For more information, consult the genomicsnotesbooks guide to downloading specific databases and deploying a Data Science VM on Azure for OpenCRAVAT at https://github.com/microsoft/genomicsnotebook/blob/main/sample-notebooks/genomics-opencravat.ipynb


Amazon Web Services
-------------------

OpenCRAVAT is usable on Amazon Web Services in two ways. The first is an
AMI that contains an up to date version of the package and almost all
annotators. The second is a CloudFormation workflow which will use the
AMI to annotate variants in S3 buckets.

AMI
~~~

The AMI is a public community image in the us-east-1 region called
OpenCRAVAT-version (for example OpenCRAVAT-1.7.1). `Here is a
link <https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Images:visibility=public-images;search=OpenCRAVAT;sort=name>`__.


The AMI runs CentOS 7 and consists of two 300 GB volumes, a root/job
volume, and a data volume mounted at ``/mnt/ssd``. Log in as the default
user, ``centos``. Modules are located at ``/mnt/ssd/oc``, and config
files are at ``/usr/local/lib/python3.6/site-packages/cravat/conf``.

We recommend at least a 4 core, 4 GB machine. Expect to use
approximately 300 MB of ram per 1 million variants. OpenCRAVAT will run
faster with more cores, as certain parts of the annotation process are
parallel. Best performance is achieved by either using an Provisioned
IOPS SSD for the modules volume, or choosing an instance with an
ephemeral ssd and moving the modules to it.

CloudFormation
~~~~~~~~~~~~~~

`The OpenCRAVAT CloudFormation
template <https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=OpenCRAVAT&templateURL=http://opencravat.s3.amazonaws.com/cf/oc-cf.yml>`__
can be used to automatically annotate files in S3. When run, it will
create an analysis instance from the AMI, pull an input file from S3,
annotate it, and place the results in S3.

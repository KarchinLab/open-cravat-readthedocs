===========
Cloud Usage
===========

Microsoft Azure 
---------------

Thanks to our collaborators at `Microsoft Genomics <https://www.microsoft.com/en-us/genomics/>`__, it is fairly simple to get OpenCRAVAT up-and-running on Microsoft Azure. We recommend selecting the F2s v2 virtual machine (VM) for small jobs, and F16s zV2 VM for heavier loads that include multiple samples with whole genome sequencing. 
After the VM is started, ssh into the VM and then run a few commands to install all necessary components: 

* To install OpenCRAVAT, run ``pip3 install open-cravat``

We recommend that users pull the store modules from Genomic Data Lake when running a VM on Azure, this dataset is a mirror of the store at https://store.opencravat.org and https://run.opencravat.org. To facilitate this, we provide a small script for pulling and downloading the relevant modules. 

* `Download azcopy <https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10>`__
* Determine the annotation and analysis modules that you’d like to download. View all available options with ``oc module ls -a`` 
* `Download the import_modules.py script <https://github.com/KarchinLab/open-cravat-readthedocs/blob/18616edaf1c3aec0174d2d9c53d3d0d59131c7ac/files/import_modules.py>`__, and place it in the same directory as azcopy 
* To run the script, type ``python3 import_modules.py module1 module2`` 

For more information, consult the genomicsnotesbooks guide to downloading specific databases and deploying a Data Science VM on Azure for OpenCRAVAT at https://github.com/microsoft/genomicsnotebook/blob/main/sample-notebooks/genomics-opencravat.ipynb


Amazon Web Services
-------------------

CloudFormation
~~~~~~~~~~~~~~

`The OpenCRAVAT CloudFormation
template <https://oc-cloudform.s3.amazonaws.com/oc-cf-template.yml>`__
can be used to automatically annotate files in S3. When run, it will
create an analysis instance from the AMI, pull an input file from S3,
annotate it, and place the results in S3.

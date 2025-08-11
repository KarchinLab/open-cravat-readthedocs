HPC Cluster Usage
=========

Installation
--------

OpenCRAVAT is entirely contained within the python package. Your installation will likely depend on the policies of your cluster.

Data Management
----------------------------

By default, OpenCRAVAT will install modules in a directory created in the python pip installation. For multi-user systems this may be problematic when the data size is large.
It's recommended to move it to a location with enough storage space before installing modules. The directory OpenCRAVAT searches for modules can be controlled with the command ``oc config md <directory>``. 

Performance
--------------

Most of the OpenCRAVAT workload is spent querying data on disk. As a result, OpenCRAVAT performance depends strongly on disk latency and bandwidth. 
This can result in slow performance if the modules are located on a network location such as an NFS mount when OpenCRAVAT is running on a worker node. 
To avoid this, you can copy the modules onto a node-local storage before running the job. Talk to you system administrator about what directory to use for this.

In general the process will involve these steps

.. code:: bash

    # Get the default modules directory
    DefaultMD=$(oc config md)

    # Get the node-local storage location
    NodeMD="/scratch/job/ocmd"

    # Copy data to node-local storage
    rsync -a $DefaultMD $NodeMD

    # Point oc to the node-local storage
    oc config md "$NodeMD"

    # Run your job
    oc run input.txt

::
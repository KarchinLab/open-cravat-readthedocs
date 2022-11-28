===================
Metrics
===================

Since version 2.3.0, OpenCRAVAT gathers metrics about how users are interacting
with the system. These metrics are aggregated and reported back to our funders
to measure the usage of OpenCRAVAT. They are also used to better understand how
OpenCRAVAT is being used and how to improve it. No personally identifiable
information is gathered, and users may opt-out at any time.

What information is gathered
____________________________

Two general types of information are collected for each cravat annotation job. 

The first type is job information. This includes information such as what 
annotators were used, how many variants were in the job, which genome assembly 
was used, and how long the job took to run. No information about the variants is
collected.

The second type is machine information. This is information about the computer that ran the job.
It includes information such as the number of processors, amount of memory, and 
type of operating system. This also includes a unique ID for each computer. The ID is anonymous
and is persistent between jobs.

Example
_______

Here is an example of the data collected

::

	{
	"jobData": {
		"genome": "hg38",
		"resultModifiedAt": "2022/11/28 15:28:43",
		"numInputFiles": 1,
		"resultCreatedAt": "2022/11/28 15:28:43",
		"numVariants": 388,
		"ocVersion": "2.3.0",
		"converterFormat": "cravat",
		"primaryTranscript": "mane",
		"indexingRuntime": 0.002,
		"jobRuntime": 4.089,
		"success": "Finished Normally",
		"modules": {
		"mapper": {
			"runtime": 2.064,
			"name": "hg38",
			"version": "1.10.3"
		},
		"converter": {
			"runtime": 0.743,
			"name": "cravat"
		},
		"annotators": [
			{
			"name": "go",
			"version": "2022.11.01",
			"runtime": 0.024
			},
			{
			"name": "clinvar",
			"version": "2022.11.14",
			"runtime": 0.063
			}
		],
		"aggregator": {
			"variants": {
			"runtime": 0.02
			},
			"genes": {
			"runtime": 0.019
			},
			"samples": {
			"runtime": 0.009
			},
			"tags": {
			"runtime": 0.019
			},
			"total": {
			"runtime": 0.058
			}
		},
		"postaggregators": [
			{
			"name": "tagsampler",
			"version": "1.1.5",
			"runtime": 0.012
			}
		]
		}
	},
	"machineData": {
		"OS": "Linux",
		"OSVersion": "6.0.9-300.fc37.x86_64",
		"totalMemory": 33574010880,
		"availableMemory": 25785372672,
		"freeMemory": 9525465088,
		"amountRAM": 33574010880,
		"swapMemory": 50751070208,
		"numCPU": 16,
		"fileSystem": "btrfs",
		"machineId": "00000000-0000-0000-0000-e0d4e8a1bc92",
		"pythonVersion": "3.11.0"
		}
	}


Opting out
__________

Users can opt-out of metrics collection at any time from the GUI, command line,
or by editing a config file.

To opt-out from the GUI, click the three-line settings menu in the top right of
the submit screen. Then, un-check "Allow collection of CRAVAT metrics", and 
click "Save". You can opt back in by checking the box, then saving again.

To opt-out from the command line, run the command

::
	oc config metrics No

You can opt back in by changing "No" to "Yes"

To opt-out with a config file, first find your cravat-system.yml file. Run 
``oc config system``, the config file location will be in the first line. Then,
edit the ``cravat_metrics`` file to include the line
::

	cravat_metrics: false

You opt back in by changing "false" to "true".


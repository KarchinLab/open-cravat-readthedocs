==============
Large VCF Annotation
==============

For large, many-sample VCF inputs, 

- WGS studies often use down-stream tools which require VCF input
- The OpenCRAVAT SQLite output database format performs poorly with large sample counts

The ``vcfanno`` tool will directly annotate a typical BGZipped VCF file, and
produce a BGZipped output that can be indexed with ``tabix``.

Usage
=====

::

		usage: oc vcfanno [-h] [-a [ANNOTATORS ...]] [-t THREADS] [--temp-dir TEMP_DIR] [-o OUTPUT_PATH]
		                [--chunk-size CHUNK_SIZE]
		                input_path

	positional arguments:
		input_path

	options:
		-h, --help            show this help message and exit
		-a [ANNOTATORS ...], --annotators [ANNOTATORS ...]
		-t THREADS, --threads THREADS
		                      Number of CPU threads to use
		--temp-dir TEMP_DIR   Temporary directory for working files
		-o OUTPUT_PATH, --output-path OUTPUT_PATH
		                      Output vcf path (gzipped). Defaults to input_path.oc.vcf.gz
		--chunk-size CHUNK_SIZE
		                      Number of lines to annotate in each thread before syncing to disk. Affects
		                      performance.


Output Format
=============

Annotations are added to the INFO field of the VCF. OpenCRAVAT provided keys are in the format ``OC_AnnotatorName_AnnotationName``, for example a gnomAD4 allele frequency call would be ``OC_GNOMAD4_AF``. Further details of each annotation are in the vcf header.

Some annotations provided by OpenCRAVAT are either complex structured data, or free-form text. These types of data can make vcf files difficult to read or parse. To resolve this, OpenCRAVAT fields are encoded using `HTTP Percent-encoding <https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding>`_. Structured data is typically also `JSON encoded <https://json.org>`_. 

While this makes the data less human-readable, most users do not directly read large VCFs. These encoding schemes are widely used, and most programming languages have standard tools to decode them.

For example, the OC_ALL_ANNOTATIONS field for a missense variant that affects multiple transcripts is JSON encoded to

::
	
	{"RP1":[["P56715","p.Asn985Tyr","MIS","ENST00000220676.2","c.2953A>T"],["","","INT","ENST00000636932.1","c.787+4547A>T"],["","","INT","ENST00000637698.1","c.787+4547A>T"]]}

And then HTTP Percent-encoded

::

	%7B%22RP1%22%3A%5B%5B%22P56715%22%2C%22p.Asn985Tyr%22%2C%22MIS%22%2C%22ENST00000220676.2%22%2C%22c.2953A%3ET%22%5D%2C%5B%22%22%2C%22%22%2C%22INT%22%2C%22ENST00000636932.1%22%2C%22c.787%2B4547A%3ET%22%5D%2C%5B%22%22%2C%22%22%2C%22INT%22%2C%22ENST00000637698.1%22%2C%22c.787%2B4547A%3ET%22%5D%5D%7D
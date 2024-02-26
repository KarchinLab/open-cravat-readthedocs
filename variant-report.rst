=========================
Variant Report
=========================

The OpenCRAVAT Variant Report is an annotation viewer for a single variant.
It includes information from most OpenCRAVAT annotators. Because it requires most
annotators to be installed, it is not recommended to install it locally. Instead,
the Variant Report can be viewed on 
`run.opencravat.org <https://run.opencravat.org/webapps/variantreport/index.html>`_.

Adding a variant
________________

Variants can be viewed by inputing their chromosome, position, reference allele,
and alternate allele in the input fields at the top left of the page. Variants 
must be on the GRCh38/hg38 assembly. To convert variants from other assemblies,
we recommend `LiftOver <https://genome.ucsc.edu/cgi-bin/hgLiftOver>`_.

Using a URL
___________

Variants can also be directly linked. Simple include the allele infomation in
the URL according the the template.

``https://run.opencravat.org/webapps/variantreport/index.html?chrom=<Chromosome>&pos=<Position>&ref_base=<RefAllele>&alt_base=<AltAllele>``

The input fields in the page will be pre-filled with the variant from the URL.

`Click here for an example. <https://run.opencravat.org/webapps/variantreport/index.html?chrom=chr17&pos=39724004&ref_base=C&alt_base=G>`_

The direct links can be used to easily link to the Variant Report from other pages.

=========================
Single Variant Report
=========================

The OpenCRAVAT Single Variant Report is an annotation viewer for a single variant.
It includes information from most OpenCRAVAT annotators. It can be accessed by clicking
the **Single Variant** tab at the top of the submit page of the OpenCRAVAT GUI.
Because it requires most annotators to be installed, it is not recommended to run locally.
Local OpenCRAVAT installs include the **Single Variant** tab as well, which links to the
Single Variant Report hosted on run.opencravat.org.

The single variant page can also be opened directly at `this link <https://run.opencravat.org/webapps/variantreport/index.html>`_.

Adding a variant
________________

Variants can be entered using any of the following formats:

- **Genomic coordinates**: Enter the chromosome, position, reference allele, and
  alternate allele separated by spaces, tabs, colons, semicolons, or periods
  (e.g. ``chr1 11796321 G A``). For insertions, use ``-`` as the reference allele;
  for deletions, use ``-`` as the alternate allele.

- **HGVS notation**: Enter an HGVS ``c.`` or ``g.`` string
  (e.g. ``NM_000051.4:c.2413C>T``).

- **dbSNP rsID**: Enter an rsID (e.g. ``rs121913514``).

- **ClinGen Allele Registry ID**: Enter a ClinGen ID (e.g. ``CA10578967``).

Variants on the GRCh38/hg38 assembly are preferred. Variants on GRCh37/hg19 are
also accepted and will be automatically lifted over to hg38.

Using a URL
___________

Variants can also be directly linked by including the variant information as
query parameters in the URL.

**Genomic coordinates**

``https://run.opencravat.org/webapps/variantreport/index.html?chrom=<Chromosome>&pos=<Position>&ref_base=<RefAllele>&alt_base=<AltAllele>``

`Example: chr1 11796321 G A <https://run.opencravat.org/webapps/variantreport/index.html?chrom=chr1&pos=11796321&ref_base=G&alt_base=A>`_

**HGVS**

HGVS strings contain reserved characters and must be
`URL encoded <https://en.wikipedia.org/wiki/Percent-encoding>`_ before use in a URL.
Tools such as `URL Encoder <https://www.urlencoder.org/>`_ can help with this.

``https://run.opencravat.org/webapps/variantreport/index.html?hgvs=<HGVS_String>``

`Example: NM_000051.4:c.2413C>T <https://run.opencravat.org/webapps/variantreport/index.html?hgvs=NM_000051.4%3Ac.2413C%3ET>`_

**dbSNP rsID**

``https://run.opencravat.org/webapps/variantreport/index.html?dbsnp=<rsID>``

`Example: rs121913514 <https://run.opencravat.org/webapps/variantreport/index.html?dbsnp=rs121913514>`_

**ClinGen Allele Registry ID**

``https://run.opencravat.org/webapps/variantreport/index.html?clingen=<ClinGenID>``

`Example: CA10578967 <https://run.opencravat.org/webapps/variantreport/index.html?clingen=CA10578967>`_

The direct links can be used to easily link to the Single Variant Report from other pages.

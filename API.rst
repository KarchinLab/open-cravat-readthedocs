===
API
===

(OpenCRAVAT 1.6.0 feature)

OpenCRAVAT GUI supports web API for submitting a job, checking the
status of a job, creating a job report, and downloading a job report.
Examples below are in Python, using ``requests`` module. If you want to
try the examples, first open Python console and run the below and then
follow examples.

.. code:: python

    python
    f = open('test_input.txt', 'w')
    f.write('chr10 8055656 + A T s3 var001\n')
    f.close()
    import requests

Accessing API with multi-user OpenCRAVAT
========================================

The instruction above are based on OpenCRAVAT GUI run in the personal
mode. If OpenCRAVAT GUI is run with --server option (multi-user mode), a
session should be obtained and logged in first, as shown below. Then,
replace ``requests.get`` and ``requests.post`` in the examples on this
page with ``session.get`` and ``session.post``.\*\*

.. code:: python

    import requests
    import base64
    session = requests.Session()
    reply = session.get('https://run.opencravat.org/server/login', headers={'Authorization': 'Basic ' + base64.b64encode(b'USERNAME:PASSWORD').decode()})
    reply.json()
    'success'
    (Then, to log out from the session)
    reply = session.get('https://run.opencravat.org/server/logout')
    reply.json()
    'success'


Submitting a job
================

-  Method: POST
-  Location: /submit/submit
-  Consumes: Multipart/form-data
-  Produces: a JSON object, notable fields of which are as follows.

   -  status['status']: 'Submitted' for successful job submission
   -  id: job ID of the submitted job

-  Form data parameters:

   -  annotators: list. Annotation modules
   -  reports: list. Report types
   -  assembly: string. Genome assembly of input
   -  forcedinputformat: string. Input format
   -  note: string

-  File data: "file\_x" where x is a number from 0 should be used to
   enumerate input files. Multiple files can be submitted as one job.

Example:

.. code:: python

    r = session.post('https://run.opencravat.org/submit/submit', files={'file_0':open('test_input.txt')}, data={'options': '{"annotators": ["clinvar"], "reports": ["text"], "assembly": "hg38", "note": "test run"}'})
    r.json()
    {'orig_input_fname': ['test_input.txt'], 'assembly': 'hg38', 'note': 'test run', 'db_path': '', 'viewable': False, 'reports': ['text'], 'annotators': ['clinvar'], 'annotator_version': '', 'open_cravat_version': '', 'num_input_var': '', 'submission_time': '2019-11-19T14:57:21.502575', 'id': '191119-145721', 'run_name': 'test_input.txt', 'status': {'status': 'Submitted'}}
    job_id = r.json()['id']

Checking job status
===================

-  Method: GET
-  Location: /submit/jobs/JOBID/status (replace JOBID with the "id"
   value obtained from the response of the submission POST request.)
-  Produces: a JSON object, notable fields of which are as follows.

   -  status: string. Latest status update of the job. When the job
      finishes, it will be "Finished".

Example:

.. code:: python

    r = session.get('https://run.opencravat.org/submit/jobs/' + job_id + '/status')
    r.json()['status']
    "Finished"

Creating report files
=====================

-  Method: POST
-  Location: /submit/jobs/JOBID/reports/REPORTTYPE (replace JOBID with
   the "id" value obtained from the response of the submission POST
   request and REPORTTYPE with a report type string.)
-  Produces: string. "done" means normal return.

Example:

.. code:: python

    r = session.post('https://run.opencravat.org/submit/jobs/' + job_id + '/reports/vcf')
    r.json
    'done'

Checking report files available for download
============================================

-  Method: GET
-  Location: /submit/jobs/JOBID/reports
-  Produces: a JSON list with the report types the files for which are
   available for download

Example:

.. code:: python

    r = session.get('https://run.opencravat.org/submit/jobs/' + job_id + '/reports')
    r.json()
    ['text', 'vcf']

Downloading report files
========================

-  Method: GET
-  Location: /submit/jobs/JOBID/reports/REPORTTYPE (replace JOBID with
   the "id" value obtained from the response of the submission POST
   request and REPORTTYPE with a report type string.)
-  Produces: HTTP(S) response with a report file. See "Content-Type" in
   its headers for the type of the file and "Content-Disposition" for
   the filename of the file.

Example:

.. code:: python

    r = session.get('https://run.opencravat.org/submit/jobs/' + job_id + '/reports/vcf')
    r.text
    '##fileformat=VCFv4.2\n##OpenCRAVATFileDate=20191119\n##INFO=<ID=CRV,Number=A,Type=String,Description="OpenCRAVAT annotation. Format: base__note|base__coding|base__hugo|base__transcript|base__so|base__achange|base__all_mappings|base__numsample|base__samples|base__tags|clinvar__sig|clinvar__disease_refs|clinvar__disease_names|clinvar__rev_stat|clinvar__id Explanation: base__numsample=Number of samples which contain the variant.|base__samples=Samples which contain the variant.|base__tags=Variant tags from the input file.|clinvar__disease_refs=Disease reference numbers|clinvar__rev_stat=The level of review supporting the assertion of clinical significance">\n#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\ts3\n10\t8055656\t1\tA\tT\t.\t.\tCRV="chr10"|8055656|"A"|"T"||"Yes"|"GATA3"|"ENST00000379328.7"|"missense"|"M1L"|ENST00000346208.3:GATA3:P23771:missense:M1L:A1T&ENST00000379328.7:GATA3:(na):missense:M1L:A1T|1|"s3"|"var001"|||||\tGT\t1|1\n'

Getting annotation on one variant without submitting a job using OpenCRAVAT server's live annotation
====================================================================================================

-  Method: GET
-  Location: /submit/annotate
-  Parameters

   -  chrom: chromosome
   -  pos: position (1-based)
   -  ref\_base: reference base
   -  alt\_base: alternate base
   -  annotators: comma-delimited string of annotation module names

-  Produces: a JSON object with annotation result, which is organized by
   annotation module names as the first level key and column names as
   the second level key.

Example:

.. code:: python

    r=requests.get('https://run.opencravat.org/submit/annotate?chrom=chr1&pos=12777320&ref_base=G&alt_base=T&annotators=clinvar,dbsnp,exac_gene,go,rvis')
    r.json()
    {'clinvar': {'sig': '', 'disease_refs': '', 'disease_names': '', 'rev_stat': '', 'id': ''}, 'dbsnp': {'snp': 'rs112368379'}, 'exac_gene': {'exac_pli': 3.89692512946575e-06, 'exac_prec': 0.369464079984044, 'exac_pnull': 0.630532023090827, 'exac_nontcga_pli': 2.29346103558518e-06, 'exac_nontcga_prec': 0.28488011039975, 'exac_nontcga_pnull': 0.715117596139215, 'exac_nonpsych_pli': 2.04859216406268e-06, 'exac_nonpsych_prec': 0.250289965336068, 'exac_nonpsych_pnull': 0.749707986071768, 'exac_del_score': None, 'exac_dup_score': None, 'exac_cnv_score': None, 'exac_cnv_flag': None}, ..., 'crx': {'uid': 'noid', 'chrom': 'chr1', 'pos': 12777320, 'ref_base': 'G', 'alt_base': 'T', 'note': '', 'coding': 'Yes', 'hugo': 'PRAMEF12', 'transcript': 'ENST00000357726.4', 'so': 'synonymous', 'achange': 'A391A', 'all_mappings': '{"PRAMEF12":[["O95522","A391A","synonymous","ENST00000357726.4","G1173T"]]}'}}
    >>r=requests.get('https://run.opencravat.org/submit/annotate?chrom=chr7&pos=140753336&ref_base=A&alt_base=T')
    >>r.json()
    {"segway_kidney": {"fetal_kidney": "Transcribed"}, "segway_lung": {"fetal_lung": "Transcribed"}, "segway_muscle": {"fetal_muscle_trunk": "Transcribed", "skeletal_muscle_female": "Transcribed", "skeletal_muscle_male": "Quiescent"}, "segway_ovary": {"ovary": "Quiescent"}, "abraom": null, "biogrid": ..., "thousandgenomes": null, "thousandgenomes_ad_mixed_american": null, "thousandgenomes_african": null, "thousandgenomes_east_asian": null, "thousandgenomes_european": null, "thousandgenomes_south_asian": null, "vest": null, "crx": {"uid": "", "chrom": "chr7", "pos": 140753336, "ref_base": "A", "alt_base": "T", "note": "", "coding": "Yes", "hugo": "BRAF", "transcript": "ENST00000288602.10", "so": "missense", "achange": "V600E", "all_mappings": "{\"BRAF\":[[\"P15056\",\"V600E\",\"missense\",\"ENST00000288602.10\",\"T1799A\"]]}"}}


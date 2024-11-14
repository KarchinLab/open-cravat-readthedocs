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

    f = open('test_input.txt', 'w')
    f.write('chr10 8055656 + A T s3 var001\n')
    f.close()


Logging in
========================================

The instruction above are based on using the public OpenCRAVAT server
mode. If you are instead running against a personal instance of the OpenCRAVAT GUI, you can
skip this step and replace all mentions of ``session`` below with ``requests``. For example 
``session.get`` is replaced by ``requests.get``.

.. code:: python

    import requests
    import base64
    session = requests.Session()
    reply = session.get('https://run.opencravat.org/server/login', headers={'Authorization': 'Basic ' + base64.b64encode(b'USERNAME:PASSWORD').decode()})


Submitting a job
================

Submit a new input file for annotation.

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
    print(r.json())
    job_id = r.json()['id']

Checking job status
===================

Get the status of a job (in queue, running, finished, failed)

-  Method: GET
-  Location: /submit/jobs/<JOBID>/status (replace JOBID with the "id"
   value obtained from the response of the submission POST request.)
-  Produces: a JSON object, notable fields of which are as follows.

   -  status: string. Latest status update of the job. When the job
      finishes, it will be "Finished".

Example:

.. code:: python

    r = session.get('https://run.opencravat.org/submit/jobs/' + job_id + '/status')
    print(r.json()['status'])


Creating report files
=====================

Request a report of the annotated variants in one of the supported formats.

-  Method: POST
-  Location: /submit/jobs/JOBID/reports/REPORTTYPE (replace JOBID with
   the "id" value obtained from the response of the submission POST
   request and REPORTTYPE with a report type string.)
-  Produces: string. "done" means normal return.

Example:

.. code:: python

    r = session.post('https://run.opencravat.org/submit/jobs/' + job_id + '/reports/vcf')
    print(r.json)


Checking report files available for download
============================================

Check the completed reports for a job.

-  Method: GET
-  Location: /submit/jobs/JOBID/reports
-  Produces: a JSON list with the report types the files for which are
   available for download

Example:

.. code:: python

    r = session.get('https://run.opencravat.org/submit/jobs/' + job_id + '/reports')
    print(r.json())


Downloading report files
========================

Download a report containing annotated variants.

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
    wf = open('output.vcf','w')
    wf.write(r.text)
    wf.close()
    

Single variant annotation
====================================================================================================

Get annotation on a single variant as a json object. This endpoint does not require login.

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
    print(r.json())
    {'clinvar': {'sig': '', 'disease_refs': '', 'disease_names': '', 'rev_stat': '', 'id': ''}, 'dbsnp': {'snp': 'rs112368379'}, 'exac_gene': {'exac_pli': 3.89692512946575e-06, 'exac_prec': 0.369464079984044, 'exac_pnull': 0.630532023090827, 'exac_nontcga_pli': 2.29346103558518e-06, 'exac_nontcga_prec': 0.28488011039975, 'exac_nontcga_pnull': 0.715117596139215, 'exac_nonpsych_pli': 2.04859216406268e-06, 'exac_nonpsych_prec': 0.250289965336068, 'exac_nonpsych_pnull': 0.749707986071768, 'exac_del_score': None, 'exac_dup_score': None, 'exac_cnv_score': None, 'exac_cnv_flag': None}, ..., 'crx': {'uid': 'noid', 'chrom': 'chr1', 'pos': 12777320, 'ref_base': 'G', 'alt_base': 'T', 'note': '', 'coding': 'Yes', 'hugo': 'PRAMEF12', 'transcript': 'ENST00000357726.4', 'so': 'synonymous', 'achange': 'A391A', 'all_mappings': '{"PRAMEF12":[["O95522","A391A","synonymous","ENST00000357726.4","G1173T"]]}'}}
    r=requests.get('https://run.opencravat.org/submit/annotate?chrom=chr7&pos=140753336&ref_base=A&alt_base=T')
    print(r.json())
    {"segway_kidney": {"fetal_kidney": "Transcribed"}, "segway_lung": {"fetal_lung": "Transcribed"}, "segway_muscle": {"fetal_muscle_trunk": "Transcribed", "skeletal_muscle_female": "Transcribed", "skeletal_muscle_male": "Quiescent"}, "segway_ovary": {"ovary": "Quiescent"}, "abraom": null, "biogrid": ..., "thousandgenomes": null, "thousandgenomes_ad_mixed_american": null, "thousandgenomes_african": null, "thousandgenomes_east_asian": null, "thousandgenomes_european": null, "thousandgenomes_south_asian": null, "vest": null, "crx": {"uid": "", "chrom": "chr7", "pos": 140753336, "ref_base": "A", "alt_base": "T", "note": "", "coding": "Yes", "hugo": "BRAF", "transcript": "ENST00000288602.10", "so": "missense", "achange": "V600E", "all_mappings": "{\"BRAF\":[[\"P15056\",\"V600E\",\"missense\",\"ENST00000288602.10\",\"T1799A\"]]}"}}


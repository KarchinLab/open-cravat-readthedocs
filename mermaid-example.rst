=============================
Example
=============================


.. contents::
   :depth: 3
..

.. mermaid::

  flowchart TD
    L[Creating an OpenCRAVAT Account] --> A
    click L "#creating-an-opencravat-account-web"
    M[Installing OpenCRAVAT via Installer] --> N
    N["Install Annotators"] --> B
    click M "#installing-opencravat-via-installer-local"
    click N "#install-annotators-local"
    A[Browse and select annotators] --> B[Convert to Input File Format]
    click A "#browse-annotators-web"
    click B "#convert-to-input-file-format"
    B -->|Variant File Input| C[Submit Annotation Job]
    click C "#submit-annotation-job"
    C -->|Results|D["Filter Results"] --> E[Visualize Results]
    click D "#filter-results"
    click E "#visualize-results"

Creating an OpenCRAVAT Account (Web)
====================================

Let’s start out by creating an account on https://run.opencravat.org. If
your organization is running OpenCRAVAT locally, you will need to find
out the appropriate URL for the instance of OpenCravat.

Here’s the initial screen we’ll see when we go to
https://run.opencravat.org. You’ll click on the **Sign Up** Button to
create an account.

|image2| Enter your details in the form, and sign up. You’ll
automatically be signed into the interface and will be ready to go for
the next step.

|image3|

Now you’re ready to browse the `OpenCRAVAT
Store <#browse-annotators-web>`__ to look for annotators.

Installing OpenCRAVAT via Installer (Local)
===========================================

You can install OpenCRAVAT via the installers below:

Windows
-------

`Windows
installer <https://karchinlab.org/opencravat/installers/OpenCRAVAT-2.4.1.exe>`__

Windows Defender may indicate that it prevented an unknown application
from running. If so, click the ‘More’ link on the message and then
select ‘Run Anyway’. An “OpenCRAVAT” icon will be created on the Desktop
and the Start Menu.

MacOS
-----

.. youtube:: 6f5fB6fVdBs


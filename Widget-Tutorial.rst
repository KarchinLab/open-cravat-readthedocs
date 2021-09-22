===============
Widget tutorial
===============



Writing a Web Result Viewer Widget
==================================

To make a web result viewer widget, two kinds of files are required: .js
and .yml.

The naming convention for web result viewer widgets is to have ``wg``
prefix in front of the annotator the data of which the widget uses.
Thus, the name of a widget for ``clinvar`` annotator is recommended to
be ``wgclinvar``. If such a name has already been claimed, you can use
another name but keep the ``wg`` prefix.

The .yml file is a module config file. See the below example
(``wgclinvar.yml``).

.. code:: yml

    title: ClinVar
    version: 1.0.0
    type: webviewerwidget
    required_annotator: clinvar
    description: Clinvar webviewer widget
    developer:
      name: 'Rick Kim'
      organization: 'In Silico Solutions'
      email: 'rkim@insilico.us.com'
      website: 'http://www.insilico.us.com'
      citation: ''

All keys except ``required_annotator`` is the same as in the module
config file for an annotator. ``required_annotator`` specifies which
annotator's result is needed to feed the data to this widget.

When the web result viewer draws each widget, it passes three parameters
to a widget: ``div``: ``div`` element which wraps the widget content
``row``: array of annotation values for the clicked/selected row in the
variant- or gene-level result table ``tabName``: ``variant`` or
``gene``, showing which level result is being passed as ``row``

See the below example code from ``wgclinvar.js``.

.. code:: javascript

    widgetGenerators['clinvar'] = {
        'variant': {
            'width': 280, 
            'height': 80, 
            'function': function (div, row, tabName) {
                addInfoLine(div, row, 'Significance', 'clinvar__sig', tabName);
                addInfoLine(div, row, 'Diseases', 'clinvar__diseases', tabName);
                addInfoLine(div, row, 'Ref. Nums', 'clinvar__refs', tabName);
            }
        }
    }

``widgetGenerators['widget_name']`` should be used to wrap widget
construction codes. If the name of a widget is ``sample_widget``, the
code should have ``widgetGenerators['sample_widget']``. The javascript
code of all widgets will be stored in ``widgetGenerators`` object, with
each widget's name as a key. ``widgetGenerators['sample_widget']`` has
annotation levels as the first level keys. In the above example, it has
only ``variant`` key. This means that only the variant tab's detail
panel will call ``function`` part of ``variant`` part of
``widgetGenerators['clinvar']``.

For each level, three key-value pairs are required: ``width``,
``height``, and ``function``. For ``width``, use 280 as the smallest and
an increment of 300. For ``height``, use 80 as the smallest and an
increment of 100. These two will define the size of the widget.

``function`` builds the content of the widget. ``addInfoLine`` is a
convenience function you can use. It puts a div with the value of a
column from the given row with a title of your choice. The syntax of
this function is addInfoLine(div, row, ``title``, ``db_column_name``,
tabName) and change ``title`` and ``db_column_name``. ``db_column_name``
is the name of a column in the result sqlite3 file's ``variant`` or
``gene`` table, which is specified by ``tabName`` variable. The
convention for ``db_column_name`` is
``an annotator name + '__' + column name defined in the annotator's yml file``.

If an external script/library is needed, use ``$.getScript`` jQuery
function, as shown in the below example. Put this function at the top of
the code.

``$.getScript('/result/widgetfile/wgndex/cytoscape.js', function () {});``

Widgets will appear automatically on the tabs defined as top-level keys
of ``widgetGenerators[widgetName]``.
In the ClinVar widget code above, ``variant`` top-level key indicates that
this widget has content for the variant tab of the interactive result viewer,
and thus will appear in the widget area of the variant tab of the interactive
result viewer. The same applies to ``gene`` and ``summary`` levels, also. Thus,
to make a summary widget for example, the widget code should have 
``summary`` top-level key under ``widgetGenerators[widgetName]`` object, 
``function`` key under the `summary` key, and the actual function to make content
as the value for the ``function`` key. With this in mind, the ClinVar widget code
above will make more sense.

To test your new widget, make a job result file. For example,

.. code:: shell

    oc new example-input .
    oc run example_input -l hg38
    oc gui example_input.sqlite

Then, check the variant, gene, or summary tab depending on which level you implemented
in your widget.

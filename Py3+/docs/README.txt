================================
CirGO (Circular Gene Ontology Terms) 
================================


CirGO (Circular Gene Ontology terms) is an alternative way of visualising
GO terms in 2D space that is suitable for publishing and presenting 
gene expression ontology data. 







Typical usage often looks like this::

    #!/usr/bin/env python

    from CirGO import location
    from towelstuff import utils

    if utils.has_towel():
        print "Your towel is located:", location.where_is_my_towel()

(Note the double-colon and 4-space indent formatting above.)

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.


A Section
=========

Lists look like this:

* First

* Second. Can be multiple lines
  but must be indented properly.

A Sub-Section
-------------

Numbered lists look like you'd expect:

1. hi there

2. must be going

Urls are http://like.this and links can be
written `like this <http://www.example.com/foo/bar>`_.

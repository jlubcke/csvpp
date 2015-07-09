========
Usage
========

To use CVS Pretty Printer in a project::

	import csvpp

	assert csvpp.csvpp(u'  foo, bar\n1, 2\n') == u'  foo, bar\n  1,   2\n'

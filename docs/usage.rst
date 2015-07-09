========
Usage
========

There is a command line version installed with the packag invoked like::

	$ cat | csvpp
          foo, bar
          1, 2
        ^D
     
The output will be::

        foo, bar
  	1,   2

To use CVS Pretty Printer in a project::

	import csvpp

	assert csvpp.csvpp(u'  foo, bar\n1, 2\n') == u'  foo, bar\n  1,   2\n'

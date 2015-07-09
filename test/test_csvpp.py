from __future__ import unicode_literals

from mock import patch

import csvpp


def test_format():

    actual = csvpp.csvpp("""\
        foo, bar, boink
        1, yayayayayay, 2
""")

    expected = """\
        foo, bar,         boink
        1,   yayayayayay, 2
"""

    assert expected == actual


@patch('sys.stdin')
@patch('sys.stdout')
def test_cmdline(fake_stdout, fake_stdin):

    fake_stdin.read.return_value = b"""\
            foo, bar
            1, 2
"""

    csvpp.main()

    fake_stdout.write.assert_called_with(b"""\
            foo, bar
            1,   2
""")

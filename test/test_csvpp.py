from __future__ import unicode_literals
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

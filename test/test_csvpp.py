from __future__ import unicode_literals
import csvpp


def test_format():

    actual = csvpp.csvpp("""\
        foo, bar
        1, yayayayayay
""")

    expected = """\
        foo, bar
        1,   yayayayayay
"""

    assert expected == actual

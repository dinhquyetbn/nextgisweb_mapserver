from lxml.etree import RelaxNG, fromstring, tostring

from .keyword import registry


def _test_shema(cls):
    root = cls.element_schema()
    root.set('datatypeLibrary', 'http://www.w3.org/2001/XMLSchema-datatypes')

    xml = tostring(root, pretty_print=True)

    idx = 1
    print('')
    for s in xml.split('\n'):
        print("%03d: %s" % (idx, s))
        idx += 1
    print('')

    RelaxNG(fromstring(xml))


def test_schema():
    for directive in registry:
        yield _test_shema, directive

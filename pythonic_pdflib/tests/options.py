from __future__ import absolute_import
from django.utils import unittest
from ..options import RGBColor, Options, FitTextline
from collections import OrderedDict

class RGBColorTestCase(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(RGBColor(255, 0, 255)), '{rgb 1.0 0.0 1.0}')
        self.assertEqual(str(RGBColor(100, 100, 100)), '{rgb 0.392156862745 0.392156862745 0.392156862745}')

    def test_hex(self):
        self.assertEqual(RGBColor(255, 127, 0).hex(), '#ff7f00')

class OptionsTestCase(unittest.TestCase):

    def test_list(self):
        d = OrderedDict()
        d['position'] = 'center'
        d['fillcolor'] = RGBColor(255, 0, 255)

        self.assertEqual(
            "%s" % Options([d, d]),
            '{{position=center fillcolor={rgb 1.0 0.0 1.0}} {position=center fillcolor={rgb 1.0 0.0 1.0}}}'
        )


class FitTextlineTestCase(unittest.TestCase):

    def test_fittextline(self):
        d = OrderedDict()
        d['position'] = 'center'
        d['fillcolor'] = '#414141'

        self.assertEqual(
            "%s" % FitTextline(d),
            '{position=center fillcolor=#414141}'
        )

        d = OrderedDict()
        d['position'] = 'center'
        d['fillcolor'] = RGBColor(255, 0, 255)

        self.assertEqual(
            "%s" % FitTextline(d),
            '{position=center fillcolor={rgb 1.0 0.0 1.0}}'
        )

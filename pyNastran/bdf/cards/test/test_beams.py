from __future__ import (nested_scopes, generators, division, absolute_import,
                        print_function, unicode_literals)
import os
import unittest
from itertools import count

from six.moves import zip
from numpy import array, allclose

from pyNastran.bdf.bdf import BDF, BDFCard, PBEAM
from pyNastran.bdf.field_writer_8 import print_card_8

class TestBeams(unittest.TestCase):
    def test_pbeam_01(self):
        lines = [
            'PBEAM,39,6,2.9,3.5,5.97',
            '     ,  , ,2.0,-4.0',
            '     ,YES,1.0,5.3,56.2,78.6',
            '     ,   ,   ,2.5,-5.0',
            '     ,   ,   ,1.1,    ,2.1,,0.21',
            '     ,   ,   ,   ,    ,0.5,,0.0',
        ]
        bdf = BDF(debug=False)
        card = bdf.process_card(lines)
        #print(print_card_8(card))
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)
        fields = card2.raw_fields()

        lines_expected = [
            'PBEAM         39       6     2.9     3.5    5.97      0.      0.      0.',
            '              0.      0.      2.     -4.      0.      0.      0.      0.',
            '             YES      1.     5.3    56.2    78.6      0.      0.      0.',
            '              0.      0.     2.5     -5.      0.      0.      0.      0.',
            '              1.      1.     1.1      0.     2.1     2.1     .21     .21',
            '              0.      0.      0.      0.      .5      .5      0.      0.'
        ]
        self._compare(fields, lines_expected)

    def _compare(self, fields, lines_expected):
        msg = print_card_8(fields).rstrip()
        lines_actual = msg.rstrip().split('\n')
        msg_a = '\n%s\n\n%s\n' % ('\n'.join(lines_expected), msg)
        msg_a += 'nlines_actual=%i nlines_expected=%i' % (len(lines_actual), len(lines_expected))
        self.assertEqual(len(lines_actual), len(lines_expected), msg_a)
        for i, actual, expected in zip(count(), lines_actual, lines_expected):
            actual = str(actual)
            expected = str(expected)
            msg = msg_a + '\ni=%s' % i + '\nactual   = %r\n' % actual
            msg += 'expected = %r' % expected
            self.assertEqual(actual, expected, msg)

    def test_pbeam_02(self):
        bdf = BDF(debug=False)
        lines = [
            'PBEAM,39,6,2.9,3.5,5.97',
            '     ,  , ,2.0,-4.0',
            '     ,YES,1.0,5.3,56.2,78.6',
            '     ,   ,   ,2.5,-5.0',
            #'     ,YES,1.0,5.3,56.2,78.6',
            #'     ,   ,   ,2.5,-5.0',
            #'     ,YES,1.0,5.3,56.2,78.6',
            #'     ,   ,   ,2.5,-5.0',
            '     ,   ,   ,1.1,    ,2.1,,0.21',
            '     ,   ,   ,   ,    ,0.5,,0.0',
        ]

        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)
        fields = card2.raw_fields()

        lines_expected = [
            'PBEAM         39       6     2.9     3.5    5.97      0.      0.      0.',
            '              0.      0.      2.     -4.      0.      0.      0.      0.',
            '             YES      1.     5.3    56.2    78.6      0.      0.      0.',
            '              0.      0.     2.5     -5.      0.      0.      0.      0.',
            #'             YES      1.     5.3    56.2    78.6      0.      0.      0.',
            #'              0.      0.     2.5     -5.      0.      0.      0.      0.',
            #'             YES      1.     5.3    56.2    78.6      0.      0.      0.',
            #'              0.      0.     2.5     -5.      0.      0.      0.      0.',
            '              1.      1.     1.1      0.     2.1     2.1     .21     .21',
            '              0.      0.      0.      0.      .5      .5      0.      0.'
        ]
        self._compare(fields, lines_expected)

    def test_pbeam_03(self):
        bdf = BDF(debug=False)
        lines = [
            'PBEAM,39,6,2.9,3.5,5.97',
            '     ,  , ,2.0,-4.0',
            '     ,YES,1.0,5.3,56.2,78.6',
            '     ,   ,   ,2.5,-5.0',
            '     ,   ,   ,1.1,    ,2.1,,0.21',
            '     ,   ,   ,   ,    ,0.5,,0.0',
        ]

        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)
        fields = card2.raw_fields()

        lines_expected = [
            'PBEAM         39       6     2.9     3.5    5.97      0.      0.      0.',
            '              0.      0.      2.     -4.      0.      0.      0.      0.',
            '             YES      1.     5.3    56.2    78.6      0.      0.      0.',
            '              0.      0.     2.5     -5.      0.      0.      0.      0.',
            '              1.      1.     1.1      0.     2.1     2.1     .21     .21',
            '              0.      0.      0.      0.      .5      .5      0.      0.',
        ]
        self._compare(fields, lines_expected)

    def test_pbeam_04(self):
        bdf = BDF(debug=False)
        lines = [
            'PBEAM,39,6,2.9,3.5,5.97',
            '     ,  , ,2.0,-4.0',
            '     ,   ,   ,1.1,    ,2.1,,0.21',
            '     ,   ,   ,   ,    ,0.5,,0.0',
        ]

        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)
        fields = card2.raw_fields()
        lines_expected = [
            'PBEAM         39       6     2.9     3.5    5.97      0.      0.      0.',
            '              0.      0.      2.     -4.      0.      0.      0.      0.',
            '              1.      1.     1.1      0.     2.1     2.1     .21     .21',
            '              0.      0.      0.      0.      .5      .5      0.      0.',
        ]
        self._compare(fields, lines_expected)

    def test_pbeam_05(self):
        bdf = BDF(debug=False)
        lines = [
            'PBEAM,39,6,2.9,3.5,5.97',
            '     ,  , ,2.0,-4.0',
        ]

        card = bdf.process_card(lines)
        #print(print_card_8(card))
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)
        fields = card2.raw_fields()
        msg = print_card_8(fields)

        lines_expected = [
            'PBEAM         39       6     2.9     3.5    5.97      0.      0.      0.',
            '              0.      0.      2.     -4.      0.      0.      0.      0.',
            '              1.      1.      0.      0.      0.      0.      0.      0.',
            '              0.      0.      0.      0.      0.      0.      0.      0.',
        ]
        self._compare(fields, lines_expected)

    def test_pbeam_06(self):
        bdf = BDF(debug=False)
        lines = [
            'PBEAM   1       1       1.      60.     1.                              PBEAM1',
            '+BEAM1  5.              -5.                                             PBEAM2',
            '+BEAM2  YES     1.      2.      240.                                    PBEAM3',
            '+BEAM3  10.             -10.                                            PBEAM4',
            '+BEAM4                  -.666667',
        ]

        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)
        fields = card2.raw_fields()

        lines_expected = [
            'PBEAM          1       1      1.     60.      1.      0.      0.      0.',
            '              5.      0.     -5.      0.      0.      0.      0.      0.',
            '             YES      1.      2.    240.      1.      0.      0.      0.',
            '             10.      0.    -10.      0.      0.      0.      0.      0.',
            '              1.      1.-.666667      0.      0.      0.      0.      0.',
            '              0.      0.      0.      0.      0.      0.      0.      0.',
        ]
        self._compare(fields, lines_expected)

    def test_pbeam_07(self):
        bdf = BDF(debug=False)
        lines = [
            'PBEAM   100     100     1.00    10.     1.0                             +Z1',
            '+Z1     NO      1.0                                                     +Z4',
            '+Z4     0.0     0.0',
        ]
        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)

        #if 0:
            #fields = card2.raw_fields()
            #msg = print_card_8(fields)

            #lines_actual = msg.rstrip().split('\n')
            #msg = '\n%s\n\n%s' % ('\n'.join(lines_expected), msg)
            #msg += 'nlines_actual=%i nlines_expected=%i' % (len(lines_actual), len(lines_expected))
            #self.assertEqual(len(lines_actual), len(lines_expected), msg)
            #for actual, expected in zip(lines_actual, lines_expected):
                #msg =  '\nactual   = %r\n' % actual
                #msg += 'expected = %r' % expected
                #self.assertEqual(actual, expected, msg)

    def test_pbeam_08(self):
        bdf = BDF(debug=False)
        lines = [
            'PBEAM*   4570049         4570010        .12             2.56-4          *    HRY',
            '*    HRY.005625                         8.889-4         6.4444-7        *    HRZ',
            '*    HRZ-.04            -.75            .04             -.75            *    HSA',
            '*    HSA.04             .75             -.04            .75             *    HSB',
            '*    HSB YES            1.              .12             2.56-4          *    HSC',
            '*    HSC.005625                         8.889-4         6.4444-7        *    HSD',
            '*    HSD-.04            -.75            .04             -.75            *    HSE',
            '*    HSE.04             .75             -.04            .75             *    HSF',
            '*    HSF.853433         .849842                                         *    HSG',
            '*    HSG',
        ]
        lines_expected = [
            'PBEAM*           4570049         4570010             .12         .000256',
            '*                .005625                        .0008889    .00000064444',
            '*                   -.04            -.75             .04            -.75',
            '*                    .04             .75            -.04             .75',
            '*                    YES              1.             .12         .000256',
            '*                .005625                        .0008889    .00000064444',
            '*                   -.04            -.75             .04            -.75',
            '*                    .04             .75            -.04             .75',
            '*                .853433         .849842',
            '*',
        ]

        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        card2 = PBEAM.add_card(cardi)

        fields = card2.raw_fields()
        msg = print_card_8(fields)
        size = 16
        msg = card2.write_card(size, 'dummy')

        lines_actual = msg.rstrip().split('\n')
        msg_a = '\n%s\n\n%s' % ('\n'.join(lines_expected), msg)
        msg_a += 'nlines_actual=%i nlines_expected=%i' % (
            len(lines_actual), len(lines_expected))
        self.assertEqual(len(lines_actual), len(lines_expected), msg)
        for actual, expected in zip(lines_actual, lines_expected):
            actual = str(actual)
            expected = str(expected)
            msg = msg_a + '\nactual   = %r\n' % actual
            msg += 'expected = %r' % expected
            self.assertEqual(actual, expected, msg)

    def test_pbeam_09(self):
        bdf = BDF(debug=False)
        fields = [
            u'PBEAM', 4570049, 4570010, 0.12, 0.000256, 0.005625, None, 0.0008889, 6.4444e-07,
            -0.04, -0.75, 0.04, -0.75, 0.04, 0.75, -0.04, 0.75,
            'YES', 1.0, 0.12, 0.000256, 0.005625, 0.000256, None, 0.0008889,
            6.4444e-07, -0.04, -0.75, 0.04, -0.75, 0.04, 0.75, -0.04,
            0.853433, 0.849842
        ]
        #fields = [u'PBAR', 1510998, 1520998, 0.0, 4.9000000000000006e-14,
        #4.9000000000000006e-14, 0.0, 0.0, None, 0.0, 0.0, 0.0, 0.0,
        #0.0, 0.0, 0.0, 0.0, None, None, 0.0]
        card = print_card_8(fields)
        #print(card)
        card = print_card_8(fields)
        lines = card.split('\n')
        card = bdf.process_card(lines)
        cardi = BDFCard(card)
        #with self.assertRaises(AssertionError):  # A=0, I12=0, K1=0
        pbeam = PBEAM.add_card(cardi)
        fields2 = pbeam.repr_fields()
        assert fields == fields

    def test_pbeam_10(self):
        """
        The number of continuation lines on a PBEAM for a NO/YESA is 0.
        The number of continuation lines on a PBEAM for a YES is 1.
        """
        model = BDF(debug=False)

        # correct - standard NO with full list of values
        lines = [
            'PBEAM          1       1 5.094+7 289940.1.6043+7         271610. 3.73058',
            '            0.',
            '              NO     1.0 .7489+7 238250.1.3182+7   1.-12 223170.3.458069',
            '              0.      0.           .872    .718',
            '              0.  .33936      0. .31983',
        ]
        lines_expected = lines
        model.add_card(lines, 'PBEAM', is_list=False)

        # correct - 2nd continuation line
        lines = [
            'PBEAM          2       1 5.094+7 289940.1.6043+7         271610. 3.73058',
            '+',
            '              NO     1.0 .7489+7 238250.1.3182+7   1.-12 223170.3.458069',
            '              0.      0.           .872    .718',
            '              0.  .33936      0. .31983',
        ]
        lines_expected = lines
        model.add_card(lines, 'PBEAM', is_list=False)

        # BAD x/xb value of 1.4 (should be 0 to 1.0)
        lines = [
            'PBEAM          2       1 5.094+7 289940.1.6043+7         271610. 3.73058',
            '+',
            '              NO     1.4 .7489+7 238250.1.3182+7   1.-12 223170.3.458069',
            '              0.      0.           .872    .718',
            '              0.  .33936      0. .31983',
        ]
        lines_expected = lines
        with self.assertRaises(AssertionError):
            model.add_card(lines, 'PBEAM', is_list=False)

        # error - 3 lines after NO
        lines = [
            'PBEAM          3       1 5.094+7 289940.1.6043+7         271610. 3.73058',
            '            0.',
            '              NO     1.0 .7489+7 238250.1.3182+7   1.-12 223170.3.458069',
            '            0.',
            '              0.      0.           .872    .718',
            '              0.  .33936      0. .31983',
        ]
        with self.assertRaises(RuntimeError):
            model.add_card(lines, 'PBEAM', is_list=False)

        # correct - skipped 2nd line
        lines = [
            'PBEAM          4       1 5.094+7 289940.1.6043+7         271610. 3.73058',
            '              NO     1.0 .7489+7 238250.1.3182+7   1.-12 223170.3.458069',
            '              0.      0.           .872    .718',
            '              0.  .33936      0. .31983',
        ]
        lines_expected = lines
        model.add_card(lines, 'PBEAM', is_list=False)

        # correct - skipped 2nd line and last line
        lines = [
            'PBEAM          5       1 5.094+7 289940.1.6043+7         271610. 3.73058',
            '              NO     1.0 .7489+7 238250.1.3182+7   1.-12 223170.3.458069',
            '              0.      0.           .872    .718',
        ]
        lines_expected = lines
        model.add_card(lines, 'PBEAM', is_list=False)

        # correct - skipped 2nd line and last 2 lines
        lines = [
            'PBEAM          6       1 5.094+7 289940.1.6043+7         271610. 3.73058',
            '              NO     1.0 .7489+7 238250.1.3182+7   1.-12 223170.3.458069',
        ]
        lines_expected = lines
        model.add_card(lines, 'PBEAM', is_list=False)

        # correct - single line
        lines = [
            'PBEAM          7       1 5.094+7 289940.1.6043+7         271610. 3.73058',
        ]
        lines_expected = lines
        model.add_card(lines, 'PBEAM', is_list=False)

    def test_pbeam_11(self):
        model = BDF(debug=False)
        lines = [
            #'PBEAM         1       1    1.e8    1.e8    1.e8              10.      1.',
            #'             NO      1.    3.e5    3.e8    3.e8              10.      1.',
            'PBEAM          1       1    1.+8    1.+8    1.+8             10.      1.',
            '              NO      1. 300000.    3.+8    3.+8             10.      1.',
        ]
        model.add_card(lines, 'PBEAM', is_list=False)
        lines_expected = [
            'PBEAM          1       1    1.+8    1.+8    1.+8             10.      1.',
            '+',
            '              NO      1. 300000.    3.+8    3.+8             10.      1.',
        ]
        prop = model.properties[1]
        #print(prop.raw_fields())
        lines_actual = prop.write_card().split('\n')
        msg_a = ''
        for line_expected, line_actual in zip(lines_expected, lines_actual):
            #assert line_expected == line_actual, line_actual
            actual = str(line_actual)
            expected = str(line_expected)
            msg = msg_a + '\nactual   = %r\n' % actual
            msg += 'expected = %r' % expected
            self.assertEqual(actual, expected, msg)

    def test_cbeam_01(self):
        """modification of test_pbeam_05"""
        model = BDF(debug=False)
        lines = ['PBEAM,3,6,2.9,3.5,5.97,0.4,3.14',
                 '     , , ,2.0,-4.0',]
        card = model.add_card(lines, 'PBEAM', is_list=False)

        lines = ['CBEAM         10       3      1       2      0.01.000000     0.0']
        model.add_card(lines, 'CBEAM', is_list=False)

        mid = 6
        E = 1.0e7
        G = None
        nu = 0.3
        model.add_mat1(mid, E, G, nu)
        model.add_grid(1, xyz=[0., 0., 0.])
        model.add_grid(2, xyz=[0., 0., 0.])
        model.cross_reference()

        cbeam = model.Element(10)
        #cbeam = model.elements[10]
        #print("Area = ", cbeam.Area())
        #print("I11 = ", cbeam.I11())
        #print("I22 = ", cbeam.I22())
        #print("I12 = ", cbeam.I12())
        #print("J = ", cbeam.J())

        #print("Area = ", cbeam.Area())
        #print("I11 = ", cbeam.I1())
        #print("I22 = ", cbeam.I2())
        #print("I12 = ", cbeam.I12())
        #print("J = ", cbeam.J())
        node_ids = cbeam.node_ids
        assert node_ids == [1, 2], node_ids
        self.assertEqual(cbeam.Area(), 2.9)
        self.assertEqual(cbeam.I11(), 3.5)
        self.assertEqual(cbeam.I22(), 5.97)
        self.assertEqual(cbeam.I12(), 0.4)
        self.assertEqual(cbeam.J(), 3.14)

    def test_cbeam_02(self):
        """CBEAM/PBEAML"""
        model = BDF(debug=False)
        model.add_grid(1, xyz=[0., 0., 0.])
        model.add_grid(2, xyz=[1., 0., 0.])
        model.add_grid(3, xyz=[0., 1., 0.])

        mid = 1
        E = 3.0e7
        G = None
        nu = 0.3
        model.add_mat1(mid, E, G, nu, rho=1.)

        #---------------------------------------------------------------
        eid = 1
        pid = 101
        nids = [1, 2]
        x = [0., 0., 1.]
        g0 = None
        cbeam1 = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                 pa=0, pb=0, wa=None, wb=None,
                                 sa=0, sb=0, comment='CBEAM')
        Type = 'BOX'
        xxb = [0.]
        dims = [[1., 2., 0.1, 0.1], [1., 2., 0.1, 0.1]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 2
        pid = 102
        x = None
        g0 = 3
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'BOX'
        xxb = [0.]
        dims = [[1., 2., 0.1, 0.1]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 3
        pid = 103
        x = [0., 0., 1.]
        g0 = None
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'BAR'
        xxb = [0.]
        dims = [[2., 3.]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 4
        pid = 104
        x = [0., 0., 1.]
        g0 = None
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'ROD'
        xxb = [0.]
        dims = [[2.]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 5
        pid = 105
        x = [0., 0., 1.]
        g0 = None
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'TUBE'
        xxb = [0.]
        dims = [[2., 1.]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 6
        pid = 106
        x = [0., 0., 1.]
        g0 = None
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'L'
        xxb = [0.]
        dims = [[2., 2., 0.1, 0.1]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 7
        pid = 107
        x = [0., 0., 1.]
        g0 = None
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'T'
        xxb = [0.]
        dims = [[1., 2., 0.1, 0.2]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 8
        pid = 108
        x = [0., 0., 1.]
        g0 = None
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'T1'
        xxb = [0.]
        dims = [[1., 2., 0.2, 0.1]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------
        eid = 9
        pid = 109
        x = [0., 0., 1.]
        g0 = None
        cbeam = model.add_cbeam(eid, pid, nids, x, g0, offt='GGG', bit=None,
                                pa=0, pb=0, wa=None, wb=None,
                                sa=0, sb=0, comment='CBEAM')
        Type = 'T2'
        xxb = [0.]
        dims = [[1., 2., 0.2, 0.1]]
        pbeaml = model.add_pbeaml(pid, mid, Type, xxb, dims, nsm=None,
                                  so=None, comment='PBEAML')
        #---------------------------------------------------------------

        model.validate()
        model.pop_parse_errors()
        model.pop_xref_errors()
        pbeaml.raw_fields()
        pbeaml.write_card_16()
        model._verify_bdf(xref=False)

        #----------------
        model.cross_reference()

        model._verify_bdf(xref=True)
        model.mass_properties()
        pids_to_area = model.get_area_breakdown(property_ids=None, sum_bar_area=False)
        for pid, area in sorted(pids_to_area.items()):
            assert area > 0., 'pid=%s area=%s' % (pid, area)

        pids_to_mass, _mass_type_to_mass = model.get_mass_breakdown(property_ids=None)
        for pid, mass in sorted(pids_to_mass.items()):
            assert mass > 0., 'pid=%s mass=%s' % (pid, mass)

        #--------------------
        model.uncross_reference()
        model._verify_bdf(xref=False)
        model.safe_cross_reference()
        model.uncross_reference()

    def test_beam_mass_01(self):
        model = BDF(debug=False)
        #model.case_control_deck = CaseControlDeck(case_control_lines)
        spc = ['SPC1', 123456, 123456, 1]
        grid1 = ['GRID', 1, None, 0., 0., 0.]
        grid2 = ['GRID', 2, None, 1., 0., 0.]
        grid3 = ['GRID', 3, None, 1., 0., 0.]
        force = ['FORCE', 100, 1, 0, 2., 3., 4.]

        pid = 11
        cbeam = [
            'CBEAM', 10, pid, 1, 2, 0., 1., 0., None,
        ]
        mid = 12
        nsm_offset_a = [0., 0., 0.]
        nsm_offset_b = [0., 50., 0.]
        k1 = k2 = None
        area1 = 2.0
        area2 = 1.0
        rho = 3.
        nsm_a = 0.
        nsm_b = 0.
        nu = 0.3
        pbeam = ([
            'PBEAM', pid, mid,
                        area1, 2.1, 1.2, 1.3, None, nsm_a,
            None, None, None, None, None, None, None, None,

            'YES', 1.0, area2, 2.1, 1.2, 1.3, None, nsm_b,
            None, None, None, None, None, None, None, None,

            k1, k2, None, None, 100., 100., None, None] +  # 100s are the NSIa, NSIb (moment of inertia per unit length)
            nsm_offset_a + nsm_offset_b + [None, None, None, None]) # Nones are neutral axis offset
        #print('\n' + print_card_8(pbeam))

        mat1 = ['MAT1', 12, 3.0e7, None, nu, rho]
        model.add_card(grid1, 'GRID')
        model.add_card(grid2, 'GRID')
        #model.add_card(grid3, 'GRID')
        model.add_card(cbeam, 'CBEAM')
        model.add_card(pbeam, 'PBEAM')
        model.add_card(mat1, 'MAT1')
        model.add_card(spc, 'SPC1')
        model.add_card(force, 'FORCE')
        model.cross_reference()
        #print(model.properties[11])

        mass, cg, I = model.mass_properties(
            element_ids=None, mass_ids=None,
            reference_point=None,
            sym_axis=None,
            scale=None)
        #print('cg* =', cg)
        L = 1.0
        area = (area1 + area2) / 2.
        nsm = (nsm_a + nsm_b) / 2.
        mass_per_length = area * rho + nsm
        mass = L * mass_per_length

        mass_a = L / 2. * (area1 * rho + nsm_a)
        mass_b = L / 2. * (area2 * rho + nsm_b)
        xcg = (0.0 * mass_a + 1.0 * mass_b) / (mass_a + mass_b)
        #print(mass_a, mass_b, xcg, mass_a + mass_b)
        #print('mass =', mass)
        #cbeam = CBEAM()
        cbeam = model.elements[10]
        pbeam = model.properties[11]
        assert pbeam.Nu() == nu, 'pbeam.Nu()=%s nu=%s' % (pbeam.Nu(), nu)
        assert pbeam.Rho() == rho, 'pbeam.Rho()=%s rho=%s' % (pbeam.Rho(), rho)
        assert allclose(cbeam.Length(), 1.0), cbeam.Length()
        #assert allclose(cbeam.Mass(), 10.25), cbeam.Mass()
        #assert allclose(cbeam.MassPerLength(), 10.25), cbeam.MassPerLength()
        #assert allclose(mass, 10.25), mass

        with open('pbeam12.bdf', 'w') as bdf_file:
            case_control_lines = (
                'SOL 101\n'
                'CEND\n'
                'SUBCASE 1\n'
                '    STRESS(PLOT,SORT1,REAL) = ALL\n'
                '    SPC = 123456\n'
                '    LOAD = 100\n'
                'BEGIN BULK\n'
                'PARAM,GRDPNT,0\n'
                'PARAM,POST,-1\n'
                'PARAM   POSTEXT YES\n'
            )
            bdf_file.write(case_control_lines)
            model.write_bdf(bdf_file, enddata=True)

        model2 = BDF(debug=False)
        model2.read_bdf('pbeam12.bdf')

        if not os.path.exists('pbeam12.op2') and 0:
            os.system('nastran scr=yes bat=no old=no pbeam12.bdf')
        os.remove('pbeam12.bdf')

        if 0:  # pragma: no cover
            from pyNastran.op2.op2 import OP2
            op2 = OP2()
            op2.read_op2('pbeam12.op2')
            #os.remove('pbeam12.op2')
            gpw = op2.grid_point_weight
            op2_mass = gpw.mass.max()
            assert op2_mass == mass, 'op2_mass=%s mass=%s' % (op2_mass, mass)
            print('op2_mass=%s mass=%s' % (op2_mass, mass))
            op2_cg = gpw.cg

            cg = array([0.5, 0., 0.], dtype='float32')
            print('cg =', op2_cg)

    def test_pbmsect(self):
        """tests a PBMSECT"""
        model = BDF(debug=False)
        pid = 10
        mid = 11
        form = 'GS'
        options = {'OUTP' : 2}
        #pbrsect = model.add_pbrsect(pid, mid, form, options, comment='pbrsect')
        pbrsect = model.add_pbmsect(pid, mid, form, options, comment='pbmsect')

        pbrsect.validate()
        pbrsect.raw_fields()
        pbrsect.write_card()
        pbrsect.write_card(size=16)

    def test_pbeam3(self):
        """tests a PBEAM3"""
        model = BDF(debug=False)
        pid = 10
        mid = 11
        A = 1.0
        iz = 2.0
        iy = 3.0
        iyz = 0.4
        j = 5.0
        #form = 'GS'
        #options = {'OUTP' : 2}
        #pbrsect = model.add_pbrsect(pid, mid, form, options, comment='pbrsect')
        pbeam3 = model.add_pbeam3(pid, mid, A, iz, iy, iyz, j, nsm=0.,
                                  cy=0., cz=0., dy=0., dz=0., ey=0., ez=0., fy=0., fz=0.,
                                  comment='pbeam3')
        model.add_mat1(mid, 3.0e7, None, 0.3, rho=0.2)

        pbeam3.validate()
        #pbeam3.raw_fields()
        pbeam3.write_card()
        pbeam3.write_card(size=16)
        model.cross_reference()
        model.pop_xref_errors()

        pbeam3.write_card()
        pbeam3.write_card(size=16)

        model.uncross_reference()
        pbeam3.write_card()
        pbeam3.write_card(size=16)



if __name__ == '__main__':  # pragma: no cover
    unittest.main()

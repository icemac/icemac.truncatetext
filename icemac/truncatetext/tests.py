# -*- coding: utf-8 -*-
# Copyright (c) 2009-2012 Michael Howitz
# See also LICENSE.txt
# $Id$

import doctest

def test_all():
    return doctest.DocFileSuite('README.txt')

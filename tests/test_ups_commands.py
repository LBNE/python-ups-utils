#!/usr/bin/env python
'''
test ups.commands

WARNING: these tests will merely print a message and succeed if UPS is not detected.

'''

import os
from ups.commands import install, UpsCommands
from ups.products import make_product

ups_version = '5.0.5'
ups_products = os.path.realpath('products')

def setup():
    install(ups_version, ups_products)
    

def test_ups_depend():
    '''
    Test calling "ups depend".
    '''
    ups = UpsCommands(ups_products)

    prod = make_product('ups')
    text = ups.depend(prod)

    print text
    assert text.startswith('ups v')

def test_ups_avail():
    '''
    Test calling "ups depend".
    '''
    ups = UpsCommands(ups_products)

    text = ups.avail()
    print text



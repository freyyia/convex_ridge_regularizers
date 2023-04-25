# -*- coding: utf-8 -*-

""" PACKAGE INFO
This file contains parameters to fill settings in setup.py for 
the cvx_nn_models package.
"""

# Set the package release version
version_info = (0, 0, 1)
__version__ = '.'.join(str(c) for c in version_info)

# Set the package details
__name__                = 'cvx_nn_models'
__maintainer__          = "T. Klatzer"
__maintainer_email__    = "t.klatzer@sms.ed.ac.uk"
__license__             = "GNU General Public License v3.0"
__platforms__           = "Linux, Windows, MacOS"
__provides__            = ["cvx_nn_models"]
__author__       = "T. Klatzer"
__email__        = "t.klatzer@sms.ed.ac.uk"
__year__         = '2023'
__url__          = "https://github.com/freyyia/convex_ridge_regularizers"
__download_url__ = "https://github.com/freyyia/convex_ridge_regularizers"
__description__  = ''


# Default package properties
__about__ = ('{}\nAuthor: {} \nEmail: {} \nYear: {} \nInfo: {}'
             ''.format(__name__, __author__, __email__, __year__,
                       __description__))



__classifiers__ = ["Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Windows",      
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers"],


__long_description__ = """
==========
Convex Regularizer for Inverse Problems
==========
Forked from axgoujon
A Neural-Network-Based Convex Regularizer for Inverse Problems
https://github.com/freyyia/convex_ridge_regularizers
"""



.. imgeaser documentation master file, created by
   sphinx-quickstart on Sat Sep 30 09:41:25 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to imgeaser's documentation!
====================================

A python package for performing easing functions on image data.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   self
   /api.rst
   /examples.rst
   /requirements.rst


Why did you write this?
=======================
I've been working on some code to procedurally generate images and
video. It is getting pretty bloated, so I thought I could carve the
easing functions into its own module. For that reason, I'm not sure
if this is useful to anyone else, but I figured I'd put it out there
just in case.


Who created these easing functions?
===================================
I have no idea who created the concept of easing functions. Most of
the ones here are adapted from algorithms found on:

    http://easings.net


How do I run the code?
======================
The best way to get started is to clone the repository to your local
system and take a look at the examples in the example directory.


Is it portable?
===============
It should be, but I've not tested that.


Can I install this package from pip?
====================================
Yes, but imgeaser is not currently available through PyPI. You will
need to clone the repository to the system you want to install
imgwriter on and run the following::

    pip install path/to/local/copy

Replace `path/to/local/copy` with the path for your local clone of
this repository.


How do I run the tests?
=======================
The `precommit.py` script in the root of the repository will run the
unit tests and a few other tests beside. Otherwise, the unit tests
are written with :mod:`pytest`, so you can run the tests with::

    python -m pytest


How do I contribute?
====================
At this time, this is code is really just me exploring and learning.
I've made it available in case it helps anyone else, but I'm not really
intending to turn this into anything other than a personal project.

That said, if other people do find it useful and start using it, I'll
reconsider. If you do use it and see something you want changed or
added, go ahead and open an issue. If anyone ever does that, I'll
figure out how to handle it.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Gamut Mapping Ramblings
=======================

..  image:: https://raw.githubusercontent.com/colour-science/gamut-mapping-ramblings/master/docs/_static/Gamut_Medicina_01.png

Introduction
------------

Various ramblings in the world of Scene-Referred Gamut Mapping as part of the
`ACES VWG <https://community.acescentral.com/c/aces-development-acesnext/vwg-aces-gamut-mapping-working-group/80>`__.

Study Models Implemented in `notebooks/gamut_mapping_medicina_01.ipynb`:

- `Mansencal and Scharfenberg (2020) <https://community.acescentral.com/t/gamut-mapping-in-cylindrical-and-conic-spaces/2870/4>`__
- `Smith (2020) <https://community.acescentral.com/t/rgb-saturation-gamut-mapping-approach-and-a-comp-vfx-perspective/>`__

Images courtesy `Carol Payne <https://www.dropbox.com/sh/u6z2a0jboo4vno8/AAB-10qcflhpr0C5LWhs7Kq4a?dl=0>`__
and `Martin Smekal <https://community.acescentral.com/t/vfx-work-in-acescg-with-out-of-gamut-devices/2385>`__.

Installation
------------

`Poetry <https://python-poetry.org/>`__ is required to install main
dependencies and `Node.js <https://nodejs.org/>`__ for the
`Jupyter Lab <https://jupyter.org/>`__ Matplotlib extension.

.. code-block:: bash

    $ poetry install
    $ poetry run python -c "import imageio;imageio.plugins.freeimage.download()"
    $ jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib

Run
~~~

.. code-block:: bash

    $ poetry run jupyter lab

Code of Conduct
---------------

The *Code of Conduct*, adapted from the `Contributor Covenant 1.4 <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>`__,
is available on the `Code of Conduct <https://www.colour-science.org/code-of-conduct/>`__ page.

About
-----

| **Gamut Mapping Ramblings** by Colour Developers
| Copyright © 2019-2020 – Colour Developers – `colour-developers@colour-science.org <colour-developers@colour-science.org>`__
| This software is released under terms of New BSD License: https://opensource.org/licenses/BSD-3-Clause
| `https://github.com/colour-science/gamut-mapping-ramblings <https://github.com/colour-science/gamut-mapping-ramblings>`__

Gamut Mapping Ramblings
=======================

..  image:: https://raw.githubusercontent.com/colour-science/gamut-mapping-ramblings/master/resources/images/Gamut_Medicina_01.png

Introduction
------------

Ramblings in the world of Scene-Referred Gamut Mapping as part of the
`ACES VWG <https://community.acescentral.com/c/aces-development-acesnext/vwg-aces-gamut-mapping-working-group/80>`__.

The following study models are implemented in the `gamut_mapping_medicina_01 <https://github.com/colour-science/gamut-mapping-ramblings/blob/master/notebooks/gamut_mapping_medicina_01.ipynb>`__
notebook.

- `Mansencal and Scharfenberg (2020) <https://community.acescentral.com/t/gamut-mapping-in-cylindrical-and-conic-spaces/2870/4>`__
- `Smith (2020) <https://community.acescentral.com/t/rgb-saturation-gamut-mapping-approach-and-a-comp-vfx-perspective/>`__

The notebook is intended to be read with the **JupyterLab Dark Theme**:

..  image:: https://raw.githubusercontent.com/colour-science/gamut-mapping-ramblings/master/resources/images/JupyterLab_Dark_Theme.png

Various compression functions are implemented in the `gamut_mapping_compression_functions_01 <https://github.com/colour-science/gamut-mapping-ramblings/blob/master/notebooks/gamut_mapping_compression_functions_01.ipynb>`__
notebook.

Images courtesy of:

- `Justin Holt <https://www.dropbox.com/sh/u6z2a0jboo4vno8/AAB-10qcflhpr0C5LWhs7Kq4a?dl=0>`__
- `Thomas Mansencal <https://community.acescentral.com/t/spectral-images-generation-and-processing/>`__
- `Fabian Matas <https://community.acescentral.com/t/spectral-images-generation-and-processing/>`__
- `Carol Payne <https://www.dropbox.com/sh/u6z2a0jboo4vno8/AAB-10qcflhpr0C5LWhs7Kq4a?dl=0>`__
- `Martin Smekal <https://community.acescentral.com/t/vfx-work-in-acescg-with-out-of-gamut-devices/2385>`__

Installation
------------

Docker
~~~~~~

.. code-block:: bash

    $ docker build -t colourscience/gamut-mapping-ramblings:latest "."

*Note*

Allocated memory will need to be increased in Docker preferences:
*Preferences --> Resources --> Advanced*, 8Go should be enough.

Pip
~~~

`Node.js <https://nodejs.org/>`__ is required for the
`Jupyter Lab <https://jupyter.org/>`__ Matplotlib extension.

`Pip <https://pip.pypa.io/en/stable/installing/>`__ can be used to install the
main dependencies, assuming you have created and activated a
`Virtual Environment <https://docs.python.org/3/tutorial/venv.html>`__:

.. code-block:: bash

    $ pip install --user -r requirements.txt
    $ python -c "import imageio;imageio.plugins.freeimage.download()"
    $ jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib

Poetry
~~~~~~

`Node.js <https://nodejs.org/>`__ is required for the
`Jupyter Lab <https://jupyter.org/>`__ Matplotlib extension.

`Poetry <https://python-poetry.org/>`__ can also be used to install the main
dependencies:

.. code-block:: bash

    $ poetry install
    $ poetry run python -c "import imageio;imageio.plugins.freeimage.download()"
    $ poetry run jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib

Usage
-----

Docker
~~~~~~

.. code-block:: bash

    $ docker run -v $PWD:/home/colour-science/gamut-mapping-ramblings -p 8888:8888 colourscience/gamut-mapping-ramblings:latest

Pip
~~~

.. code-block:: bash

    $ jupyter lab

Poetry
~~~~~~

.. code-block:: bash

    $ poetry run jupyter lab

Code of Conduct
---------------

The *Code of Conduct*, adapted from the `Contributor Covenant 1.4 <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>`__,
is available on the `Code of Conduct <https://www.colour-science.org/code-of-conduct/>`__ page.

Contact & Social
----------------

The *Colour Developers* can be reached via different means:

- `Email <mailto:colour-developers@colour-science.org>`__
- `Facebook <https://www.facebook.com/python.colour.science>`__
- `Gitter <https://gitter.im/colour-science/colour>`__
- `Twitter <https://twitter.com/colour_science>`__

About
-----

| **Gamut Mapping Ramblings** by Colour Developers
| Copyright © 2019-2021 – Colour Developers – `colour-developers@colour-science.org <colour-developers@colour-science.org>`__
| This software is released under terms of New BSD License: https://opensource.org/licenses/BSD-3-Clause
| `https://github.com/colour-science/gamut-mapping-ramblings <https://github.com/colour-science/gamut-mapping-ramblings>`__

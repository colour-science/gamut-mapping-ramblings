FROM python:3.7

RUN curl -sL https://deb.nodesource.com/setup_13.x | bash - \
    && apt-get install -y nodejs

WORKDIR /tmp
COPY ./requirements.txt /tmp
RUN pip install -r requirements.txt \
    && rm /tmp/requirements.txt \
    && python -c "import imageio;imageio.plugins.freeimage.download()" \
    && jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib

RUN mkdir -p /home/colour-science/gamut-mapping-ramblings
WORKDIR /home/colour-science/gamut-mapping-ramblings

CMD sh -c 'cd /home/colour-science/gamut-mapping-ramblings && jupyter lab --allow-root --ip=0.0.0.0 --port=8888'

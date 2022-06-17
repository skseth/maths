ARG SAGE_VERSION=9.0
ARG SAGE_PYTHON_VERSION=3.7
FROM jupyter/scipy-notebook
# install Python packages you often use
RUN set -ex \
   && conda install --quiet --yes \
   # choose the python packages you need
   'plotly==5.5.0' \
   'ipyleaflet' \
   'bqplot' \
   && conda clean --all -f -y \
   # install jupyter lab extensions you need
   && jupyter labextension install jupyterlab-plotly@5.5.0 --no-build \
   && jupyter lab build -y \
   && jupyter lab clean -y \
   && rm -rf "/home/${NB_USER}/.cache/yarn" \
   && rm -rf "/home/${NB_USER}/.node-gyp" \
   && fix-permissions "${CONDA_DIR}" \
   && fix-permissions "/home/${NB_USER}"

RUN set -ex \
   && conda install --quiet --yes \
   # choose the python packages you need
   'jupyterlab-git' \
   'geopandas' \
   'geojson' \
   'mapclassify' \
   'contextily' \
   'folium' \
   'mplleaflet' \
   'osmnx' \
   && conda clean --all -f -y \
   # install jupyter lab extensions you need
   && jupyter lab build -y \
   && jupyter lab clean -y \
   && rm -rf "/home/${NB_USER}/.cache/yarn" \
   && rm -rf "/home/${NB_USER}/.node-gyp" \
   && fix-permissions "${CONDA_DIR}" \
   && fix-permissions "/home/${NB_USER}"

RUN set -ex \
   && conda install --quiet --yes \
   # choose the python packages you need
   'astropy' \
   && conda clean --all -f -y \
   && rm -rf "/home/${NB_USER}/.cache/yarn" \
   && rm -rf "/home/${NB_USER}/.node-gyp" \
   && fix-permissions "${CONDA_DIR}" \
   && fix-permissions "/home/${NB_USER}"

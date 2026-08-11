# Use a specific, pinned tag instead of 'latest' for build reproducibility
FROM jupyter/scipy-notebook:latest

USER root

# Install system dependencies for advanced mathematical text (LaTeX), graphics, and SageMath runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
    cm-super \
    dvipng \
    ffmpeg \
    gfortran \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

# Add conda-forge channel explicitly to resolve the complex Sage/Flint tree
RUN mamba install --quiet --yes \
    # Core Mathematical Framework
   #  'sage=10.3' \
    # Core Plotting & Graphing
    'python' \
    'sqlite' \    
    # Think Stats Specific Packages
    'statsmodels' \
    'seaborn' \    
    'plotly=5.22.*' \
    'bqplot' \
    'matplotlib' \
    # Geospatial Graphics
    'ipyleaflet' \
    'geopandas' \
    'geojson' \
    'mapclassify' \
    'contextily' \
    'folium' \
    'osmnx' \
    # Mathematics & Astronomy
    'astropy' \
    'sympy' \
    # Productivity
    'jupyterlab-git' \
    && mamba clean --all -f -y \
    # Register the SageMath kernel natively into Jupyter
   #  && sage -sh -c "jupyter kernelspec install --user" \
    # Fix file permissions for the Jupyter user
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"
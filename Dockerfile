FROM mdstudio/mdstudio_docker_conda as amber_base

ARG AMBER_TOOLS_VERSION=19

# Install AmberTools using conda
RUN conda install -c anaconda libgfortran && \
    conda install -c openbabel openbabel && \
    conda install ambertools=${AMBER_TOOLS_VERSION} -c ambermd && \
    conda install numpy

COPY entry_point_mdstudio_amber.sh sett* setup.py /home/mdstudio/mdstudio_amber/

COPY mdstudio_amber /home/mdstudio/mdstudio_amber/mdstudio_amber

COPY scripts /home/mdstudio/mdstudio_amber/scripts

RUN chown mdstudio:mdstudio /home/mdstudio/mdstudio_amber

WORKDIR /home/mdstudio/mdstudio_amber

RUN pip install -e .

CMD ["bash", "entry_point_mdstudio_amber.sh"]

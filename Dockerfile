FROM mdstudio/mdstudio_docker3:0.0.1 as amber_base

RUN apt-get update -y && apt-get install csh gcc gfortran flex -y

WORKDIR /home/mdstudio

COPY AmberTools17.tar.bz2 /home/mdstudio

RUN tar -xvf AmberTools17.tar.bz2

ENV PYTHON /usr/local/bin/python

RUN cd /home/mdstudio/amber16 && ./configure --no-updates --with-python $PYTHON gnu && make

RUN rm -rf /home/mdstudio/amber16/AmberTools /home/mdstudio/amber16/test

# used amber compiled in previous step
FROM mdstudio/mdstudio_docker3:0.0.1

# ENV AMBERHOME /home/mdstudio/amber16

run apt-get update -y && apt-get install swig gcc gfortran libopenbabel-dev openbabel -y

COPY --from=amber_base /home/mdstudio/amber16 /home/mdstudio/amber16

COPY entry_point_lie_amber.sh sett* setup.py /home/mdstudio/lie_amber/

COPY lie_amber /home/mdstudio/lie_amber/lie_amber

COPY scripts /home/mdstudio/lie_amber/scripts

RUN chown mdstudio:mdstudio /home/mdstudio/lie_amber

WORKDIR /home/mdstudio/lie_amber

RUN pip install openbabel .

USER mdstudio

CMD ["bash", "entry_point_lie_amber.sh"]

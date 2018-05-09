FROM mdstudio/mdstudio_docker3:0.0.1

COPY . /home/mdstudio/lie_amber

RUN chown mdstudio:mdstudio /home/mdstudio/lie_amber

WORKDIR /home/mdstudio/lie_amber

RUN pip install .

USER mdstudio

CMD ["bash", "entry_point_lie_amber.sh"]

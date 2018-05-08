FROM python:3.6

# Service user
RUN useradd mdstudio && mkdir /home/mdstudio && chown mdstudio:mdstudio /home/mdstudio

COPY . /home/mdstudio

WORKDIR /home/mdstudio

RUN pip install mdstudio

RUN pip install .

USER mdstudio

CMD ["./entry_point_lie_amber.sh"]

FROM python:3.8
COPY . /src
WORKDIR /src
RUN pip3 install -r src/requirements.txt
WORKDIR /src/src
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
EXPOSE 5000

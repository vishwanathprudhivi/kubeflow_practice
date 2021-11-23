FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y python3
RUN mkdir /legacy_code_repo

COPY requirements.txt /legacy_code_repo
COPY load_data.py /legacy_code_repo

RUN pip install -r /legacy_code_repo/requirements.txt

ENTRYPOINT [ "python3","/legacy_code_repo/load_data.py" ]
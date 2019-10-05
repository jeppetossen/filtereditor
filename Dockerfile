FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /filtereditor
ADD . /filtereditor
RUN pip install -r requirements.txt

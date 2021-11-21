FROM python:3
COPY app.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
CMD [ "pytest", "./app.py" ]
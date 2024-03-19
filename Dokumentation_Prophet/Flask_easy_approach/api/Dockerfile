FROM python:3.7

RUN mkdir /Flaskapp
WORKDIR /Flaskapp
COPY . /Flaskapp

RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install -r requirements.txt
#RUN pip install tensorflow

EXPOSE 5000
CMD ["python", "Flaskapp/app.py"]
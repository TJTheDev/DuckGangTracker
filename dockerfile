FROM docker.io/python
WORKDIR /usr/src/app
RUN mkdir /usr/src/app/data
#COPY requirements.txt ./
COPY app.py ./
COPY database.py ./
COPY forms.py ./
COPY requirements.txt ./
COPY templates ./templates
COPY static ./static
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python",  "app.py"]

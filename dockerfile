FROM docker.io/python
RUN pip install sqlalchemy
COPY database.py .
ENTRYPOINT ["python", "database.py"]

FROM python:3.11.3
RUN echo running 
WORKDIR /backend
COPY . .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "host=0.0.0.0"]


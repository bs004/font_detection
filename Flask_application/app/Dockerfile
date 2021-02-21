FROM python:3.7.1

COPY .usr/src/app

RUN pip install --upgrade pip

RUN sudo apt install tesseract-ocr

RUN pip install -r requirements.txt

CMD ["python" "app.py"]
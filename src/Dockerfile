FROM python:3.11

WORKDIR /src

COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /src/app.py

COPY templates /src/templates

CMD python app.py

#per buildare l'immagine da ps: "docker build -t *tagapplicazione* ."
#per runnare il container: "docker run -p 3000:3000 *tagapplicazione*"
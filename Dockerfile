FROM adreeve/python-numpy
COPY . /app/
WORKDIR /app/
RUN apt-get update
RUN apt-get install -y add make automake gcc g++ subversion python3-dev
RUN pip install -r requirements.txt && \
    python start.py

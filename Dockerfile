FROM python
LABEL authors="vtalantsev"

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
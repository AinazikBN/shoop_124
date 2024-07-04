FROM python:3

ENV PYTHONIOENCODING UTF-8 
ENV TZ=Asia/Bishkek

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo > /etc/timezone

WORKDIR /user/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir static && mkdir media
COPY . .

RUN python3 manage.py collecstatic --noinput

RUN chmod -R 755 /ursr/src/app/static

EXPOSE 8000










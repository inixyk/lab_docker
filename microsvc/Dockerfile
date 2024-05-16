FROM python
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask uWSGI requests redis
WORKDIR /app
COPY app /app
COPY cmd.sh /
EXPOSE 9090 9191
USER uwsgi
CMD ["/cmd.sh"]
# CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/aplikasi.py", "--callable", "app", "--stats", "0.0.0.0:9191"]
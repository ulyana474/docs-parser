FROM python:3
WORKDIR /code
RUN pip install pipenv
COPY Pipfile Pipfile.lock ${WORKDIR}
RUN pipenv install --system --deploy
COPY . /code/
# COPY ./entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]
FROM python:3
WORKDIR /code
RUN pip install pipenv
COPY Pipfile Pipfile.lock ${WORKDIR}/
RUN pipenv install --system --deploy
COPY ./ ./code
# CMD ["alembic", "upgrade", "head"]

# ENTRYPOINT ["tail", "-f", "/dev/null"] not closing container
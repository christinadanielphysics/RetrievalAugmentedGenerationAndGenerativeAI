# Use an official Python runtime as the base image
FROM python:3.11

EXPOSE 8080

ENV APP_HOME /ArXiv
WORKDIR $APP_HOME
COPY . ./

# Install the Python dependencies
RUN pip install -r requirements.txt

# Run the Streamlit application
CMD streamlit run --server.port 8080 app.py
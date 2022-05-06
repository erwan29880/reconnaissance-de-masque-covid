FROM aminehy/docker-streamlit-app:latest


RUN apt-get update && apt-get install -y
RUN apt-get install libgl1-mesa-glx -y
RUN python -m pip install --upgrade pip
RUN python -m pip install matplotlib numpy opencv-python pandas openpyxl streamlit keras tensorflow


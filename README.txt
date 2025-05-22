# I. No Docker

# Activate env
$ pipenv shell

# Install dependencies
$ pipenv install

./run.sh
python run.py

# II. With Docker

$ (sudo) docker build -t flaskapp:latest .
$ (sudo) docker run -it -d -p 5000:5000 flaskapp
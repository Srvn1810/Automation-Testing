#1. Using the Python PIP command creates a "Requirement.txt" file from the terminal/ command-prompt of your system?
import pip

pip freeze > requirements.txt
pip install -r requirements.txt

#2. Using the Python PIP Command install the Flask Moduel <2.0 into your system?

pip install Flask==1.1.2
pip install "Flask<2.0"



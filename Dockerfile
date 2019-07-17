FROM python:3
ADD my_script.py /
ADD myfile.txt /
CMD [ "python", "./my_script.py" ]
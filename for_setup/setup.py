from setuptools import setup

setup(
    name='Personal_assistant',
    version='0.0.1',
    description='Group-12 team project',
    authors='PythonWizards',
    install_requires=[
        'dateparser==1.0.0'
        'prompt_toolkit==3.0.21'
        'folium==0.12.1'
        'requests==2.26.0'
        'pygame==2.0.1'
        'colorama==0.4.4'
        'dill>=0.3.7'
        ],
)

# $env:PYTHONPATH = "C:\шлях\до\папки\з_цим_файлом" + $env:PYTHONPATH (треба ввести в першу чергу, вказавши адресу папки з кодом)
# pip install -r requirements (встановлює всі нетсандартні бібліоткеи що були використані в коді)
# pip install Personal_assistant (встановлює як пакет)
# python Personal_assistant.py запускає


# pip uninstall my_code (видаляє пакет)
# pip uninstall -r requirements (видаляє нетсандартні бібліоткеи що були використані в коді)
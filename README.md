[![Python application](https://github.com/Muhammad-Usman-972/MLOPs_Task/actions/workflows/python-app.yml/badge.svg)](https://github.com/Muhammad-Usman-972/MLOPs_Task/actions/workflows/main_branch_python-app.yml)
# MLOPs_Task

## For Windows
### create a virtual environment
```bash
python -m venv venv_name
```
### set execution policy
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
### activate the virtual environment
```bash
source venv_name/Scripts/activate
```
### Create requirements.txt 
```bash
touch requirements.txt
```
### Add the following to requirements.txt
```
black
pytest
```
### run makefile
```bash
make install
```
### run tests
```bash
make test
```
### run lint
```bash
make lint
```

python -m venv venv
call venv\Scripts\activate

python -m pip install --upgrade pip
pip install pyhamcrest
pip install coverage
pip install mock
pip install pyqt5
pip install pyqt5-tools

call deactivate
pause

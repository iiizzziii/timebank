1 - mariadb install - https://mariadb.com/downloads/community/ (OS = windows)

  automaticky sa stiahne klikatko heidiSQL (to iste ako dbeaver) - v nom vytvorit projekt (meno + heslo vam bude treba vo flasku)

2 - mariadb connector - https://mariadb.com/downloads/connectors/connectors-data-access/ (product = C connector / OS = windows)

3 - do virtual enviromentu instalovat:

    pip install flask
    pip install PyMySQL
    pip install SQLAlchemy
    pip install mariadb
    pip install mariadb SQLAlchemy
    
 4 - flask spustam v cmd cez prikaz: py app.py 
 
  (ak pouzivate powershell:  $env:FLASK_APP = "app.py" / $env:FLASK_ENV = "development" / flask run)

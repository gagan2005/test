# test

First install the required pip packages by using the \
```pip install -r requirements.txt```

For loading data into tables run the \
```python3 initdb.py```

Make sure to configure username and password of your postgres server in initdb.py and main.py 

To run the server ,run the \
```uvicorn main:app --reload```


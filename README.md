# Booking Hotels


1. Create envirotment:\
```python -m venv venv```
2. Activate Envirotment:\
```venv\Scripts\activate.bat``` - For Windows \
```source venv/bin/activate``` - For Linux и MacOS
3. Install dependencies:\
```pip install -r requirements.txt```
4. Install DB from docker-Compose 
``` docker-compose up -d ```
5. excute migrations that are in head
``` alembic upgrade head ```
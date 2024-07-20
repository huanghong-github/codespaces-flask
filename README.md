## uvicorn

```
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 --reload
```

## gunicorn

```
gunicorn -c gunicorn_conf.py main:app
```

## docker

```
docker-compose up
```

## 单元测试

```python
export PYTHONPATH="."
python app/tests/test_user.py
```

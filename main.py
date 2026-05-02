import time
from functools import wraps

def o'lchang_bajarilish_vaqti(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funksiya {func.__name__} bajarilish vaqti: {end_time - start_time} soniya")
        return result
    return wrapper

@o'lchang_bajarilish_vaqti
def yozuvni_yozish(text):
    time.sleep(2)  # 2 soniyani kutib turadi
    print(text)

yozuvni_yozish("Salom, dunyo!")
```

```python
import time
from functools import wraps

def o'lchang_bajarilish_vaqti(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funksiya {func.__name__} bajarilish vaqti: {end_time - start_time} soniya")
        return result
    return wrapper

@o'lchang_bajarilish_vaqti
def yozuvni_yozish(text):
    time.sleep(2)  # 2 soniyani kutib turadi
    print(text)

yozuvni_yozish("Salom, dunyo!")

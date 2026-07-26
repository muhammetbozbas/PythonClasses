from functools import wraps
def log_data(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """wrapper hakkinda bilgilendir"""
        print(f"Metot ismi: {fn.__name__}")
        print(f"Metot bilgisi: {fn.__doc__}")
        return fn(*args,**kwargs)
    return wrapper



@log_data
def add(a,b):
    """fonksiyona gönderilen iki sayiyi toplar."""
    return a+b

# print(add(10,20))
print(add.__name__)
print(add.__doc__)
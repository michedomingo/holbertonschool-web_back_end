# 0x0B. Redis basic

## Resources:books:

Read or watch:

- [Redis commands](https://redis.io/commands)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

---

## Learning Objectives:bulb:

What you should learn from this project:

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache

---

### [0. Writing strings to Redis](./exercise.py)

- Create a Cache class. In the **init** method, store an instance of the Redis client as a private variable named \_redis and flush the instance using flushdb.

### [1. Reading from Redis and recovering original type](./exercise.py)

- Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

### [2. Incrementing values](./exercise.py)

- Familiarize yourself with the INCR command and its python equivalent.

### [3. Storing lists](./exercise.py)

- Familiarize yourself with redis commands RPUSH, LPUSH, LRANGE, etc.

### [4. Retrieving lists](./exercise.py)

- In this tasks, we will implement a replay function to display the history of calls of a particular function.

### [5. Implementing an expiring web cache and tracker](./web.py)

- In this tasks, we will implement a get_page function. The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.

---

## Author

- **Michelle Domingo** - [michedomingo](https://github.com/michedomingo)

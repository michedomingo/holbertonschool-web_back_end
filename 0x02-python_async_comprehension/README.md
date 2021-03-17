# 0x02. Python - Async Comprehension

## Resources:books:

Read or watch:

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](http://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/type-hinting-generator-in-python-3-6)

---

## Learning Objectives:bulb:

What you should learn from this project:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

---

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.x)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(**import**("my_module").**doc**)')
- All your functions should have a documentation (python3 -c 'print(**import**("my_module").my_function.**doc**)'
- All your functions and coroutines must be type-annotated.

---

### [0. Async Generator](./0-async_generator.py)

- Write a coroutine called async_generator that takes no arguments.

### [1. Async Comprehensions](./1-async_comprehension.py)

- Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

### [2. Run time for four parallel comprehensions](./2-measure_runtime.py)

- Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

---

## Author

- **Michelle Domingo** - [michedomingo](https://github.com/michedomingo)

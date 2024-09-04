
<p align="center">
  <img src="https://github.com/user-attachments/assets/c7ab9d75-99f8-4b33-919b-de93cbbd3c44" alt="pythonpuggie">
</p>


# Python- Async Function
This project covers asynchronous programming in Python using coroutines and the `async/await` syntax to handle concurrent tasks. It demonstrates managing multiple asynchronous operations, measuring performance, and creating tasks with the asyncio library.
It covers concepts like running coroutines concurrently, measuring execution time, and managing tasks which is ideal for optimizing I/O-bound operations such as web requests or database queries.

## Learning Objectives
<details>
<summary>1. Understand and Use `async` and `await` Syntax in Python</summary>

   In this project, I learned to use `async` and `await` to define and run asynchronous functions. For example, in **Task 0**, I implemented `wait_random`, an asynchronous coroutine that uses `await asyncio.sleep(delay)` to wait for a random delay:

   ```python
   async def wait_random(max_delay: int = 10) -> float:
       '''
       Asynchronous coroutine that waits for a random delay
       between 0 and max_delay seconds and returns it.
       '''
       delay = random.uniform(0, max_delay)
       await asyncio.sleep(delay)
       return delay
   ```
</details>
  
<details>
<summary>2. Execute Asynchronous Programs Using `asyncio`</summary>

   I executed asynchronous programs using the `asyncio.run()` function. In **Task 1**, I ran the `wait_n` coroutine that executes multiple instances of `wait_random` concurrently:

   ```python
   import asyncio

   async def wait_n(n: int, max_delay: int) -> List[float]:
       '''
       Runs `wait_random` n times with a maximum delay of `max_delay`
       and returns the delays in ascending order.
       '''
       tasks = [wait_random(max_delay) for _ in range(n)]
       delays = [await task for task in asyncio.as_completed(tasks)]
       return delays

   asyncio.run(wait_n(5, 5))
   ```
</details>

<details>
<summary>3. Run Concurrent Coroutines Effectively</summary>

   I learned to run coroutines concurrently using `asyncio.gather` or `asyncio.as_completed`. In **Task 4**, I implemented `task_wait_n`, which runs multiple tasks concurrently using `asyncio.as_completed`:

   ```python
   async def task_wait_n(n: int, max_delay: int) -> List[float]:
       '''
       Runs `task_wait_random` n times with a maximum delay of `max_delay`
       and returns the delays in ascending order.
       '''
       tasks = [task_wait_random(max_delay) for _ in range(n)]
       delays = [await task for task in asyncio.as_completed(tasks)]
       return delays
   ```

   This function gathers results as they complete, allowing efficient concurrency management.
   </details>

<details>
<summary>4. Create and Manage `asyncio` Tasks</summary>

   I created and managed tasks using the `asyncio.create_task()` method. In **Task 3**, I implemented `task_wait_random` that creates and returns an `asyncio.Task`:

   ```python
   def task_wait_random(max_delay: int) -> asyncio.Task:
       '''
       Returns an asyncio.Task that runs the `wait_random` coroutine
       with the given `max_delay`.
       '''
       return asyncio.create_task(wait_random(max_delay))
   ```

   In **Task 4**, I used these tasks to run multiple asynchronous operations concurrently and handled their results effectively.
</details>

<details>
<summary>5. Use the `random` Module in Asynchronous Contexts</summary>

   I used the `random` module to generate random delay values in an asynchronous context. In **Task 0**, the `wait_random` coroutine uses `random.uniform` to create a random float between `0` and `max_delay`:

   ```python
   delay = random.uniform(0, max_delay)
   await asyncio.sleep(delay)
   return delay
   ```

   This random delay is then used to simulate asynchronous operations that complete at unpredictable times.

</details>

### Resources

- [Real Python - Async IO in Python](https://realpython.com/async-io-python/)
- [Python Docs - asyncio](https://docs.python.org/3/library/asyncio.html)
- [Python Docs - random module](https://docs.python.org/3/library/random.html#random.uniform)

### Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- `aiohttp` for HTTP requests

### Basic Concepts

- **Coroutine**: A special type of function that can pause execution and yield control back to the event loop, allowing other tasks to run.
- **Event Loop**: The core of every `asyncio` application that schedules and executes tasks, manages I/O operations, and handles events.
- **`async` Keyword**: Used to define a coroutine. Example: `async def foo(): pass`
- **`await` Keyword**: Used inside an `async` function to call another async function and wait for its result.


<details>
<summary>Python - Asynchronous execution </summary>
Coroutines and the async/await syntax in Python are used to write asynchronous code that can perform tasks concurrently without the need for threads or processes. This is particularly useful for I/O-bound tasks, like web requests or database queries, where you’d otherwise be waiting for a response and wasting CPU cycles and where traditional threading or multiprocessing might be overkill or introduce unnecessary complexity.

Basic Concepts:
Coroutine: A coroutine is a special type of function that can pause its execution and yield control back to the event loop, allowing other tasks to run. It can later resume from where it left off.

Event Loop: The event loop is the core of every asyncio application. It schedules and executes tasks and callbacks, manages I/O operations, and handles events.

async: This keyword is used to define a coroutine. For example, async def foo(): pass defines a coroutine named foo.

await: This keyword is used inside an async function to call another async function and wait for its result. It essentially yields control back to the event loop.

Basic Example:
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def say_world():
    await asyncio.sleep(1)
    print("World")

async def main():
    await say_hello()
    await say_world()

asyncio.run(main())
In this example, the main coroutine calls say_hello and then say_world. Each of these coroutines sleeps for 1 second using asyncio.sleep (an asynchronous sleep) and then prints a message. The program will take 2 seconds to complete because the coroutines are awaited one after the other.

Concurrent Execution:
To run multiple coroutines concurrently, you can use asyncio.gather:

async def main():
    await asyncio.gather(say_hello(), say_world())
Now, “Hello” and “World” will be printed almost simultaneously, and the program will take approximately 1 second to complete.

Real-world Example:
Consider a scenario where you want to fetch multiple web pages concurrently:

import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    tasks = [fetch_url(url) for url in urls]
    pages = await asyncio.gather(*tasks)
    for url, page in zip(urls, pages):
        print(f"Content from {url}: {len(page)} bytes")

asyncio.run(main())
In this example, we’re using the aiohttp library to fetch web pages asynchronously. The main coroutine creates a list of tasks to fetch each URL and then gathers the results. This allows fetching all the URLs concurrently, which is much faster than fetching them one by one.

Can coroutines replace multi-threading?
Coroutines and multi-threading are both mechanisms to achieve concurrency, but they serve different purposes and have different strengths and weaknesses. Whether coroutines can replace multi-threading depends on the specific use case.

Coroutines:
Nature: Coroutines are cooperative, meaning that they decide when to give up control. This is done using the await keyword in Python’s asyncio. This allows other coroutines to run.

Use Cases: Coroutines are best suited for I/O-bound tasks, like reading/writing to files, network operations, or any task where the program spends a lot of time waiting.

Advantages:

Lightweight: You can have thousands or even millions of coroutines without the overhead of threads.
Deterministic: Since there’s no preemption by an external scheduler, the points where context switches happen are explicit and predictable.
Avoids many concurrency problems: Since only one coroutine runs at a time in a single-threaded event loop, you don’t have to worry about race conditions in the same way as with threads.
Limitations:

CPU-bound tasks: Coroutines run in a single thread. If you have a CPU-bound task, it can block the event loop, making all other tasks wait.
Need for async/await: Existing synchronous code and libraries need to be adapted to be used in an asynchronous context.
Multi-threading:
Nature: Threads are preemptive, meaning the OS decides when to switch between threads, which can happen at any point.

Use Cases: Threads can be used for both I/O-bound and CPU-bound tasks. They allow multiple operations to run in parallel on multi-core processors.

Advantages:

True parallelism: On multi-core systems, multiple threads can run in parallel, making full use of the CPU.
Easier integration: Many existing libraries are thread-safe or can be used in a multi-threaded context without modification.
Limitations:

Overhead: Threads have a significant memory and context-switching overhead.
Concurrency issues: Race conditions, deadlocks, and other concurrency-related problems can be challenging to debug and solve.
Global Interpreter Lock (GIL) in CPython: In the standard Python interpreter (CPython), the GIL prevents multiple native threads from executing Python bytecodes at once. This means that multi-threading is not always effective for CPU-bound tasks in Python.
Coroutines can’t universally replace multi-threading, but they offer a more efficient and often simpler way to handle concurrency for I/O-bound tasks. For CPU-bound tasks, especially in languages or environments without a GIL-like mechanism, multi-threading or multiprocessing might be more appropriate.

In many modern applications, a combination of both coroutines and threads (or processes) is used to achieve the desired performance and responsiveness. For example, you might use an asynchronous framework for handling I/O and background threads for CPU-intensive computations.
</details>

<details>
<summary>Python - Asynchronous Programming </summary>
What is Asynchronous Programming?
In traditional synchronous programming, each operation is executed one after the other. If one operation takes time (like fetching data from the internet), the entire program waits and nothing else progresses.

Asynchronous programming allows certain operations to be executed in the “background”, freeing up the main program to continue running. This is especially useful for I/O-bound operations like network requests, file operations, etc.

The Event Loop
The heart of asynchronous programming in Python is the “event loop”. Think of it as a constantly running loop that checks if there are any tasks to run. If there are tasks, it runs them; if not, it keeps looping.

Tasks can be scheduled to run on the event loop, and the loop will execute them when it can. The event loop can handle many tasks by quickly switching between them, giving the illusion that they’re running at the same time.

Async/Await
async and await are keywords introduced in Python to make asynchronous programming more readable and straightforward.

async defines an asynchronous function. This function doesn’t run immediately; instead, it returns a coroutine object.
await is used to call an asynchronous function and wait for it to complete.
Simple Example:
Let’s say we want to simulate a function that waits for a while:

import asyncio

async def say_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

# Running the asynchronous function
async def main():
    print("Started")
    await say_after(1, "Hello")
    await say_after(2, "World")
    print("Finished")

# Python 3.7+
asyncio.run(main())

In this example:

say_after is an asynchronous function because of the async keyword.
Inside say_after, we use await to pause the function for a specified delay. During this pause, the event loop can do other things.
In the main function, we call say_after twice. The second call won’t start until the first one is finished because of the await keyword.
asyncio.run(main()) is used to run the main coroutine and start the event loop.
How does this differ from synchronous code?
If this were synchronous code, the entire program would stop during the sleep calls. But with async/await, other tasks could run during those pauses.

More Complex Example: Running Tasks Concurrently
What if we want both messages to print after waiting for 3 seconds, without waiting for the first task to complete?

async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))

    print("Started")

    # Wait until both tasks are completed
    await task1
    await task2

    print("Finished")

asyncio.run(main())

Here, asyncio.create_task() schedules the coroutines to run on the event loop, but doesn’t wait for them to complete. Both say_after calls run “concurrently”, making the program faster.

In Summary:
Asynchronous programming allows multiple tasks to run seemingly in parallel, making efficient use of resources.
The event loop is the core of this mechanism, constantly checking and running tasks as they’re scheduled.
async/await provides a readable way to write asynchronous code in Python.
Remember, async/await is best suited for I/O-bound and high-level structured network code, not for CPU-bound tasks. For CPU-bound tasks, you might want to look into multi-threading or multi-processing in Python.
</details>

### Getting Started
<details>
<summary>
To run the examples in this project, you need to have Python 3.9 installed on Ubuntu 20.04 LTS. Here's what I did, but there are certainly other ways to achieve the same setup:</summary>

1. **Add the Deadsnakes PPA and Install Python 3.9**:

    I first updated the package list and added the Deadsnakes PPA to install Python 3.9:

    ```bash
    sudo apt update
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.9 python3.9-venv
    ```

2. **Create and Activate a Virtual Environment**:

    After installing Python 3.9, I created and activated a virtual environment:

    ```bash
    python3.9 -m venv venv
    source venv/bin/activate
    ```

3. **Install Necessary Packages**:

    I installed the necessary packages for the project. This project uses **aiohttp** for asynchronous HTTP requests:

    ```bash
    pip install aiohttp
    ```

These steps worked for me, but there are other methods to set up Python and the required environment depending on your system preferences and configurations.

</details>

## Tasks and Detailed Usage

### Task 0: The Basics of Async
<details>
<summary>
Write an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
Use the random module.</summary>

**Code:**

**File:** `0-basic_async_syntax.py`

```python
#!/usr/bin/env python3
'''
This module contains an asynchronous coroutine that waits for a random
delay between 0 and max_delay seconds and returns the delay.
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and returns it.
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
```

**Explanation:**

- The function `wait_random` is defined with a parameter `max_delay` annotated as an integer, with a default value of 10.
- It generates a random float value between 0 and `max_delay` using `random.uniform(0, max_delay)`.
- The function uses `await asyncio.sleep(delay)` to asynchronously wait for the generated delay.
- The function returns the delay as a float.

**Usage:**

To test the coroutine, use the provided main script (`0-main.py`):

**File:** `0-main.py`

```python
#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

**Run the main script:**

```bash
chmod +x 0-main.py
./0-main.py
```

**Expected Output:**

The output will be a series of random float numbers representing the delay time, for example:

```
9.034261504534394
1.6216525464615306
10.634589756751769
```

This output confirms that the coroutine correctly waits for a random delay between 0 and `max_delay` seconds and returns the delay time as expected.

</details>


### Task 1: Execute Multiple Coroutines Concurrently
<details>
<summary>Import wait_random from the previous python file that you’ve written and write an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.</summary>


**Code:**

**File:** `1-concurrent_coroutines.py`

```python
#!/usr/bin/env python3
'''
This module has a coroutine `wait_n` that runs `wait_random` multiple times
and returns a sorted list of delays.
'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs `wait_random` n times with a maximum delay of `max_delay`
    and returns the delays in ascending order.
    '''
    # list of tasks to run concurrently
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # gather results as they complete
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
```

**Explanation:**

- The function `wait_n` runs the `wait_random` coroutine `n` times concurrently with a maximum delay of `max_delay`.
- Uses `asyncio.as_completed` to gather the results as they complete, ensuring the delays are in ascending order.

**Usage:**

To test the function, use the provided main script (`1-main.py`):

**File:** `1-main.py`

```python
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

**Run the main script:**

```bash
chmod +x 1-main.py
./1-main.py
```

**Expected Output:**

The output will be a list of random float numbers representing the delay times, sorted in ascending order, for example:

```
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```
</details>


### Task 2: Measure the Runtime

<details>
<summary>From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.</summary>


**Code:**

**File:** `2-measure_runtime.py`

```python
#!/usr/bin/env python3
'''
This module contains a function `measure_time` that measures the average
runtime of the `wait_n` coroutine.
'''

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time for `wait_n(n, max_delay)` and
    returns the average time per call.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
```

**Explanation:**

- The `measure_time` function:
  - Records the start time before running the `wait_n` coroutine.
  - Runs `wait_n` using `asyncio.run()` to execute it asynchronously.
  - Calculates the total elapsed time by subtracting the start time from the time after execution.
  - Returns the average runtime per call (`total_time / n`).

**Usage:**

To test the function, use the provided main script (`2-main.py`):

**File:** `2-main.py`

```python
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

**Run the Main Script:**

```bash
chmod +x 2-main.py
./2-main.py
```

**Expected Output:**

The output will display the average time taken per call, for example:

```
1.759705400466919
```
</details>

### Task 3: Tasks
<details>
<summary>Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function, use the regular function syntax to do this) task_wait_random that takes an integer max_delay and returns a asyncio.Task.</summary>


**Code:**

**File:** `3-tasks.py`

```python
#!/usr/bin/env python3
'''
This module contains a function `task_wait_random` that returns an asyncio.Task.
'''

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Returns an asyncio.Task that runs the `wait_random` coroutine
    with the given `max_delay`.
    '''
    return asyncio.create_task(wait_random(max_delay))
```

**Explanation:**

- The `task_wait_random` function:
  - Takes an integer `max_delay` as an argument.
  - Uses `asyncio.create_task()` to create and return a task that runs `wait_random` with the specified `max_delay`.

**Usage:**

To test the function, use the provided main script (`3-main.py`):

**File:** `3-main.py`

```python
#!/usr/bin/env python3

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

**Run the Main Script:**

Make the script executable and run it:

```bash
chmod +x 3-main.py
./3-main.py
```

**Expected Output:**

The output should confirm that the returned object is an `asyncio.Task`:

```
<class '_asyncio.Task'>
```

This confirms that the function correctly creates an asyncio task to run the `wait_random` coroutine.
</details>

### Task 4: Tasks
<details>
<summary>Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.</summary>

**Code:**

**File:** `4-tasks.py`

```python
#!/usr/bin/env python3
'''
This module contains a function `task_wait_n` that runs multiple
tasks using `task_wait_random` and returns a sorted list of delays.
'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs `task_wait_random` n times with a maximum delay of `max_delay`
    and returns the delays in ascending order.
    '''
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Gather results as they complete
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
```

**Explanation:**

- The `task_wait_n` function:
  - Uses `task_wait_random` from Task 3 to create a list of tasks.
  - Runs these tasks concurrently and collects their results as they complete, ensuring the delays are in ascending order.

**Usage:**

To test the function, use the provided main script (`4-main.py`):

**File:** `4-main.py`

```python
#!/usr/bin/env python3

import asyncio
task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```

**Run the Main Script:**

Make the script executable and run it:

```bash
chmod +x 4-main.py
./4-main.py
```

**Expected Output:**

The output will display a list of delays in ascending order, for example:

```
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```

This confirms that the function correctly creates multiple tasks and returns their results in ascending order.
</details>

## Author

Vie Paula - [GitHub Profile](https://github.com/ThatsVie)

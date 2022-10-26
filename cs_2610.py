import time

def time_of_function(function, function2):
    def wrapped(string):
        start_time = time.perf_counter_ns()
        function(string)
        res = time.perf_counter_ns() - start_time
        start_time = time.perf_counter_ns()
        function2(string)
        res2 = time.perf_counter_ns() - start_time
        if res < res2: print(res)
        else: print(res2)
    return wrapped

def counter_1(strinu):
    stu = strinu.lower()
    count = 0
    for i in set(stu):
        if stu.count(i) > 1:
            count += 1
    return count

def counter_2(s):
    return len([ch for ch in (set(s.lower())) if s.lower().count(ch) > 1])

#тесты говно
res = time_of_function(counter_1, counter_2)
res("aabbcc")

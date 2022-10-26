import time

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

@time_of_function
def counter_1(strinu):
    stu = strinu.lower()
    count = 0
    for i in set(stu):
        if stu.count(i) > 1:
            count += 1
    return count

@time_of_function
def counter_2(s):
    return len([ch for ch in (set(s.lower())) if s.lower().count(ch) > 1])

#тесты говно

print(counter_1("aaabbbc"))
print(counter_2("aaabbbc"))

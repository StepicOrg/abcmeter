import os
from datetime import datetime

from antlr4 import FileStream

from abcmeter import CPP, JAVA, PYTHON, calculate_abc_score

language_by_extension = {
    '.cpp': CPP,
    '.java': JAVA,
    '.py': PYTHON,
}


def get_language_by_file(file_name):
    _, extension = os.path.splitext(file_name)

    return language_by_extension[extension]


def profiling():
    file_name = 'cpp/tests/main.cpp'
    language = get_language_by_file(file_name)

    print(f'Profiling for {language} in {file_name}')

    times = list()
    for i in range(10):
        input = FileStream(file_name, encoding='utf8')
        start_time = datetime.now()
        listener = calculate_abc_score(input, language)
        delta_time = datetime.now() - start_time
        times.append(delta_time.total_seconds() * 1000)

    print('a: ' + str(listener.a))
    print('b: ' + str(listener.b))
    print('c: ' + str(listener.c))
    print('ABC score: ' + str(listener.abc_score))
    print()

    mid = sorted(times[1:])[(len(times) - 1) // 2]
    caching_time = times[0] - mid
    print(f'caching time: {format(caching_time, ".5f")}ms')
    print(f'min: {format(min(times[1:]), ".5f")}ms')
    print(f'mid: {format(mid, ".5f")}ms')
    print(f'max: {format(max(times[1:]), ".5f")}ms')


if __name__ == '__main__':
    profiling()

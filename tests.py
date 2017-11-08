import os
from contextlib import contextmanager
from datetime import datetime

from abcmeter import CPP, JAVA, PYTHON, calculate_abc_score


def print_with_time_label(start_time, content, end='\n'):
    delta_time = datetime.now() - start_time
    print(f'{format(delta_time.total_seconds(), ".5f")}: {content}', end=end)


@contextmanager
def print_process(start_time, process_name):
    print_with_time_label(start_time, process_name + ' start')
    yield
    print_with_time_label(start_time, process_name + ' done')


language_by_extension = {
    '.cpp': CPP,
    '.java': JAVA,
    '.py': PYTHON,
}


def get_language_by_file(file_name):
    _, extension = os.path.splitext(file_name)

    return language_by_extension[extension]


def main():
    file_name = 'cpp/tests/main.cpp'
    language = get_language_by_file(file_name)

    start_time = datetime.now()

    listener = calculate_abc_score(start_time, file_name, language, print_process)

    print_with_time_label(start_time, 'a: ' + str(listener.a))
    print_with_time_label(start_time, 'b: ' + str(listener.b))
    print_with_time_label(start_time, 'c: ' + str(listener.c))
    print_with_time_label(start_time, 'ABC score: ' + str(listener.abc_score))


if __name__ == '__main__':
    main()

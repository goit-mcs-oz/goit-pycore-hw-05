# Завдання 3

from collections import defaultdict
from pathlib import Path
from sys import argv


def parse_log_line(line: str) -> dict:
    line_list = line.strip().split()
    data, time, level, *message = line_list
    return {'data': data,
            'time': time,
            'level': level,
            'message': " ".join(message)}


def load_logs(file_path: str) -> list:
    logs_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if len(lines) == 0:
            return []
        for item in lines:
            logs_list.append(parse_log_line(item))
        return logs_list


def filter_logs_by_level(logs: list, level: str) -> list:
    return [item for item in logs if item['level'].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    logs_by_level = defaultdict(int)
    for item in logs:
        logs_by_level[item['level']] += 1
    return logs_by_level


def display_log_counts(counts: dict):
    print('Рівень логування'.ljust(20, ' '), "|", 'Кількість'.ljust(10, ' '))
    print(''.ljust(20, '-'), "|", ''.ljust(10, '-'))
    for key, value in counts.items():
        if key == 'ERROR':
            print(f'\033[34m{key}\033[0m'.ljust(29, ' '),
                  "|", str(value).ljust(10, ' '))
        else:
            print(key.ljust(20, ' '), "|", str(value).ljust(10, ' '))


if len(argv) > 1:
    file_path = Path(argv[1])
    level = None
    if len(argv) > 2:
        level = argv[2]
    if (file_path.exists()):
        try:
            logs = load_logs(file_path)
            log_counts = count_logs_by_level(logs)
            display_log_counts(log_counts)
            if (level):
                logs_filtered = filter_logs_by_level(logs, level)
                if len(logs_filtered):
                    print(f"\nДеталі логів для рівня '{level.upper()}':")
                    for item in logs_filtered:
                        data, time, _, message = item.values()
                        y, m, d = data.split('-')
                        data_string = f'{y}\033[32m-{m}-{d}\033[0m'
                        print(f'{data_string} {time} - {message}')
        except Exception as e:
            print(f"Помилка: {e}")
    else:
        print("Вкажіть коректний шлях до файлу")

# ============================================================
# Самостоятельная работа от 29.09.26
# Программа для деканата
# ============================================================

def input_students():
    """Возвращает тестовый массив студентов: [ID, ФИО, Средний_балл]."""
    return [
        [103, "Пермяков Афанасий Тарасович", 4.5],
        [101, "Петров Пётр Петрович",   3.2],
        [107, "Сидоров Сидор Сидорович", 2.8],
        [102, "Кузнецова Анна Сергеевна", 4.9],
        [105, "Смирнов Олег Иванович",  2.5],
        [104, "Волкова Мария Андреевна", 3.8],
        [106, "Морозов Дмитрий Львович", 4.1],
    ]


def sort_by_score(students):
    """Сортировка по среднему баллу (Bubble Sort), по убыванию."""
    # Guard clause: пустой массив
    if not students:
        return []
    a = [row[:] for row in students]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j][2] < a[j + 1][2]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def top3(students):
    """Возвращает Топ-3 студента по среднему баллу."""
    if not students:
        return []
    sorted_students = sort_by_score(students)
    return sorted_students[:3]


def group_stats(students):
    """Возвращает (средний балл группы, количество двоечников)."""
    if not students:
        return (0, 0)
    total = 0
    losers = 0
    for s in students:
        total += s[2]
        if s[2] < 3:
            losers += 1
    return (total / len(students), losers)


def sort_by_id(students):
    """Сортировка студентов по ID (по возрастанию)."""
    if not students:
        return []
    a = [row[:] for row in students]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def binary_search_by_id(students, target_id, left=None, right=None):
    """Рекурсивный бинарный поиск студента по ID."""
    if left is None:
        left = 0
    if right is None:
        right = len(students) - 1

    if left > right:
        return None

    mid = (left + right) // 2
    if students[mid][0] == target_id:
        return students[mid]
    if students[mid][0] < target_id:
        return binary_search_by_id(students, target_id, mid + 1, right)
    return binary_search_by_id(students, target_id, left, mid - 1)


def main():
    students = input_students()

    print("=" * 60)
    print("Исходный список студентов:")
    print("=" * 60)
    for s in students:
        print(f"ID={s[0]:>4} | {s[1]:<30} | балл = {s[2]:.2f}")
    print()

    # --- Задача 1. Топ-3 ---
    print("=" * 60)
    print("Топ-3 студента по среднему баллу")
    print("=" * 60)
    for i, s in enumerate(top3(students), start=1):
        print(f"{i}. ID={s[0]:>4} | {s[1]:<30} | балл = {s[2]:.2f}")
    print()

    # --- Задача 2. Статистика ---
    print("=" * 60)
    print("Статистика группы")
    print("=" * 60)
    avg, losers = group_stats(students)
    print(f"Средний балл по группе: {avg:.3f}")
    print(f"Количество двоечников (балл < 3): {losers}")
    print()

    # --- Задача 3. Поиск по ID ---
    print("=" * 60)
    print("Поиск студента по ID (рекурсивный бинарный поиск)")
    print("=" * 60)
    sorted_by_id = sort_by_id(students)
    print("Массив, отсортированный по ID:")
    for s in sorted_by_id:
        print(f"  ID={s[0]:>4} | {s[1]}")
    print()

    for target_id in [104, 101, 999]:
        result = binary_search_by_id(sorted_by_id, target_id)
        if result:
            print(f"ID={target_id}: найден -> {result[1]} (балл {result[2]:.2f})")
        else:
            print(f"ID={target_id}: не найден")


if __name__ == "__main__":
    main()
"""Точка входа демонстрации лабораторной работы №3."""

from models import ExtendedList, ShapeFactory, Student


def main() -> None:
    print("=== Лабораторная работа № 3 (Вариант 2) ===")

    # Задание 2 (средняя): Класс Студент
    print("\n1. Класс «Студент»:")
    alice = Student("Алиса Селезнёва", "ИПМКН-21", 4.88)
    bob = Student("Борис Летов", "ИПМКН-21", 4.62)
    print(alice.display_info())
    print(bob.display_info())

    # Задание 7 (средняя): Перегрузка оператора +
    print("\n2. Перегрузка оператора + (объединение в проект):")
    project_collab = alice + bob
    print(project_collab)

    # Задание 4 (средняя) + Задание 2 (повышенная): Фигуры и Factory
    print("\n3. Фабрика фигур (ShapeFactory):")
    triangle = ShapeFactory.produce("triangle", 6.0)
    ellipse = ShapeFactory.produce("ellipse", 5.0, 3.0)

    print(
        f"Треугольник со стороной 6: Площадь = {triangle.area():.2f}, "
        f"Периметр = {triangle.perimeter():.2f}"
    )
    print(
        f"Эллипс (5x3): Площадь = {ellipse.area():.2f}, "
        f"Периметр = {ellipse.perimeter():.2f}"
    )

    # Задание 6 (повышенная): Расширение встроенного list
    print("\n4. Расширенный список (ExtendedList):")
    sample_data = ExtendedList([4, 7, 2, 4, 10, 15, 2, 8])
    print(f"Исходный список: {sample_data}")
    print(f"Среднее: {sample_data.compute_mean():.2f}")
    print(f"Только чётные: {sample_data.select_evens()}")
    print(f"Без дубликатов: {sample_data.drop_duplicates()}")


if __name__ == "__main__":
    main()
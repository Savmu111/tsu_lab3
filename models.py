from abc import ABC, abstractmethod
import math
from typing import List


class Student:
    """Сущность студента с академическими данными."""

    def __init__(self, full_name: str, group_code: str, rating: float) -> None:
        self.full_name = full_name
        self.group_code = group_code
        self.rating = rating

    def display_info(self) -> str:
        """Формирует строковое представление сведений об учащемся."""
        return (
            f"Обучающийся: {self.full_name} | "
            f"Группа: {self.group_code} | "
            f"Успеваемость: {self.rating:.2f}"
        )

    def __add__(self, other: object) -> "StudentGroup":
        """Объединение двух студентов в совместную проектную ячейку."""
        if not isinstance(other, Student):
            return NotImplemented
        avg_rating = (self.rating + other.rating) / 2
        return StudentGroup(
            members=[self.full_name, other.full_name],
            collective_rating=avg_rating,
        )


class StudentGroup:
    """Проектная группа, полученная путем сложения студентов."""

    def __init__(self, members: List[str], collective_rating: float) -> None:
        self.members = members
        self.collective_rating = collective_rating

    def __str__(self) -> str:
        names = " & ".join(self.members)
        return (
            f"Команда [{names}], средний рейтинг: "
            f"{self.collective_rating:.2f}"
        )


class Shape(ABC):
    """Абстрактная геометрическая фигура."""

    @abstractmethod
    def area(self) -> float:
        """Расчёт площади."""

    @abstractmethod
    def perimeter(self) -> float:
        """Расчёт периметра."""


class Triangle(Shape):
    """Равносторонний треугольник."""

    def __init__(self, side: float) -> None:
        if side <= 0:
            raise ValueError("Сторона треугольника должна быть положительной.")
        self.side = side

    def area(self) -> float:
        return (math.sqrt(3) / 4) * (self.side ** 2)

    def perimeter(self) -> float:
        return 3 * self.side


class Ellipse(Shape):
    """Эллипс с большой и малой полуосями."""

    def __init__(self, semi_major: float, semi_minor: float) -> None:
        if semi_major <= 0 or semi_minor <= 0:
            raise ValueError("Полуоси эллипса должны быть положительными.")
        self.a = semi_major
        self.b = semi_minor

    def area(self) -> float:
        return math.pi * self.a * self.b

    def perimeter(self) -> float:
        return math.pi * (
            3 * (self.a + self.b)
            - math.sqrt((3 * self.a + self.b) * (self.a + 3 * self.b))
        )


class ShapeFactory:
    """Фабричный метод создания экземпляров фигур."""

    @classmethod
    def produce(cls, shape_kind: str, *dimensions: float) -> Shape:
        normalized_kind = shape_kind.strip().lower()

        if normalized_kind == "triangle":
            if len(dimensions) != 1:
                raise ValueError("Для треугольника требуется 1 параметр.")
            return Triangle(dimensions[0])

        if normalized_kind == "ellipse":
            if len(dimensions) != 2:
                raise ValueError("Для эллипса требуется 2 параметра: a и b.")
            return Ellipse(dimensions[0], dimensions[1])

        raise ValueError(
            f"Фигура типа '{shape_kind}' не поддерживается фабрикой."
        )


class ExtendedList(list):
    """Пользовательский список с дополнительными математическими методами."""

    def compute_mean(self) -> float:
        """Вычисляет среднее значение числовых элементов."""
        numeric_items = [x for x in self if isinstance(x, (int, float))]
        if not numeric_items:
            return 0.0
        return sum(numeric_items) / len(numeric_items)

    def select_evens(self) -> "ExtendedList":
        """Возвращает новый ExtendedList только с четными целыми числами."""
        return ExtendedList(
            x for x in self if isinstance(x, int) and x % 2 == 0
        )

    def drop_duplicates(self) -> "ExtendedList":
        """Удаляет повторы с сохранением первоначального порядка."""
        registry = set()
        deduped = ExtendedList()
        for element in self:
            if element not in registry:
                registry.add(element)
                deduped.append(element)
        return deduped
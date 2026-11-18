from datetime import datetime

class Habit:
    def __init__(self, name, difficulty, category, frequency, habit_type):
        self.name = name
        self.difficulty = difficulty.strip().lower()
        self.category = category.strip().lower()
        self.frequency = frequency.strip().lower()
        self.habit_type = habit_type.strip().lower()
        self.created_at = datetime.now()

        if self.difficulty not in ["легкий", "средний", "тяжелый"]:
            raise ValueError("Неизвестная сложность")
        
        if self.category not in ["работа", "учеба", "спорт", "творчество", "разум"]:
            raise ValueError("Неизвестная категория")
        
        if self.habit_type not in ["полезная", "плохая"]:
            raise ValueError("Неизвестный тип привычки")
        
        if self.frequency not in ["ежедневно", "еженедельно", "по выбранным дням"]:
            raise ValueError("Неправильный ввод")
"""    def can_complete():
    def complete():
    def get_completion_history():    """
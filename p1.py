from datetime import datetime

class ProgramArchive:
    def __init__(self, name, os, size_mb, date_recorded):
        self.name = name
        self.os = os
        self.size_mb = size_mb
        self.date_recorded = date_recorded  # очікується рядок у форматі 'YYYY-MM-DD'

    def display_info(self):
        print(f"Назва програми: {self.name}")
        print(f"Операційна система: {self.os}")
        print(f"Розмір програми: {self.size_mb} МБ")
        print(f"Дата запису: {self.date_recorded}")

    def is_for_windows(self):
        return "windows" in self.os.lower()

    def was_added_recently(self, days=30):
        record_date = datetime.strptime(self.date_recorded, '%Y-%m-%d')
        delta = datetime.now() - record_date
        return delta.days <= days

# Приклад створення об'єкта
program1 = ProgramArchive(
    name="Termius",
    os="Windows 11",
    size_mb=138.2,
    date_recorded="2025-06-08"
)

# Виведення інформації
program1.display_info()

# Перевірки
print("\nЧи це програма для Windows?", program1.is_for_windows())
print("Чи була додана нещодавно?", program1.was_added_recently())

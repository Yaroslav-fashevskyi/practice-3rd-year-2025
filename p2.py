from datetime import datetime

# ✅ Базовий клас
class ProgramArchive:
    def __init__(self, name, os, size_mb, date_recorded):
        self.name = name
        self.os = os
        self.size_mb = size_mb
        self.date_recorded = date_recorded  # формат 'YYYY-MM-DD'

    def display_info(self):
        print(f"Назва програми: {self.name}")
        print(f"Операційна система: {self.os}")
        print(f"Розмір програми: {self.size_mb} МБ")
        print(f"Дата запису: {self.date_recorded}")

    def is_for_windows(self):
        return "windows" in self.os.lower()

    def was_added_recently(self, days=30):
        record_date = datetime.strptime(self.date_recorded, '%Y-%m-%d')
        return (datetime.now() - record_date).days <= days

# ✅ Похідний клас
class GameProgram(ProgramArchive):
    def __init__(self, name, os, size_mb, date_recorded, genre, multiplayer):
        super().__init__(name, os, size_mb, date_recorded)
        self.genre = genre
        self.multiplayer = multiplayer

    def display_game_info(self):
        self.display_info()
        print(f"Жанр: {self.genre}")
        print(f"Мультиплеєр підтримується: {'Так' if self.multiplayer else 'Ні'}")

    def is_multiplayer_game(self):
        return self.multiplayer

    def is_large_game(self):
        return self.size_mb > 500  # поріг для "великої" гри

# ✅ Основна частина — 2 гри
def main():
    minecraft = GameProgram(
        name="Minecraft",
        os="Windows 11",
        size_mb=300,
        date_recorded="2025-06-08",
        genre="Sandbox",
        multiplayer=True
    )

    euro_truck = GameProgram(
        name="Euro Truck Simulator 2",
        os="Windows 10",
        size_mb=4000,
        date_recorded="2025-06-05",
        genre="Simulation",
        multiplayer=True
    )

    for game in [minecraft, euro_truck]:
        print("\n=== ІНФОРМАЦІЯ ПРО ГРУ ===")
        game.display_game_info()
        print(f"Велика гра? {'Так' if game.is_large_game() else 'Ні'}")
        print(f"Мультиплеєр? {'Так' if game.is_multiplayer_game() else 'Ні'}")
        print(f"Програма для Windows? {'Так' if game.is_for_windows() else 'Ні'}")
        print(f"Додана нещодавно? {'Так' if game.was_added_recently() else 'Ні'}")

# ▶️ Запуск
main()

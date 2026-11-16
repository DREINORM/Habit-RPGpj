from users import User

player = User("Player")

# Проверка начальных характеристик
assert player.level == 1
assert player.xp == 0
assert player.gold == 0
assert player.health == 100

# Проверка золота
player.add_gold(100)
assert player.spend_gold(50) == True
assert player.gold == 50

assert player.spend_gold(100) == False
assert player.gold == 50

# Проверка здоровья
player.take_damage(30)
assert player.health == 70

player.heal(20)
assert player.health == 90

player.heal(100)
assert player.health == 100

# Проверка смерти
player.take_damage(150)
assert player.health == 0
assert player.is_alive() == False

# Проверка прокачки
player = User("Tester")
player.add_xp(100)

assert player.level > 1

print("Все тесты пройдены!")

# Проверка отрицательного золота
player = User("GoldTester")
player.add_gold(-100)
assert player.gold == 0

# Проверка отрицательного опыта
player.add_xp(-50)
assert player.xp == 0
assert player.level == 1

# Проверка нескольких повышений уровня за раз
player = User("LevelTester")
player.add_xp(1000)
assert player.level > 1
assert player.xp >= 0
assert player.xp < player.get_required_xp()

# Проверка лечения после смерти
player = User("DeadTester")
player.take_damage(150)
player.heal(50)
assert player.health == 0
assert player.is_alive() is False

print("Дополнительные тесты пройдены!")
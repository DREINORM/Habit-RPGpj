class User:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.gold = 0
        self.health = 100


    def add_gold(self, amount):
        if amount < 0:
            return
        
        self.gold += amount

    def take_damage(self, damage):
        if damage <= 0:
            return   
        if not self.is_alive():
            return
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"персонаж {self.name}, умер")
            return

    def heal(self, amount):
        if amount <= 0:
            return
        
        if not self.is_alive():
            
            return
        self.health += amount
        
        if self.health >= 100:
            self.health = 100
            return

    def is_alive(self):
        return self.health > 0 
 
    def get_required_xp(self):
        return int(10 * self.level**1.5)

    def level_up(self):
        required_xp = self.get_required_xp()

        while self.xp >= required_xp:
            self.level += 1
            self.xp -= required_xp
            required_xp = self.get_required_xp()

    def add_xp(self, amount):
        if amount < 0:
            return 
        
        self.xp += amount
        self.level_up()

    def spend_gold(self, price):
        if price <= 0:
            return False
        
        if price > self.gold:
            return False
        
        self.gold -= price
        return True
    
    def show_stats(self):
        print("=================СТАТИСТИКА ПЕРСОНАЖА=================")
        print(f'ИМЯ ПЕРСОНАЖА:{self.name}')
        print(f'УРОВЕНЬ:{self.level}')
        print(f'ОПЫТ:{self.xp}')
        print(f'ЗОЛОТО: {self.gold}')
        print(f'ЗДОРОВЬЕ: {self.health}')
            


        
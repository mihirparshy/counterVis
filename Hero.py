class Heroes:
    def __init__(self, heroes):
        self.heroes = heroes

    def is_hero(self, hero):
        for each in self.heroes:
            if hero.lower() == each.name.lower():
                return True
        return False

    def hero_append(self, hero):
        assert isinstance(hero, Hero)
        self.heroes.append(hero)

    def __str__(self):
        node_str = ""
        for hero in self.heroes:
            node_str += str(hero) + "\n"
        return "HEROES:\n" + node_str

    def get(self, i):
        return self.heroes[i]

    def return_hero(self, hero_str):
        for each in self.heroes:
            if hero_str.lower() == each.name.lower():
                return each
        raise TypeError("What you typed isn't a hero: " + hero_str)


class Hero:
    def __init__(self, name, counters):
        assert isinstance(name, str)
        self.name = str(name)
        self.counters = counters  # would receive another list of hero and weight

    # checks if a hero is counter of the current one
    def is_counter(self, find_hero):
        assert isinstance(find_hero, Hero)
        for i in range(0, len(self.counters)):
            if find_hero.name.lower() == self.counters[i].counter.name.lower():
                return True
        return False

    # returns the counter weight of a hero
    def return_counter_weight(self, find_hero):
        assert isinstance(find_hero, Hero)
        for i in range(0, len(self.counters)):
            if find_hero.name.lower() == self.counters[i].counter.name.lower():
                return self.counters[i].weight
        return 0

    # prints hero's name and counters
    def __str__(self):
        ans = "<" + self.name + ">: "
        for each in self.counters:
            ans += str(each)
        return ans

    # appends a counter to the list
    def add_counter(self, hero_counter, weight):
        assert isinstance(weight, int)
        assert isinstance(hero_counter, Hero)
        self.counters.append(Counter(hero_counter, weight))

    # setters and getters
    def get_name(self):
        return self.name

    def set_counters(self, counters_list):
        self.counters = counters_list

    def get_counters(self):
        return self.counters


class Counter:
    def __init__(self, counter, weight):
        assert isinstance(counter, Hero)
        assert isinstance(weight, int)
        self.counter = counter
        self.weight = int(weight)

    def __str__(self):
        return "(" + self.counter.name + " | " + str(self.weight) + ")"

class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price

atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)


def dijkstrah(starting_city, final_destination):
    cheapest_price_table = {}
    cheapest_previous_stopover_city_table = {}

    unvisited_cities = []
    visited_cities = {}

    cheapest_price_table[starting_city.name] = 0
    current_city = starting_city

    while current_city:
        visited_cities[current_city.name] = True
        try:
            unvisited_cities.remove(current_city)
        except ValueError:
            pass

        for adjacent_city, price in current_city.routes.items():
            if not visited_cities.get(adjacent_city.name):
                unvisited_cities.append(adjacent_city)

            price_through_current_city = cheapest_price_table[current_city.name] + price
            if not cheapest_price_table.get(adjacent_city.name) or \
                price_through_current_city < cheapest_price_table.get(adjacent_city.name):
                cheapest_price_table[adjacent_city.name] = price_through_current_city

                cheapest_previous_stopover_city_table[adjacent_city.name] \
                    = current_city.name


        try:
            current_city = min(unvisited_cities, \
                               key=lambda k: cheapest_price_table[k.name])
        except ValueError:
            break

    shottest_path = []
    current_city_name = final_destination.name
    while current_city_name != starting_city.name:
        shottest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]

    shottest_path.append(starting_city.name)
    shottest_path.reverse()
    for city in shottest_path:
        if shottest_path.index(city) != -1:
            print(city, end="---->")
        else:
            print(city)



print(dijkstrah(atlanta, el_paso))
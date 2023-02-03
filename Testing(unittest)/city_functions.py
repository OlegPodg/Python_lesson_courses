def city_country(city, country, population=None):
    if population:
        total_data = f'{city.title()}, {country.title()} - population {population}'
    else:
        total_data = f'{city.title()}, {country.title()}'

    return total_data


city_country('пекин', 'киТай')

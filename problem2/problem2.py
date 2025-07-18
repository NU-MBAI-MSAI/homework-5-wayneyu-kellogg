def date_format(date):
    components = date.split('/')
    return f'{components[2]}-{components[0]}-{components[1]}'
def greet(name: str, language: dict):
    language = {
        'name': name,
        'en': 'Hello',
        'ru': 'Привет',
        'fr': 'Bonjour'
    }


print(greet('Roman', dict['ru']))
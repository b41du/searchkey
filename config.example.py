# setup database
db_config = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'databasename',
        'user': 'username',
        'password': 'password',
        'prefix': ''
    }
}

# setup file output
path_keyword_url_file = 'data/keyword-url.txt'
keyword_url_separator = '***'

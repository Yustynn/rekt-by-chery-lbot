from sys import argv

if argv[1] == 'clear':
    import logic.db.cleardb
    print('DB Cleared')

elif argv[1] == 'seed':
    import logic.db.seed
    print('DB Seeded')


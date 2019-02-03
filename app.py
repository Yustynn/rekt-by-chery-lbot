import os

from logic.updater import updater

import logic.commands
print('commands registered')

print('clearing db...')
import logic.db.cleardb
print('done')
print('seeding db...')
import logic.db.seed
print('done')

updater.start_polling()

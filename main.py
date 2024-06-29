import asyncio
import logging

from bot import main

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        print(f'Error: {e}')
        print('Shutting down...')
        exit(1)
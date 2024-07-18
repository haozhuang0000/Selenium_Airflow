from logger import Log
from mongodb import MongoDBHandler
from common_methods import get_driver

def get_content():

    driver = get_driver()
    driver.get('https://www.selenium.dev/')
    return driver.page_source

def main():

    logger = Log('Running simple airflow tutorial with selenium').getlog()
    logger.info('Connecting to DB')
    mongodb = MongoDBHandler()
    db = mongodb.get_database()
    col = db['test_airflow']

    logger.info('Getting content from website')
    content = get_content()
    data = {'content': content}

    logger.info('Inserting into your database')
    col.insert_one(data)

if __name__ == '__main__':

    main()
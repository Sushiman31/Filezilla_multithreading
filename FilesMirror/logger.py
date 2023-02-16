import os
import sys
import logging
import logging.config

sys.path.append(os.path.realpath("shared/"))
sys.path.append(os.path.realpath("tests/"))


class Logger(object):

    @staticmethod
    def log_debug(msg):
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.conf')
        logging.config.fileConfig(log_file_path)
        logging.debug(msg)

    @staticmethod
    def log_info(msg):
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.conf')
        logging.config.fileConfig(log_file_path)
        logging.info(msg)

    @staticmethod
    def log_warning(msg):
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.conf')
        logging.config.fileConfig(log_file_path)
        logging.warning(msg)

    @staticmethod
    def log_error(msg):
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.conf')
        logging.config.fileConfig(log_file_path)
        logging.error(msg)

    @staticmethod
    def log_critical(msg):
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.conf')
        logging.config.fileConfig(log_file_path)
        logging.critical(msg)
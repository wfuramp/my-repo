import logging
import sys

def setup_logger(name="pipeline_logger", log_level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # 控制台输出
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger

'restate: Logging se 3 messages (info, warning, error) print karo timestamps ke saath.'

# example:info=Program exicute successfully..!, warning=Program showing error..., error=Something wrong...!

# pseudocode:
            # 1.import logging
            # 2.logging.basicConfig(level=logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")
            # 3.logging.info("Program exicute successfully..!")
            # 4.logging.warning("Program showing error...")
            # 5.logging.error("Something wrong...!")

import logging

logging.basicConfig(level=logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")
logging.info("Program exicute successfully..!")
logging.warning("Program showing error...")
logging.error("Something wrong...!")

# dry run:
# 2026-08-26 18:39:32,835 - INFO - Program exicute successfully..!
# 2026-08-26 18:39:32,836 - WARNING - Program showing error...
# 2026-08-26 18:39:32,836 - ERROR - Something wrong...!  
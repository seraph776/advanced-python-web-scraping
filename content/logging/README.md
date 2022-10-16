<div id="top"  align="center">

# Logging

</div>



## Logging Levels

```python

import logging

logging.debug('message)
logging.info('message)
logging.warning('message)
logging.error('message)
logging.critical('message)

```

<div align="right">

[[↑] Back to top](#top)

</div>  

## Basic Logging


 ```python
 
 
 import logging
 
 logging.basicConfig(level=logging.WARNING,
                    filename='connection.log',
                    filemode='a',
                    style='{',
                    format='{asctime}[{levelname}]{message}',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8'
                    )
 
 
 ```
 
 <div align="right">

[[↑] Back to top](#top)

</div>  
 
 ## Using Handlers
 
 ```python  
 import logging
 
 logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
 
 ```
 
 <div align="right">

[[↑] Back to top](#top)

</div>  
 
 
 ## Advanced Logging
 
 ```python
 import logging
import sys

# Create Logger
logger = logging.getLogger(__name__)

# Set level
logger.setLevel(logging.WARNING)

# Create File Handler
file_handler = logging.FileHandler('debug.log')

# Create Stream Handler:
stream_handler = logging.StreamHandler(sys.stdout)

# Create Formatting:
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s', '%Y-%m-%d %H:%M:%S')

# Set Formatting:
file_handler.setFormatter(formatter)

# ADD HANDLERS
logger.addHandler(file_handler)
logger.addHandler(stream_handler) 
 ```
 
 <div align="right">

[[↑] Back to top](#top)

</div>  
 
 ## Logging Config FIle
 
 
 ```python
 # logging.conf
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s  
 ```
 
 ```python
 # Then use the config file in the code
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message') 
 ```
 
 <div align="right">

[[↑] Back to top](#top)

</div>  
 
 

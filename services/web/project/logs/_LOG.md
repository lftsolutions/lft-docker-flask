 # Logging Breakdown
- By Default, logging is configured as WARNING
- For every logging level you set, it will include not only that log level, but also every log level above it
   - Default Logging Configuration
      - Log Level: WARNING
      - Log Level Numeric Value: 30
      - Any logging setup with Log Level Numeric Value of 30 or above will be included in the logs
      - Further, anything with Log Level Numeric Value below 30 will not be included
- ### Levels
   - 50  - CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
   - 40 - ERROR: Due to a more serious problem, the software has not been able to perform some function.
   - 30 - WARNING (Default): An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
   - 20 - INFO: Confirmation that things are working as expected.
   - 10 - DEBUG: Detailed information, typically of interest only when diagnosing problems.
***

## Example Setup
```python
   # The log level numeric value (20)
   log_level = logging.DEBUG 

   # Logging Based on Environment (Optional)
   log_level = logging.DEBUG if DEBUG else logging.INFO

   # The  log level name (DEBUG)
   log_level_name = logging.getLevelName(log_level) 

   # Instantiation of a new logger
   logger = logging.getLogger(__name__) 

   # Configuring the logger to use Log Level DEBUG (20), which includes all log level numberic values above 20
   logger.setLevel(log_level) 
```
 
***
## Reference
- https://docs.python.org/3/howto/logging.html
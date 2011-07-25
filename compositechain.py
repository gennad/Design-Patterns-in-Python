>>> class DevelopmentPerformanceMonitor():
...   def getPerformanceMonitorHandlers():
...     return []
...
>>> class ProductionPerformanceMonitor():
...   def getPerformanceMonitorHandlers():
...     return [check_cpu_under_load, check_available_hd]
...
>>> class DevelopmentExceptionMonitor():
...   def getExceptionHandlers():
...     return [email_local_root, log_exception]
...
>>> class ProductionExceptionMonitor():
...   def getExceptionHandlers():
...     return [emails_system_admin, log_exception, create_ticket]
...
>>> class SomeSystem:
...    pm = None # Performance Monitor
...    em = None # Exception Monitor
...    def __init__(self, performance_monitor, exception_monitor):
...      pm = performance_monitor
...      em = exception_monitor
...    def on_exception(e):
...      for handler in em.getExceptionHandlers():
...        handler(e)
...    def perform_performance_monitoring(s):
...      for handler in pm.getPerformanceMonitorHandlers():
...        handler(s)

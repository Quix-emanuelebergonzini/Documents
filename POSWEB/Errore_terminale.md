FGNEG-0100013-1:posweb posweb$ ./bin/manager.sh        
/rnd/pos
Traceback (most recent call last):
  File "/rnd/pos/mmfg/posweb/daemons/process_monitor.py", line 438, in <module>
    main()
  File "/rnd/pos/mmfg/posweb/daemons/process_monitor.py", line 435, in main
    PosMonitor().main()
  File "/rnd/pos/mmfg/posweb/daemons/process_monitor.py", line 73, in main
    self.stdscr.keypad(0)
AttributeError: 'NoneType' object has no attribute 'keypad'


se succede questo mando ci si collega al manager vuol dire che è tutto ok è un problema del terminal

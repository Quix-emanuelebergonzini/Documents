i configmaps prima del cloud erano un dizionario con tutte le chiave e pwd in chiaro

ora con i bms in cloud praticamente i veri configmaps di testing e production sono sul kube
quindi bisogna andare nel progetto kube riferito allambiente e inserire dentro configmaps.yml la chiave wsclient e commitarli
 --> i segrets bisogna chiedere a Victoria solo lei può farli e commitarli <--

 i configmaps presenti nel progetto bms sono per lambiente di dev quindi i configmaps presi dal kube sono usati ad esempio quando si fa LANDSCAPE=TESTING
 e posweb dal mio pc in locale comunica con la sede di TEST quindi il bms online userà i configmaps del kube

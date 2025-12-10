come usare il grep dentro un log (es di posweb)

cat var/log/web/main.log* | grep "^2020-02-08 17"

cat var/log/cash_register/main.log* | grep "^2020-02-08 16"

oppure
cd var/log/web --|> e ci sono solo gz e un .log vacca boia
zgrep "^2021-06-22" *.gz

oppure
find . -name main.log.\*.gz -print0 | xargs -0 zgrep "^2021-10-10"


per sapere il nome del file meglio grep in questa forma

grep "^2022-04-02 12" var/log/web/main.lo*

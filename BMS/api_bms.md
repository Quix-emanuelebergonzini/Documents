su linmara vengono richiamate queste api di OT
https://bms-uat.linmara.com/api/bms/v1/sale?filter[date_from]=2024-06-01T21:45:00Z&filter[date_to]=2024-12-31T21:45:00Z&filter[size]=25&filter[page]=0
https://bms-uat.linmara.com/api/bms/v1/salestotal?filter[date_from]=2024-06-01T21:45:00Z&filter[date_to]=2024-12-31T21:45:00Z&filter[size]=25&filter[page]=0
https://bms-uat.linmara.com/api/bms/v1/consumer?filter[date_from]=2024-06-01T21:45:00Z&filter[date_to]=2024-12-31T21:45:00Z&filter[size]=25&filter[page]=0

Autenticazione gbmax / Au8sZ4CNpZ0nGBW1

i logs sono su BMS
SELECT * FROM `request_log_202503` where module like '%/api/bms/v1/consumer%' order by 1 desc;
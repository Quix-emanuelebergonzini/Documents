RICORDARSI CHE:
sugli ambienti cloud è ora utc+0 (esempio, london)

in cloud basta aggiungere il crontab nella relativa cartella prod o test

# B2E
allinea-filtri-catalogo-b2e:
  run:
    - /source/guest/posws/script/upload_b2e_data.py
    - "--command"
    - "filters"
    - "--lingua"
    - "EN"
  schedule: "0 0 * * 1"
  resources_limit_memory: 1000Mi
allinea-new-arrivals-catalogo-b2e:
  run:
    - /source/guest/posws/script/upload_b2e_data.py
    - "--command"
    - "new_arrivals"
    - "--lingua"
    - "EN"
  schedule: "0 1 * * 1"
  resources_limit_memory: 1000Mi
allinea-images-catalogo-b2e:
  run:
    - /source/guest/posws/script/upload_b2e_data.py
    - "--command"
    - "images"
    - "--lingua"
    - "EN"
  schedule: "0 2 * * 1"
  resources_limit_memory: 1000Mi

  poi rebuil dell'ultimo tag di prod o test
  e redeploy in prod o test


from poswsbe.upload_b2e_data.locator import locator
service = locator.get_service("NewFiltersUploadService")
options = {'dummy': True, 'lingua': 'IT', 'brand': ['MR'], '4annistagione': False, 'anno': ['2019'], 'stagione': ['1']}
service.upload_new_filters(options)

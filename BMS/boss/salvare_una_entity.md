esempio:
row = self.new(
    "PosRegistroPresenze",
    id=None,
    codice_negozio=codice_negozio,
    codice_cassiera=codice_cassiera,
    codice_barcode=barcode_presenza,
    dataora_inserimento_client=ora_client_date
)
self.set(row)

dove in entity.py

class PosRegistroPresenze(Entity):
	_key = ("id",)
	id = int
	codice_negozio = str
	codice_cassiera = str
	codice_barcode = int
	dataora_inserimento = datetime
	dataora_inserimento_client = datetime

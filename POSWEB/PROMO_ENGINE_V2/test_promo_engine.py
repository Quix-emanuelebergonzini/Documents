# da eseguire localmente con i demoni accessi.
# il cod_negozio lo impostiamo nella variabile.
# promo_engine_get_campaigns sfrutta la connection_parameters quindi per ws_promo_engine_v2 e ws_promo_engine_v2_admin
# quindi inserire nella tabella, per il cod_negozio per cui si prova la chiamata di promo engine, i relativi records prendendo
# quelli esistenti per il negozio locale.

import sys

for lib_dir in [
	"/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/site/bin",
	"/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/daemons",
	"/Users/emanuele.bergonzini/repos/posweb/mmfg/posweb/site/bin/lib",
]:
	if lib_dir not in sys.path:
		sys.path.insert(0, lib_dir)

from movim_db_access import promo_engine_get_campaigns
from common.pos.constants import DISCOUNT_MAP_PROMO_ENGINE_V2
import movim_utils
import common_utils
import config_store

# ho preso quello che mi è stato dato bisogna adattare le variabili input, output, changes, response

input = {"input": {
      "costs": [

      ],
      "consumer": {
        "registration_date": "20241120000000",
        "privacies": [
          {
            "brand": "MC",
            "flag_marketing": 1,
            "flag_privacy": 1
          }
        ],
        "mmsp_coupon": 0,
        "consumer_code": "18414021",
        "email": "ROX.RL@LIBERO.IT",
        "name": "ROSSELLA",
        "surname": "LIBERATORE",
        "birth_year": "1986",
        "birth_month": "08",
        "cel_2": "",
        "residence_state": "IT",
        "no_mmsp_coupon": 0,
        "vip_level": 0,
        "tel_2": "",
        "fidelity": {
          "card_type": "LOYALTY_MC_IT_24",
          "card_code": "2240032634318",
          "card_real_balance": 537,
          "card_level": "PINK",
          "card_state": "ENABLED",
          "expiration_date": "",
          "issue_date": "20241120000000"
        },
        "cel_1": "+393494388639",
        "birth_day": "20",
        "tel_1": ""
      },
      "creation_date": "20241128125609",
      "discount_fidelity": 0,
      "session_code": "28724",
      "items": [
        {
          "style_code": "6526014702",
          "style_code_variant": "6526014702001",
          "year": "2024",
          "size": "6",
          "discount_on_item": 0,
          "id": 2,
          "product_category": "GARMENTS",
          "base_price": 239,
          "style_variant": "001",
          "exit": "",
          "class": "52",
          "brand": "MC",
          "collection": "67",
          "original_final_price": 239,
          "season": "2",
          "final_price": 239,
          "style_name": "UMA",
          "tailor_expenses": 0,
          "pricelist_type": "V",
          "retail_price": 239,
          "seasonality": "SEASONAL",
          "shop_barcode": "65260147020016",
          "discount_fidelity": 0
        },
        {
          "size": "2",
          "year": "2024",
          "collection": "66",
          "discount_fidelity": 0,
          "brand": "MC",
          "original_final_price": 99,
          "final_price": 99,
          "retail_price": 99,
          "exit": "",
          "style_name": "LOU",
          "class": "75",
          "discount_on_item": 0,
          "base_price": 99,
          "pricelist_type": "V",
          "style_code": "6756014602",
          "style_variant": "004",
          "product_category": "GARMENTS",
          "shop_barcode": "67560146020042",
          "style_code_variant": "6756014602004",
          "tailor_expenses": 0,
          "seasonality": "SEASONAL",
          "season": "2",
          "id": 3
        }
      ],
      "status": "OPEN",
      "shipping_method": {
        "shipping_address": {
          "reference_name": "D'AGNANO MARISA",
          "city": "Ostuni",
          "county": "",
          "zipcode": "72017",
          "name": "",
          "province": "BR",
          "contact_number": "0831-342907",
          "state": "",
          "consumer_info": {
            "contact_number": "+393494388639",
            "reference_name": "ROSSELLA LIBERATORE",
            "surname": "LIBERATORE",
            "contact_email": "ROX.RL@LIBERO.IT",
            "name": "ROSSELLA"
          },
          "address": "Viale Pola, 9/11",
          "surname": "",
          "country": "IT"
        },
        "shipping_type": "STORE"
      },
      "request_timestamp": "2024-11-28T12:56:08+0100",
      "code": "28724",
      "payments": [

      ],
      "livello_loyalty": "pink",
      "type_cart": "SALE",
      "shop": {
        "retail_code": "0174013",
        "shop_sign": "MC",
        "shop_country": "IT"
      }
    }}
output = {"output": {
      "consumer": {
        "email": "ROX.RL@LIBERO.IT",
        "fidelity": {
          "card_state": "ENABLED",
          "card_real_balance": 537,
          "card_type": "LOYALTY_MC_IT_24",
          "issue_date": "20241120000000",
          "card_code": "2240032634318",
          "expiration_date": "",
          "card_level": "PINK"
        },
        "residence_state": "IT",
        "surname": "LIBERATORE",
        "consumer_code": "18414021",
        "tel_1": "",
        "cel_1": "+393494388639",
        "birth_day": "20",
        "birth_year": "1986",
        "privacies": [
          {
            "flag_privacy": 1,
            "brand": "MC",
            "flag_marketing": 1
          }
        ],
        "no_mmsp_coupon": 0,
        "registration_date": "20241120000000",
        "mmsp_coupon": 0,
        "birth_month": "08",
        "cel_2": "",
        "vip_level": 0,
        "name": "ROSSELLA",
        "tel_2": ""
      },
      "shipping_method": {
        "shipping_address": {
          "county": "",
          "name": "",
          "consumer_info": {
            "name": "ROSSELLA",
            "contact_email": "ROX.RL@LIBERO.IT",
            "surname": "LIBERATORE",
            "contact_number": "+393494388639",
            "reference_name": "ROSSELLA LIBERATORE"
          },
          "reference_name": "D'AGNANO MARISA",
          "zipcode": "72017",
          "address": "Viale Pola, 9/11",
          "country": "IT",
          "contact_number": "0831-342907",
          "city": "Ostuni",
          "state": "",
          "province": "BR",
          "surname": ""
        },
        "shipping_type": "STORE"
      },
      "type_cart": "SALE",
      "items": [
        {
          "amount_correction_th": -72,
          "pricelist_type": "V",
          "class": "52",
          "original_final_price": 239,
          "exit": "",
          "discount_fidelity": 0,
          "product_category": "GARMENTS",
          "size": "6",
          "final_price": 167,
          "retail_price": 239,
          "collection": "67",
          "style_code": "6526014702",
          "promo_engine": [
            "promo_54"
          ],
          "style_variant": "001",
          "base_price": 239,
          "brand": "MC",
          "discount_percentage": -30,
          "style_name": "UMA",
          "amount_correction": -72,
          "season": "2",
          "tailor_expenses": 0,
          "year": "2024",
          "id": 2,
          "style_code_variant": "6526014702001",
          "discount_on_item": 0,
          "seasonality": "SEASONAL",
          "shop_barcode": "65260147020016",
          "discount_percentage_th": -30
        },
        {
          "class": "75",
          "promo_engine": [
            "promo_54"
          ],
          "discount_fidelity": 0,
          "tailor_expenses": 0,
          "style_name": "LOU",
          "year": "2024",
          "style_variant": "004",
          "style_code_variant": "6756014602004",
          "amount_correction": -30,
          "amount_correction_th": -30,
          "collection": "66",
          "retail_price": 99,
          "discount_percentage": -30,
          "size": "2",
          "discount_on_item": 0,
          "product_category": "GARMENTS",
          "pricelist_type": "V",
          "id": 3,
          "exit": "",
          "base_price": 99,
          "season": "2",
          "original_final_price": 99,
          "style_code": "6756014602",
          "discount_percentage_th": -30,
          "seasonality": "SEASONAL",
          "shop_barcode": "67560146020042",
          "final_price": 69,
          "brand": "MC"
        }
      ],
      "request_timestamp": "2024-11-28T12:56:08+0100",
      "status": "OPEN",
      "creation_date": "20241128125609",
      "key_legal_entity": "Negozi_Italia_MC",
      "session_code": "28724",
      "code": "28724",
      "payments": [

      ],
      "day_of_week": 4,
      "costs": [

      ],
      "shop": {
        "shop_country": "IT",
        "shop_sign": "MC",
        "retail_code": "0174013"
      },
      "discount_fidelity": 0,
      "key_shop_sign": "MC",
      "livello_loyalty": "pink"
    }}
changes = {"changes": [
      {
        "effects": [
          {
            "items": [
              {
                "amount_correction": {
                  "end": -72,
                  "start": None
                },
                "partially_applied": False,
                "discount_percentage_th": {
                  "start": None,
                  "end": -30
                },
                "time": "20241128115609.271048ff",
                "final_price": {
                  "start": 239,
                  "end": 167,
                  "diff": -72
                },
                "id": 2,
                "discount_percentage": {
                  "start": None,
                  "end": -30
                },
                "amount_correction_th": {
                  "start": None,
                  "end": -72
                }
              },
              {
                "time": "20241128115609.271115ff",
                "partially_applied": False,
                "final_price": {
                  "end": 69,
                  "start": 99,
                  "diff": -30
                },
                "discount_percentage": {
                  "end": -30,
                  "start": None
                },
                "amount_correction_th": {
                  "start": None,
                  "end": -30
                },
                "amount_correction": {
                  "end": -30,
                  "start": None
                },
                "id": 3,
                "discount_percentage_th": {
                  "start": None,
                  "end": -30
                }
              }
            ],
            "value_type": "PERCENTAGE",
            "type": "CHANGE"
          }
        ],
        "informations": {
          "description": "Fino al -30% di sconto su una selezione di capi",
          "title": "BLACK FRIDAY",
          "color_code": "#FF40B3",
          "document": "",
          "effect_type": "DISCOUNT"
        },
        "promo": "promo_54"
      }
    ]}
response = {
  "insertId": "67485a590004256755b72d9b",
  "jsonPayload": {
    "creationDate": "20241128125609",
    "output": {
      "consumer": {
        "email": "ROX.RL@LIBERO.IT",
        "fidelity": {
          "card_state": "ENABLED",
          "card_real_balance": 537,
          "card_type": "LOYALTY_MC_IT_24",
          "issue_date": "20241120000000",
          "card_code": "2240032634318",
          "expiration_date": "",
          "card_level": "PINK"
        },
        "residence_state": "IT",
        "surname": "LIBERATORE",
        "consumer_code": "18414021",
        "tel_1": "",
        "cel_1": "+393494388639",
        "birth_day": "20",
        "birth_year": "1986",
        "privacies": [
          {
            "flag_privacy": 1,
            "brand": "MC",
            "flag_marketing": 1
          }
        ],
        "no_mmsp_coupon": 0,
        "registration_date": "20241120000000",
        "mmsp_coupon": 0,
        "birth_month": "08",
        "cel_2": "",
        "vip_level": 0,
        "name": "ROSSELLA",
        "tel_2": ""
      },
      "shipping_method": {
        "shipping_address": {
          "county": "",
          "name": "",
          "consumer_info": {
            "name": "ROSSELLA",
            "contact_email": "ROX.RL@LIBERO.IT",
            "surname": "LIBERATORE",
            "contact_number": "+393494388639",
            "reference_name": "ROSSELLA LIBERATORE"
          },
          "reference_name": "D'AGNANO MARISA",
          "zipcode": "72017",
          "address": "Viale Pola, 9/11",
          "country": "IT",
          "contact_number": "0831-342907",
          "city": "Ostuni",
          "state": "",
          "province": "BR",
          "surname": ""
        },
        "shipping_type": "STORE"
      },
      "type_cart": "SALE",
      "items": [
        {
          "amount_correction_th": -72,
          "pricelist_type": "V",
          "class": "52",
          "original_final_price": 239,
          "exit": "",
          "discount_fidelity": 0,
          "product_category": "GARMENTS",
          "size": "6",
          "final_price": 167,
          "retail_price": 239,
          "collection": "67",
          "style_code": "6526014702",
          "promo_engine": [
            "promo_54"
          ],
          "style_variant": "001",
          "base_price": 239,
          "brand": "MC",
          "discount_percentage": -30,
          "style_name": "UMA",
          "amount_correction": -72,
          "season": "2",
          "tailor_expenses": 0,
          "year": "2024",
          "id": 2,
          "style_code_variant": "6526014702001",
          "discount_on_item": 0,
          "seasonality": "SEASONAL",
          "shop_barcode": "65260147020016",
          "discount_percentage_th": -30
        },
        {
          "class": "75",
          "promo_engine": [
            "promo_54"
          ],
          "discount_fidelity": 0,
          "tailor_expenses": 0,
          "style_name": "LOU",
          "year": "2024",
          "style_variant": "004",
          "style_code_variant": "6756014602004",
          "amount_correction": -30,
          "amount_correction_th": -30,
          "collection": "66",
          "retail_price": 99,
          "discount_percentage": -30,
          "size": "2",
          "discount_on_item": 0,
          "product_category": "GARMENTS",
          "pricelist_type": "V",
          "id": 3,
          "exit": "",
          "base_price": 99,
          "season": "2",
          "original_final_price": 99,
          "style_code": "6756014602",
          "discount_percentage_th": -30,
          "seasonality": "SEASONAL",
          "shop_barcode": "67560146020042",
          "final_price": 69,
          "brand": "MC"
        }
      ],
      "request_timestamp": "2024-11-28T12:56:08+0100",
      "status": "OPEN",
      "creation_date": "20241128125609",
      "key_legal_entity": "Negozi_Italia_MC",
      "session_code": "28724",
      "code": "28724",
      "payments": [
        
      ],
      "day_of_week": 4,
      "costs": [
        
      ],
      "shop": {
        "shop_country": "IT",
        "shop_sign": "MC",
        "retail_code": "0174013"
      },
      "discount_fidelity": 0,
      "key_shop_sign": "MC",
      "livello_loyalty": "pink"
    },
    "changes": [
      {
        "effects": [
          {
            "items": [
              {
                "amount_correction": {
                  "end": -72,
                  "start": None
                },
                "partially_applied": False,
                "discount_percentage_th": {
                  "start": None,
                  "end": -30
                },
                "time": "20241128115609.271048ff",
                "final_price": {
                  "start": 239,
                  "end": 167,
                  "diff": -72
                },
                "id": 2,
                "discount_percentage": {
                  "start": None,
                  "end": -30
                },
                "amount_correction_th": {
                  "start": None,
                  "end": -72
                }
              },
              {
                "time": "20241128115609.271115ff",
                "partially_applied": False,
                "final_price": {
                  "end": 69,
                  "start": 99,
                  "diff": -30
                },
                "discount_percentage": {
                  "end": -30,
                  "start": None
                },
                "amount_correction_th": {
                  "start": None,
                  "end": -30
                },
                "amount_correction": {
                  "end": -30,
                  "start": None
                },
                "id": 3,
                "discount_percentage_th": {
                  "start": None,
                  "end": -30
                }
              }
            ],
            "value_type": "PERCENTAGE",
            "type": "CHANGE"
          }
        ],
        "informations": {
          "description": "Fino al -30% di sconto su una selezione di capi",
          "title": "BLACK FRIDAY",
          "color_code": "#FF40B3",
          "document": "",
          "effect_type": "DISCOUNT"
        },
        "promo": "promo_54"
      }
    ],
    "shopCode": "0174013",
    "asctime": "2024-11-28 11:56:09,271",
    "sinkType": "ResponseLogForPromoBuilder",
    "input": {
      "costs": [
        
      ],
      "consumer": {
        "registration_date": "20241120000000",
        "privacies": [
          {
            "brand": "MC",
            "flag_marketing": 1,
            "flag_privacy": 1
          }
        ],
        "mmsp_coupon": 0,
        "consumer_code": "18414021",
        "email": "ROX.RL@LIBERO.IT",
        "name": "ROSSELLA",
        "surname": "LIBERATORE",
        "birth_year": "1986",
        "birth_month": "08",
        "cel_2": "",
        "residence_state": "IT",
        "no_mmsp_coupon": 0,
        "vip_level": 0,
        "tel_2": "",
        "fidelity": {
          "card_type": "LOYALTY_MC_IT_24",
          "card_code": "2240032634318",
          "card_real_balance": 537,
          "card_level": "PINK",
          "card_state": "ENABLED",
          "expiration_date": "",
          "issue_date": "20241120000000"
        },
        "cel_1": "+393494388639",
        "birth_day": "20",
        "tel_1": ""
      },
      "creation_date": "20241128125609",
      "discount_fidelity": 0,
      "session_code": "28724",
      "items": [
        {
          "style_code": "6526014702",
          "style_code_variant": "6526014702001",
          "year": "2024",
          "size": "6",
          "discount_on_item": 0,
          "id": 2,
          "product_category": "GARMENTS",
          "base_price": 239,
          "style_variant": "001",
          "exit": "",
          "class": "52",
          "brand": "MC",
          "collection": "67",
          "original_final_price": 239,
          "season": "2",
          "final_price": 239,
          "style_name": "UMA",
          "tailor_expenses": 0,
          "pricelist_type": "V",
          "retail_price": 239,
          "seasonality": "SEASONAL",
          "shop_barcode": "65260147020016",
          "discount_fidelity": 0
        },
        {
          "size": "2",
          "year": "2024",
          "collection": "66",
          "discount_fidelity": 0,
          "brand": "MC",
          "original_final_price": 99,
          "final_price": 99,
          "retail_price": 99,
          "exit": "",
          "style_name": "LOU",
          "class": "75",
          "discount_on_item": 0,
          "base_price": 99,
          "pricelist_type": "V",
          "style_code": "6756014602",
          "style_variant": "004",
          "product_category": "GARMENTS",
          "shop_barcode": "67560146020042",
          "style_code_variant": "6756014602004",
          "tailor_expenses": 0,
          "seasonality": "SEASONAL",
          "season": "2",
          "id": 3
        }
      ],
      "status": "OPEN",
      "shipping_method": {
        "shipping_address": {
          "reference_name": "D'AGNANO MARISA",
          "city": "Ostuni",
          "county": "",
          "zipcode": "72017",
          "name": "",
          "province": "BR",
          "contact_number": "0831-342907",
          "state": "",
          "consumer_info": {
            "contact_number": "+393494388639",
            "reference_name": "ROSSELLA LIBERATORE",
            "surname": "LIBERATORE",
            "contact_email": "ROX.RL@LIBERO.IT",
            "name": "ROSSELLA"
          },
          "address": "Viale Pola, 9/11",
          "surname": "",
          "country": "IT"
        },
        "shipping_type": "STORE"
      },
      "request_timestamp": "2024-11-28T12:56:08+0100",
      "code": "28724",
      "payments": [
        
      ],
      "livello_loyalty": "pink",
      "type_cart": "SALE",
      "shop": {
        "retail_code": "0174013",
        "shop_sign": "MC",
        "shop_country": "IT"
      }
    },
    "key_legal_entity": "Negozi_Italia_MC",
    "key_shop_sign": "MC",
    "sessionCode": "28724",
    "api": "evaluate_data",
    "message": "Log Sink For Session Code: 28724 and API: evaluate",
    "compileVersion": "20241127230103547931",
    "dd.span_id": "11874298247002200147",
    "name": "mmfg.rule_engine",
    "executionTime": 0.006192207336425781,
    "dd.trace_id": "209440376475254345244654554613366952705"
  },
  "resource": {
    "type": "cloud_run_revision",
    "labels": {
      "revision_name": "promoengine-00561-frr",
      "configuration_name": "promoengine",
      "location": "europe-west1",
      "service_name": "promoengine",
      "project_id": "mmfg-promoengine-gruppo-prod"
    }
  },
  "timestamp": "2024-11-28T11:56:09.271719Z",
  "severity": "INFO",
  "labels": {
    "instanceId": "004940b3b889b47bff22126f38eedfdd5e0245d132332b50c1e677e63ac45e3469212554f47fe3a27d98929462b4f17aab4c60865a97ceadc14aea061f877ac0e5258be3ab2e"
  },
  "logName": "projects/mmfg-promoengine-gruppo-prod/logs/run.googleapis.com%2Fstdout",
  "receiveTimestamp": "2024-11-28T11:56:09.299828344Z"
}

action = ""

cod_negozio = "0174013"

def test_promo_engine_v2(action, input, output, cod_negozio):

	pard = config_store.application_parameters(use_ws=True)

	prev_prices = {
		"items": {i["id"]: i["base_price"] for i in input["items"]},
		"costs": {c["id"]: c["cost_amount"] for c in input["costs"]},
	}

	final_prices = {
		"items": {i["id"]: i["final_price"] for i in input["items"]},
	}

	items = []
	costs = []
	vouchers = []
	payments = []
	promo = {}

	res = {
		"items": items,
		"costs": costs,
		"vouchers": vouchers,
		"payments": payments,
		"promo": promo,
	}

	#extra = [{v : c['importo_finale'] for v in DISCOUNT_MAP_PROMO_ENGINE_V2.values() for c in mov_contabilita if c["codice_movimento"] == v}]

	# if extra:
		# res['extra'] = extra

	if action == "apply_selection":
		input = {
			"input": input,
			"promotions": input.pop("promotions")
		}

	if not response:
		if action == "list":
			return {}
		return res

	if action in ("apply_selection", "list") and response.get("errors"):
		descriptions_list = ', '.join(res['description'] for res in response['errors'])
		return {'exception': descriptions_list}

	if action == "list":
		return response['output']

	print("Promo Engine V2 Campaigns:")
	campaigns = promo_engine_get_campaigns(pard, cod_negozio)

	# lavoro i dati del servizio per ridare al client tutte le informazioni necessarie
	output_items = output.get("items", [])
	last_progressivo = 0
	if output_items:
		last_progressivo = max([int(item["id"]) for item in output_items if item["id"] is not None])

	output_costs = output.get("costs", [])
	output_changes = changes["changes"]

	pard["POS_CONFIG"]["COUNTRY_CODE"] = "IT"
	payments_trads = movim_utils.get_tipi_pagamento(pard)

	tipi_movimento_d = {
		r['codice_movimento']: r['descrizione']
		for r in common_utils.translate_list_of_dicts(
			pard, movim_utils.get_tipi_movimento_all(pard),
			"pos_movement_type", "descrizione", "codice_movimento"
		)
	}

	# gestione della risposta sui capi
	for capo in output_items:
		id = capo["id"]
		if not id:
			last_progressivo = int(last_progressivo) + 1
			id = last_progressivo

		all_discounts = sum(capo.get(k, 0) for k in DISCOUNT_MAP_PROMO_ENGINE_V2.keys())
		new_items = {
			"id": id,
			"sku": capo.get("shop_barcode", ""),
			"name": capo.get("style_name", ""),
			"discount_on_item": capo.get("discount_on_item", 0),
			"prev_price": prev_prices["items"].get(capo["id"], capo.get("final_price", 0)),
			"final_price": capo.get("final_price", 0),
			"modified": True if capo.get("promo_engine") else False,
			"added": True if capo["id"] is None else False,
			"promo_engine": capo.get("promo_engine", []),  # promo utilizzate dal capo
			"net_final_price": common_utils.fix_number(capo.get("final_price", 0) - all_discounts),
			# importo prezzo_finale al netto del promo_engine
			"discount_final_price": common_utils.fix_number(capo.get("original_final_price", 0))
			# importo netto tutti gli sconti (es, fidelitY
		}

		if new_items["added"]:
			dati_capo = common_db_access.get_all_dati_capi(pard, [new_items["sku"]])
			if not dati_capo:
				return {'exception':
							common_utils.translate_elements(pard['USER'], pard['POS_CONFIG']['GUI_LANGUAGE_LOCALE'],
															'pos_sale')['group_sku_catalog']}
			new_items["name"] = dati_capo[new_items["sku"]]["nome"]
			for id_promo in capo["promo_engine"]:
				change = list(filter(lambda o: o["promo"] == id_promo, output_changes))
				if change:
					change = change[0]
				promo.setdefault(id_promo, {
					"items": [],
					"costs": [],
					"title": change["informations"].get('title', change["informations"].get('text', '')) if change else '',
					"description": change["informations"].get('description', '') if change else '',
					"id_promo": id_promo
				})["items"].append({
					"id": new_items["id"],
					"amount": capo.get("final_price", 0),
					"value_type": "",
					"value": 0,
				})

		if new_items["modified"] and not new_items["added"]:
			found_related_promo = False
			for id_promo in capo["promo_engine"]:
				change_list = list(filter(lambda o: o["promo"] == id_promo, output_changes))
				if change_list:
					for change in change_list:
						for effect in change["effects"]:
							for obj in effect.get("items", []):
								if obj["id"] == capo["id"]:
									promotion = {}
									value_type = ''
									value = 0
									for campaign in campaigns['data']['results']:
										tmp_list_promo = list(filter(lambda p: p['id'] == int(id_promo.split('_')[-1]),
																	 campaign['promotions']))
										if tmp_list_promo:
											promotion = tmp_list_promo[0]
											break;
									if promotion.get('effects'):
										value_type = promotion['effects'][0]['value_type']
										effect_value_type = promotion['effects'][0]['effect_value']['type']
										value = json.loads(promotion['effects'][0]['effect_value']['value'])
										if value_type == 'PERCENTAGE' and effect_value_type == 'single':
											value = float(value)
										else:
											value = ""
									promo.setdefault(id_promo, {
										"items": [],
										"costs": [],
										"title": change["informations"].get('title',
																			change["informations"].get('text', '')),
										"description": change["informations"].get('description', ''),
										"id_promo": id_promo,
									})["items"].append({
										"id": obj["id"],
										"amount": obj.get("final_price", {}).get("diff", 0),
										"value_type": value_type,
										"value": value,
									})
									found_related_promo = True
			if not found_related_promo:
				new_items["modified"] = False

		if new_items["modified"] and not new_items["added"] and new_items['final_price']:
			new_items["final_price"] = common_utils.arrotonda_importo(pard, common_utils.fix_number(
				new_items["prev_price"] -
				(common_utils.fix_number(final_prices["items"][capo["id"]] - new_items["final_price"])) + new_items[
					"discount_on_item"]
			), round_decimals=pard['POS_CONFIG']['DECIMAL_PLACES_ROUNDING'])
			new_items["discount_on_item"] = common_utils.fix_number(new_items["prev_price"] - new_items["final_price"])

		items.append(new_items)

	# gestione della risposta sulle contabilità
	for contabilita in output_costs:
		all_discounts = sum(contabilita.get(k, 0) for k in DISCOUNT_MAP_PROMO_ENGINE_V2.keys())
		new_costs = {
			"id": contabilita["id"],
			"cost_type": MAPPING_TOKEN_PROMO_ENGINE_V2_CODMOV.get(contabilita["cost_type"], contabilita["cost_type"]),
			"cost_type_trad": tipi_movimento_d.get(
				MAPPING_TOKEN_PROMO_ENGINE_V2_CODMOV.get(contabilita["cost_type"], contabilita["cost_type"]),
				contabilita["cost_type"]
			),
			"prev_price": prev_prices["costs"].get(contabilita["id"], contabilita.get("cost_amount", 0)),
			"final_price": contabilita.get("cost_amount", 0),
			"modified": True if contabilita.get("promo_engine") else False,
			"promo_engine": contabilita.get("promo_engine", []),
			"net_final_price": common_utils.fix_number(contabilita.get("cost_amount", 0) - all_discounts),
			"discount_final_price": common_utils.fix_number(contabilita.get("original_final_price", 0))
		}

		if new_costs["modified"]:
			found_related_promo = False
			for id_promo in contabilita["promo_engine"]:
				change_list = list(filter(lambda o: o["promo"] == id_promo, output_changes))
				if change_list:
					for change in change_list:
						for effect in change["effects"]:
							for obj in effect["costs"]:
								if obj["id"] == contabilita["id"]:
									promo.setdefault(id_promo, {
										"items": [],
										"costs": [],
										"title": change["informations"].get('title',
																			change["informations"].get('text', '')),
										"description": change["informations"].get('description', ''),
										"id_promo": id_promo,
									})["costs"].append({
										"id": obj["id"],
										"amount": obj.get("cost_amount", {}).get("diff", 0),
									})
									found_related_promo = True
			if not found_related_promo:
				new_costs["modified"] = False

		costs.append(new_costs)

	# gestione della risposta sui pagamenti e vouchers
	id_burned_coupon = None
	for change in output_changes:
		promo_name = change["informations"].get("title", change["informations"].get("text", ''))
		description = change["informations"].get("description", '')
		if change["informations"].get("effect_type") in ("PAYMENT_TENDER",):
			for effect in change["effects"]:
				for pay in effect["payments"]:
					payments.append({
						"payment_code": pay["payment_type"],
						"payment_code_trad": payments_trads[pay["payment_type"]]["descrizione"] if payments_trads.get(
							pay["payment_type"]) else pay["payment_type"],
						"amount": pay["payment_amount"],
					})
		if change["informations"].get("effect_type") in ("VOUCHER",):
			for effect in change["effects"]:
				if effect.get("messages"):
					try:
						converted = base64.b64encode(effect["messages"][0])
					except:
						converted = base64.b64encode(effect["messages"][0].encode("utf-8"))
					vouchers.append(converted)
		if change["informations"].get("effect_type") in ("COUPON_DISCOUNT",):
			effects_coupon = [k for ch_effects in change.get("effects", []) for k in ch_effects.get("consumer", {}).keys()
							  if k.endswith("_coupon")]
			id_burned_coupon = (
				change['promo'],
				effects_coupon[0] if effects_coupon else []
			)
		promo.setdefault(change["promo"], {"items": [], "costs": [], "id_promo": change["promo"], "title": promo_name,
										   "description": description})

	if id_burned_coupon:
		promo[id_burned_coupon[0]]['vip_tiers_coupon_used'] = id_burned_coupon[1]

	if action == "apply_selection":
		tmp_promo = {}
		[tmp_promo.update({x['promo']: promo[x['promo']]}) for x in selected_promo if promo.get(x['promo'])]
		promo = tmp_promo

	res.update({
		"items": items,
		"costs": costs,
		"vouchers": vouchers,
		"payments": payments,
		"promo": promo,
	})

	print("Promo Engine V2 Res: {}".format(res))
	return res


test_promo_engine_v2(action, input["input"], output["output"], cod_negozio)
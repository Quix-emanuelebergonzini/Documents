# from __future__ import print_function
# from __future__ import division
# from __future__ import absolute_import
# from future import standard_library
# standard_library.install_aliases()
from common import ws_json
import config_store
pard = config_store.application_parameters(use_ws=True)
input = {u'shop': {u'state_shop': 'HK', u'shop_country': 'HK', u'retail_code': '1101013', u'shop_sign': u'MR'}, u'status': u'OPEN', u'code': '328405', u'shipping_method': {}, u'sale_channel': u'Retail', u'creation_date': '20210923102411', u'document_type': u'documentType', u'shop_sign': u'MM', u'consumer': {u'surname': u'', u'smart2': u'', u'smart1': u'', u'registration_date': u'20191030000000', u'birth_day': u'00', u'fidelity': {}, u'residence_state': u'CN', u'tel1': u'', u'tel2': u'', u'name': u'', u'privacy': [{u'flag_marketing': 0, u'brand': u'MR', u'flag_privacy': 1}], u'consumer_code': u'HK_127743', u'birth_month': u'00', u'email': u'', u'birth_year': u'0'}, u'legal_entity': u'M005', u'costs': [], u'payments': [], u'items': [{u'product_category': u'X', u'style_code': u'092213445', u'year': u'2019', u'id': 1, u'categoria_merciologica': u'GARMENTS', u'model_code': u'1021169004', u'shop_barcode': u'10211690040581', u'tipologia_listino': u'S', u'exit': u'', u'style_name': u'PROTOTYPE', u'pricelist_type': u'S', u'tg': u'1', u'final_price': 1736, u'spese_sartoria': 0, u'style_variant': u'', u'season': u'1', u'brand': u'PE', u'variante': u'058', u'collection': u'11', u'retail_price': 2480, u'class': u'02', u'tailor_expenses': 0, u'model_name': u'TALIA', u'base_price': 1736}], u'type_cart': u'SALE'}
cod_negozio = '1101013'
response = ws_json.json_request(
    pard['POS_CONFIG']['WS_PROMO_ENGINE_V2'],
    cod_negozio,
    input,
    "",
    request_method="POST"
)

== poslite sg ==
from common import ws_json
import config_store
pard = config_store.application_parameters(use_ws=True)
input = {"shop": {"retail_code": "1901012", "shop_country": "SG", "shop_sign": "MC"}, "status": "OPEN", "code": "6115", "session_code": "6115", "creation_date": "20250320092112", "request_timestamp": "2025-03-20T10:20:12+0100", "consumer": {"consumer_code": "HK_127962", "name": "STELLA", "surname": "FUNG", "birth_day": "01", "birth_month": "01", "birth_year": "2000", "email": "stellaskfung@mmhk.hk", "tel_1": "", "tel_2": "", "cel_1": "+8529255258401", "cel_2": "", "residence_state": "TW", "fidelity": {"card_type": "", "card_code": "", "card_level": "", "card_real_balance": "", "card_state": "", "issue_date": "", "expiration_date": ""}, "privacies": [{"brand": "MC", "flag_privacy": 1, "flag_marketing": 1}], "registration_date": "20230210000000", "mmsp_coupon": 0, "no_mmsp_coupon": 0, "vip_level": 0}, "payments": [], "type_cart": "SALE", "shipping_method": {}, "items": [{"shop_barcode": "10110121060201", "id": 1, "style_code": "1011012106", "style_code_variant": "1011012106020", "style_name": "LABBRO", "style_variant": "020", "size": "1", "year": "2022", "season": "1", "class": "01", "exit": "", "discount_on_item": 0.0, "collection": "11", "brand": "MM", "seasonality": "SEASONAL", "product_category": "GARMENTS", "retail_price": 8109.0, "base_price": 8109.0, "pricelist_type": "V", "final_price": 8109.0, "original_final_price": 8109.0, "tailor_expenses": 0, "discount_fidelity": 0.0}, {"shop_barcode": "61010152020024", "id": 2, "style_code": "6101015202", "style_code_variant": "6101015202002", "style_name": "OCA", "style_variant": "002", "size": "4", "year": "2025", "season": "1", "class": "10", "exit": "", "discount_on_item": 0.0, "collection": "62", "brand": "MC", "seasonality": "SEASONAL", "product_category": "GARMENTS", "retail_price": 379.0, "base_price": 379.0, "pricelist_type": "V", "final_price": 379.0, "original_final_price": 379.0, "tailor_expenses": 0, "discount_fidelity": 0.0}], "livello_loyalty": "", "costs": [], "discount_fidelity": 0}
cod_negozio = '1901012'
json_params = { 'name': pard['POS_CONFIG']['WS_PROMO_ENGINE_V2'], 'cod_negozio': cod_negozio, 'data': input, 'json_api': False }
def url_pe_list_selection(old_value):
    if "evaluate" in old_value:
        return old_value.replace("evaluate", "estimate")
    else:
        return "{}/engine/estimate".format(old_value)

fz_override = {'url': url_pe_list_selection}
json_params.update({'override': fz_override})
response = ws_json.json_request( **json_params )
result = response.get_data()

-- problemi di proxy -- provare http_proxy='' curl -vvv {url}
-- problemi di request_method
-- problemi di certificati
-- problemi di composione url

-- problemi di chiavi del dizionario nei dati
-- o passaggio del content (tipo manca la chiave "data": {...})

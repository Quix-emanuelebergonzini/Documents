import os
from pprint import pprint
from unicodedata import normalize
import csv
import traceback
from copy import copy

from mmj_transcodifiche import trans


def manage_alpha_addr(r):
	ret = copy(r)
	addr_needed = ("address", "zipcode", "city", "province", "state", "street_number", "building", "subbuilding")
	alpha = "LATIN"
	we_have_one = any(
		r.get(k, '').replace(".", "")
		for k in r
		if any(k in k_addr_n for k_addr_n in addr_needed)
	)
	keys = list(r.keys())
	for k in keys:
		if k.startswith("alphabet_address_"):
			alpha = k.split("_")[2]
			ret.pop(k)
	for k, v in r.items():
		if k in addr_needed:
			new_k = "alphabet_address_%s" % k
			v = ret[k]
			if v:
				ret[new_k] = v
			elif we_have_one:
				ret[new_k] = "."
			if k != "state":
				ret[k] = ''
		ret["alphabet_address_alphabet"] = alpha
	return ret


def qualify_data(r):
	print(r)
	for k, v in r.items():
		r[k] = normalize("NFKC", v.encode("utf-8").decode("utf-8")).strip()
		if r[k] == '.':
			r[k] = ''

	store, brand = trans.get(r["store"], ('0801994', 'MM'))
	r["original_store"], r["store"] = r["store"], store
	r["privacy_brand"] = brand

	id_mmfg = r.pop("id consumer MMFG", None)
	r["consumer_code"] = r.get("consumer_code") or id_mmfg
	r["nazionalita"] = r.pop("nationality", None)
	r["mobile"] = r.pop("mobile_primary", None)

	r.pop("rank", None)
	r.pop("point", None)

	if r["alphabet_name_KANJI_surname"] and not r["alphabet_name_KANJI_name"]:
		splitted = r["alphabet_name_KANJI_surname"].split()
		r["alphabet_name_KANJI_surname"] = splitted[0]
		r["alphabet_name_KANJI_name"] = " ".join(splitted[1:])
	if r["alphabet_name_KANA_surname"] and not r["alphabet_name_KANA_name"]:
		r["alphabet_name_KANA_name"] = '.'

	if not any(r[k] for k in (
			"alphabet_name_KANJI_surname", "alphabet_name_KANJI_name",
			"alphabet_name_KANA_surname", "alphabet_name_KANA_name",
			"name", "surname"
	)):
		r["name"] = ""
		r["surname"] = ""

	r["state"] = r.get("state", "JP") or "JP"

	if len(r["notes"]) > 255:
		r["store_notes"] += "\n" + r["notes"]
		r["notes"] = ""
	for k in ("wechat", "email", "notes", "store_notes", "mobile", "phone", "phone_alt", "mobile_alt"):
		if r[k].strip() in ("0", '.'):
			r[k] = ''
		if k in ("mobile", "phone", "phone_alt", "mobile_alt") and r[k] and not r[k].startswith("+"):
			r[k] = "+81" + r[k]

	try:
		year = int(r["birthdate_year"])
		if year < 1900:
			r["birthdate_year"] = ''
	except:
		r["birthdate_year"] = ''

	for k in ("privacy_marketing_value", "privacy_profiling_value"):
		if r[k].strip() in ('', '.'):
			r[k] = '0'
	return r


if __name__ == '__main__':
	for p in os.listdir("."):
		if os.path.isfile(os.path.abspath(p)) and p.endswith('.csv') and "qualified_" not in p:
			print("processing %s" % p)
			with open(p) as csv_f:
				reader = csv.DictReader(csv_f)
				out_name = "qualified_%s.csv" % str(p).split('-')[0].strip()
				with open(out_name, "w") as fout:
					for i, row in enumerate(reader):
						row = qualify_data(row)
						row = manage_alpha_addr(row)
						if i == 0:
							writer = csv.DictWriter(
								fout,
								fieldnames=row.keys(),
								quoting=csv.QUOTE_ALL,
								quotechar='"'
							)
							writer.writeheader()
						writer.writerow(row)
				print("saved in %s" % out_name)

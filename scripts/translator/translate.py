import argparse

def main(issue=None, replace=False):
	languages = ["it", "en", "de", "hu", "es", "pt", "fr", "nl", "dk", "ja", "zh", "sv", "es_ca", "tw"]
	translate = {}

	cluster = input("cluster: ")
	id = input("id: ")
	label_it = input("label italiana: ")
	translate.update({'it': label_it})
	label_en = input("label inglese: ")
	translate.update({'en': label_en})

	add_languages = input("altre lingue? ")
	if add_languages != "" and add_languages in ("yes", "y", "s"):
		label_de = input("label tedesca: ")
		translate.update({'de': label_de if label_de else label_en})
		label_hu = input("label ungherese: ")
		translate.update({'hu': label_hu if label_hu else label_en})
		label_fr = input("label francese: ")
		translate.update({'fr': label_fr if label_fr else label_en})
		label_es = input("label spagnola: ")
		translate.update({'es': label_es if label_es else label_en})
		label_pt = input("label portoghese: ")
		translate.update({'pt': label_pt if label_pt else label_en})
		label_nl = input("label olandese: ")
		translate.update({'nl': label_nl if label_nl else label_en})
		label_dk = input("label danese: ")
		translate.update({'dk': label_dk if label_dk else label_en})
		label_ja = input("label giapponese: ")
		translate.update({'ja': label_ja if label_ja else label_en})
		label_zh = input("label cinese: ")
		translate.update({'zh': label_zh if label_zh else label_en})
		label_sv = input("label svedese: ")
		translate.update({'sv': label_sv if label_sv else label_en})

	print("")
	for lang in languages:
		insert_or_replace = """{insert} INTO pos_translations VALUES('POS','{cluster}','{id}','{language}','{label_it}','{label_tradotta}','{user}',CURRENT_TIMESTAMP, '');""".format(
			insert="INSERT" if not replace else "REPLACE",
			cluster=cluster,
			id=id,
			language=lang,
			label_it=label_it,
			label_tradotta=translate.get(lang, label_en),
			user=f"bergonzinie::{issue}" if issue else "bergonzinie"
		)
		print(insert_or_replace)
	print("")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--issue', type=str, help='issue da aggiungere come user')
	parser.add_argument('-r', '--force_replace', action="store_true", help='impone replace invece di insert')
	args = parser.parse_args()
	main(issue=args.issue, replace=args.force_replace)

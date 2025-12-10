./bin/python site/bin/console.py

from frontend.consumer.locator import locator as consumer_locator
import config_store
pard = config_store.application_parameters(use_ws=True)
consumer_service = consumer_locator.get_service("ConsumerPOS",
			COD_NEGOZIO=pard['POS_CONFIG']['COD_NEGOZIO'],
			user=pard['USER'],
			locale=pard['POS_CONFIG']['GUI_LANGUAGE_LOCALE'],
			language=pard['POS_CONFIG']['GUI_LANGUAGE'])
statistics = consumer_service.get_consumer_statistics('10135211', 10, filter_available_brands=pard['POS_CONFIG']['AVAILABLE_BRANDS'])

top_classi = statistics["statistiche"]["negozio"]["top_classi"]['classi']
top_classi = [{'classe': classe['classe'], 'descrizione': classe['descrizione'].decode('utf-8')}for classe in top_classi]
statistics["statistiche"]["negozio"]["top_classi"]['classi'] = top_classi

res = consumer_locator.get_view('StatisticheConsumer').render({
  "statistics": statistics,
  "date_format": pard['POS_CONFIG']['DATE_FORMAT'],
  "PATH_INCLUSION_ICONS": pard["PATH_INCLUSION_ICONS"],
  "PATH_INCLUSION_IMAGES": pard["PATH_INCLUSION_IMAGES"],
  "is_japan": False,
  "STORE_SIGN": pard['POS_CONFIG']['STORE_SIGN'],
  "MEDIA_PHOTO_BASE_URL": pard['POS_CONFIG']["MEDIA_PHOTO_BASE_URL"],
  "MEDIA_PHOTO_BASE_URL_NEW": pard['POS_CONFIG']["MEDIA_PHOTO_BASE_URL_NEW"],
  "sid": pard['POS_CONFIG']['REMOTE_SID']
})


----

from frontend.consumer.locator import locator as consumer_locator
import config_store
pard = config_store.application_parameters(use_ws=True)
consumer_service = consumer_locator.get_service("Consumer",
  COD_NEGOZIO=pard['POS_CONFIG']['COD_NEGOZIO'],
)
stats = consumer_service.get_consumer_statistics('10135211', sku_limit=None, filter_available_brands=pard['POS_CONFIG']['AVAILABLE_BRANDS'])

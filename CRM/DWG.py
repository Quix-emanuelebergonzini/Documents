from consumer.locator import locator as loc
self = loc.get_service("Consumer")
conn = self.get_connection("dwg")
conn.query("""
    SELECT pk_consumer, dataora_ultimo_login FROM d_consumatrice_myaccount where brand = 'MA' and country = 'IT' and pk_consumer <> '0'
""")

conn.query(""" 
    describe d_consumatrice_myaccount
""")

from consumer.locator import locator as loc
self = loc.get_service("Consumer")
conn = self.get_connection("dwg")
conn.query("""
    SELECT
        recency, frequency, monetary_worldwide, monetary_regional, cluster, propensity_churn, cltv, 
        data_ultimo_acquisto, n_case_aperti, recency_rest_mmfg, cltv_rest_mmfg
    FROM kpi_insegna
    WHERE 1
    LIMIT 20
""")
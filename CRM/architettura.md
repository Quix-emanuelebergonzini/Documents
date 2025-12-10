con il passaggio a https del crm di produzione
hanno fatto in modo che il

fe serva solo le risorse statiche (css+js+html),
la parte python di fe (come le view) è erogata dal server di be

---- gestione delle branch ---
le branch (al 99%) escono da MASTER
le branch per essere testate su crm-test devono essere mergiate dentro RELEASE

le branch per essere portate in produzione devono essere mergiate dentro MASTER e poi da MASTER  a PRODUCTION




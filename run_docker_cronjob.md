emanuelebergonzini@MacBook-Pro-4 ~ % LANDSCAPE=PRODUCTION MEMORY=3000 /Users/emanuelebergonzini/projects/repos/possededt/docker/run_job.sh /env/bin/python /source/guest/posws/bin/poswsbe/pos_export_to_store_db.py incr -p10 0000000522 -f

Flag --short has been deprecated, and will be removed in the future. The --short output will become the default.

error: error executing jsonpath "{.items[-1:].metadata.name}": Error executing template: array index out of bounds: index -1, length 0. Printing more information for debugging the template:
	template was:
		{.items[-1:].metadata.name}
	object given to jsonpath engine was:
		map[string]interface {}{"apiVersion":"v1", "items":[]interface {}{}, "kind":"List", "metadata":map[string]interface {}{"resourceVersion":""}}


emanuelebergonzini@MacBook-Pro-4 ~ % gke-gcloud-auth-plugin
{
    "kind": "ExecCredential",
    "apiVersion": "client.authentication.k8s.io/v1beta1",
    "spec": {
        "interactive": false
    },
    "status": {
        "expirationTimestamp": "2023-11-15T09:19:31Z",
        "token": "XXXXXX"
    }
}%                                                                                                                                                              emanuelebergonzini@MacBook-Pro-4 ~ % 

avviene quando non ci sono cronjob configurati

quello script recupera un cronjob a caso e ne copia la definizione (che non sarebbe banale includere nei sorgenti del
sosftware, essendo basata su app_container.yml, configmap, secret, ...), quindi occorre esista almeno un cronjob per farcela
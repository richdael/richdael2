from azure.identity import AzureCliCredential
import os


#credential
credential = AzureCliCredential()

#Récupération de l'ID d'abonnement à partir de la variable.
subscription_id = os.environ["Azure_Sub_Id"] = "aaf6ab19-4b31-4e75-9f48-4f12ac0ef41d"
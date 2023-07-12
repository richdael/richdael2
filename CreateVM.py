import logging
from azure.mgmt.compute import ComputeManagementClient
import Config
import Location
import CreateRG
import CreateSubnet
import CreateIpAdresse
import CreateNSG
import CreateNiC
import CreateVnet
import CreateName


#Démarrage
print(f"VM 정보 입력 완료!")

# Step 1 Créer un groupe de ressources
CreateRG

# Step 2 Mettre en service le réseau virtuel
CreateVnet

# Step 3 - Créer le sous-réseau
CreateSubnet

# Step 4 - Créer l'adresse IP
CreateIpAdresse

# Step 5 -Créer le NSG avec le port RDP
CreateNSG

# Step 6 - Créer le network interface
CreateNiC

# Step 7 - VMname 
CreateName

# Step 8 - Création de la VM | Configuration de base
Compute_client = ComputeManagementClient(Config.credential, Config.subscription_id)


print(f"{CreateName.VM_NAME} VM 생성 시작!")
# sizing & Version
poller = Compute_client.virtual_machines.begin_create_or_update(CreateRG.RESOURCE_GROUP_NAME, CreateName.VM_NAME,
{
    "location": Location.LOCATION,
    "storage_profile": {
        "image_reference": {
            "publisher": 'MicrosoftWindowsServer',
            "offer": "WindowsServer",
            "sku": "2022-datacenter-g2",
            "version": "latest"
        }
    },
    "hardware_profile":{
        "vm_size": "Standard_D2ds_v4"
    },
    "os_profile":{
        "computer_name": CreateName.VM_NAME,
        "admin_username": CreateName.Username,
        "admin_password": CreateName.PASSWORD
    },
    "network_profile": {
        "network_interfaces": [{
            "id": CreateNiC.nic_result.id,
        }]
    }
})
vm_result = poller.result()

print(f" {vm_result.name} 생성완료!")


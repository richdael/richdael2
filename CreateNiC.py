import GetObjectNetwork
import CreateRG
import Location
import CreateNSG
import CreateSubnet
import CreateIpAdresse
import Config
import CreateName

network_client = GetObjectNetwork.NetworkManagementClient(Config.credential, Config.subscription_id)
NIC_NAME = CreateName.VM_NAME
IP_CONFIG_NAME = CreateName.VM_NAME


poller = network_client.network_interfaces.begin_create_or_update(CreateRG.RESOURCE_GROUP_NAME, NIC_NAME, {
    "location" : Location.LOCATION,
    'network_security_group': {
        'id': CreateNSG.nsg_result.id
    },
    "ip_configurations": [{
        "name" : IP_CONFIG_NAME,
        "subnet" : { "id": CreateSubnet.subnet_result.id},
        "public_ip_address": {"id": CreateIpAdresse.ip_address_result.id}

    }]
})
nic_result = poller.result()

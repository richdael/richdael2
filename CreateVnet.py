import GetObjectNetwork
import CreateRG
import Location
import Config
import CreateName

network_client = GetObjectNetwork.NetworkManagementClient(Config.credential, Config.subscription_id)

VNET_NAME = CreateName.VM_NAME

poller = network_client.virtual_networks.begin_create_or_update(CreateRG.RESOURCE_GROUP_NAME,
    VNET_NAME,
    {
        "location": Location.LOCATION,
        "address_space" : {
            "address_prefixes": ["10.2.0.0/16"]
        }
    }
)
vnet_result = poller.result()


from manage_vm_instance import ManageVirtualMachine
from config import load_config, load_os_env
from helper.print_output import prettify_json

# load environmental variable
load_os_env()

vm = ManageVirtualMachine(service_name=load_config()['service'],
                          version=load_config()['version'])

# list instances
# prettify_json(vm.list_vm_instance(project=load_config()['project_id'],
#                                 zone=load_config()['zone']))

prettify_json(vm.delete_vm_instance(project=load_config()['project_id'],
                                    zone=load_config()['zone'],
                                    instance=load_config()['instance']))

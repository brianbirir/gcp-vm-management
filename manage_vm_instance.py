from googleapiclient.discovery import build


class ManageVirtualMachine:

    def __init__(self, service_name, version):
        self.service_name = service_name
        self.version = version

    def compute(self):
        """Connection to Google Cloud Platform compute service

        Args:
            service (str): API service in this case the compute engine service
            version(str): API service version
        Returns:
            service resource object
        """
        return build(self.service_name,
                     self.version)

    def create_vm_instance(self, project, zone):
        """Create Google Compute Engine virtual machine instance
        Args:
            compute (obj): service resource object
            project (str): id of the project in GCP
            zone (str): the name of zone the instance belongs to
        """
        pass

    def list_vm_instance(self, project, zone):
        """Generate a list of instances found in the project
        Args:
            compute (obj): service resource object
            project (str): id of the project in GCP
            zone (str): the name of zone the instance belongs to
        Returns:
            list: a list of dictionary items containing GCP instances
        """
        result = self.compute().instances().list(project=project,
                                                 zone=zone).execute()
        return result['items'] if 'items' in result else None

    def delete_vm_instance(self, project, zone, instance):
        """Deletes a GCP engine instance in the specified project
        Args:
            compute (obj): service resource object
            project (str): id of the project in GCP
            zone (str): the name of zone the instance belongs to
        """
        return self.compute().\
            instances().\
            delete(project=project,
                   zone=zone,
                   instance=instance).\
            execute()

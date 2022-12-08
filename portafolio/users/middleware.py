from ipware import get_client_ip
from . models import IpClientes


class IPIsvalid:

    def __init__(self,get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        print(request)
        ip, is_routable = get_client_ip(request)
        print(f"ip: {ip}")
        IpClientes.objects.create(ip_address=str(ip))

        response = self.get_response(request)

        return response
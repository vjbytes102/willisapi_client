# website:   https://www.brooklyn.health
from http import HTTPStatus

from willisapi_client.willisapi_client import WillisapiClient
from willisapi_client.services.auth.auth_utils import AuthUtils

def create_user(key: str, client_email: str , client_name: str) -> str:
    """
    ---------------------------------------------------------------------------------------------------

    This is the signup function to access willisAPI signup API

    Parameters:
    ............
    key: str
        Temporary access token
    client_email: str
        expected onboarded userid
    client_name: str
        expected group name without empty spaces

    Returns:
    ............
    status : str
        Onboard succes/fail message

    ---------------------------------------------------------------------------------------------------
    """

    wc = WillisapiClient()
    url = wc.get_signup_url()
    headers = wc.get_headers()
    headers['Authorization'] = key
    data = dict(client_email=client_email, client_name=client_name)
    response = AuthUtils.signup(url, data, headers, try_number=1)
    if response and 'status_code' in response and response['status_code'] == HTTPStatus.OK:
        print(f"Signup Successful for client: {client_name}, client_email: {client_email}")
        return response['message']
    else:
        print(f"Signup Failed")
        return None

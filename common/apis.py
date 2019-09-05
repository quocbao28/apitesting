from common.json_helper import *

class APIS():
    def __init__(self, env):
        self.env = env

    @property
    def DOMAIN(self):
        return get_domain(self.env)
    
    @property
    def PROTOCAL(self):
        return get_protocal(self.env)
    
    def GET_OPPORTUNITY_API(self, oppID):
        return "%s://%s/ivy/api/epilot-cloud/v1/opportunities/%s" % (self.PROTOCAL, self.DOMAIN, oppID)

    @property
    def ORG_ADDRESS_API_ROUTE(self):
        return "%s://%s/ivy/api/epilot-cloud/v1/organization/geodata" % (self.PROTOCAL, self.DOMAIN)

    @property
    def CREATE_OPPORTUNITY_API(self):
        return "%s://%s/ivy/api/epilot-cloud/v1/opportunities" % (self.PROTOCAL, self.DOMAIN)


    GET_ACCESS_TOKEN_ROUTE = "https://keycloak.k8s.epilot.space/auth/realms/epilot/protocol/openid-connect/token"
    



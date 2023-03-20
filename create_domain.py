#Create WLD
import requests
import json
import sys
import time
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class CreateDomain:
    def __init__(self):
        print('Create Domain')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]

    def create_workload_domain(self):
        #validations
        payload = self.utils.read_input(os.path.abspath(__file__ +'/../')+'/domain_creation_spec.json')
        validations_url =  'https://'+self.hostname+'/v1/domains/validations'
        print ('Validating the input....')
        response = self.utils.post_request(payload,validations_url)
        if(response['resultStatus'] != 'SUCCEEDED'):
            print ('Validation Failed.')
            exit(1)
        
        #Domain Creation
        domain_creation_url = self.hostname + '/v1/domains'
        response = self.utils.post_request(payload,domain_creation_url)
        print ('Creating Domain...')

        task_url = 'https://'+self.hostname+'/v1/tasks/'+response['id']
        print ("Domain creation task completed with status:  " + self.utils.poll_on_id(task_url,True) )

if __name__== "__main__":
    CreateDomain().create_workload_domain()


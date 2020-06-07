import sys
import requests
import json
from jsonschema import validate
import time

API_ENDPOINT = "https://api-ropsten.opencerts.io/verify"
HEADER = {"Content-Type":"application/json"}
SCHEMA_PATH = {"scheme.json"}

#Debug
DEBUG_FLAG = False

def verify_cert(cert_str):
    #add document tag for json in the contenst of the request
    cert_doc = "{\"document\":" + cert_str + "}"

    pre_time = time.time()
    resp = requests.post(API_ENDPOINT, data=cert_doc, headers=HEADER)
    post_time = time.time()
    print("->Certificate verification done, taking {}".format(post_time-pre_time))
    if resp.status_code == requests.codes.ok:
        result = resp.json()
        if DEBUG_FLAG:
            print(result)
        if (result["summary"]["all"] == True):
            return True
        else:
            print("Invalid Certificate with status: {}".format(result["summary"]))
            return False
    else:
        print("Verification service failed with code {}".format(resp.status_code))
        return False

def verify_cert_url(url):
    pre_time = time.time()
    resp = requests.get(url)
    post_time = time.time()
    if DEBUG_FLAG:
        print(resp.status_code)
        print(resp.headers)
        print(resp.content)
    print("->Fetch certificate content done, taking {}".format(post_time-pre_time))
    if resp.status_code == 200:
        #TODO check if the resp is a byte object
        # check if resp follow the right json schema
        try:
            cert_str = resp.content.decode('ascii')
            return verify_cert(cert_str), cert_str
        except Exception as e:
            print("Unable to decode certificate with exception {}".format(e))
            return False, None
    else:
        print("Unable to fetch certificate with code {}".format(resp.status_code))
        return False, None

def validate_schema(cert_str):
    cert = json.loads(cert_str)
    schema_file = open(SCHEMA_PATH,"r")
    schema = schema_file.readlines()
    try:
        validate(instance=cert, schema=schema)
    except:
        return False
    return True

if __name__ == "__main__":
    infile_path = sys.argv[1]
    cert_file = open(infile_path, "r")
    cert = cert_file.read()
    print(verify_cert(cert))
    #print(verify_cert_url("https://api.myjson.com/bins/12gnkw"))

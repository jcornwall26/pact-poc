import atexit
import unittest

from pact import Consumer, Provider, Like
from consumer import repositories

pact = Consumer('ScoreCard-Module', version='1.0.2').has_pact_with(Provider('ScoreCard-Service'), 
    port='1234', 
    host_name='localhost',
    publish_to_broker=True, 
    pact_dir='./') 
pact.start_service()
atexit.register(pact.stop_service)

class GetRepositories(unittest.TestCase):
  def test_repositories(self):
    expected = self.expected_body()

    (pact
     .given('repositories are populated')
     .upon_receiving('a request for all repositories')
     .with_request('get', '/v1/repositories/')
     .will_respond_with(200, body=expected))

    with pact:
      result = repositories()

    self.assertEqual(result, expected)
  
  def expected_body(self):
    return {
      "data": [{
          "type": "repositories",
          "id": "kiwi-server-cne",
          "attributes": {
            "template_type": "kiwi-server",
            "template_version": "1.1.0",
            "runtime": "python.x"
          }
        },
        {
          "type": "repositories",
          "id": "kiwi-module-pdp",
          "attributes": {
            "template_type": "kiwi-module",
            "template_version": "1.0.5",
            "runtime": None
          }
        },
        {
          "type": "repositories",
          "id": "kiwi-module-stores",
          "attributes": {
            "template_type": "kiwi-module",
            "template_version": "2.0.1",
            "runtime": None
          }
        },
        {
          "type": "repositories",
          "id": "kiwi-module-cdp",
          "attributes": {
            "template_type": "kiwi-module",
            "template_version": "2.0.1",
            "runtime": None
          }
        },
        {
          "type": "repositories",
          "id": "ecom-web-app",
          "attributes": {
            "template_type": "nextjs-lambda",
            "template_version": "2.0.1",
            "runtime": "nodejs12.x"
          }
        },
        {
          "type": "repositories",
          "id": "ecom-checkout-client",
          "attributes": {
            "template_type": "nextjs-lambda",
            "template_version": "1.0.0",
            "runtime": "nodejs12.x"
          }
        }
      ]
    }

import atexit
import unittest

from pact import Consumer, Provider, Verifier
from consumer import repositories


pact = Consumer('ScoreCard-Module').has_pact_with(Provider('ScoreCard-Service'), port='8080', host_name='localhost') 

class GetRepositories(unittest.TestCase):
    def test_provider(self):
        verifier = Verifier(provider='ScoreCard-Service',
                        provider_base_url='http://mwa-scorecard-nodejs-swagger-ecs.lllapi.vision:3090')

        output, logs = verifier.verify_pacts('https://lululemon-jsc.pactflow.io/pacts/provider/ScoreCard-Service/latest', publish_verification_results=True)

        

export PACT_BROKER_BASE_URL = https://lululemon-jsc.pactflow.io
export PACT_BROKER_TOKEN = Ydnx0IixDBGx42y3knhsng

install-pact-cli:
	curl -LO https://github.com/pact-foundation/pact-ruby-standalone/releases/download/v1.88.58/pact-1.88.58-osx.tar.gz
	tar xzf pact-1.88.58-osx.tar.gz
	cd pact/bin
	./pact-mock-service --help start
	./pact-provider-verifier --help verify

init-pact-broker:
	docker run -d -p 8080:8080 -p 20000-20010:20000-20010 --name pact-broker uglyog/pact-jvm-server 

start-pact-broker: 
	docker start pact-broker

stop-pact-broker: 
	docker kill pact-broker

run-consumer-tests:
	python -m pytest -c ./tests.ini ./test_consumer.py 

verify-pacts:
	pact-verifier --provider=ScoreCard-Service --provider-base-url=http://mwa-scorecard-nodejs-swagger-ecs.lllapi.vision:3090 --pact-url=https://lululemon-jsc.pactflow.io/pacts/provider/ScoreCard-Service/latest --publish-verification-results --provider-app-version=1.0.0

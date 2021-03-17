##  customer-api


### choice of technology
Django-rest + sqlite was chosen primarily because of development time constraint. "Include a persistent data store", "no Java", "no performance requirements" were important factors in choice.

Development time is still an important consideration in other cases. python-django is in no way a performance dead end. Simple API's like this will more or less comfortably scale to 100-s of RPS per core with good data store and caching.

If 10000+ RPS were required, I would suggest (not in particular order):
1) compiled language, like Rust or C++
2) scalable data store, like Postgres or MariaDB for given task 
3) nginx reverse proxy
4) denser serialization format, like protobuf


### installation


        python3 -m venv customer-api-venv
        . ./customer-api-venv/bin/activate
        pip install -r requirements.txt
        
        # run e.g. with gunicorn 
        pip3 install gunicorn
        gunicorn customer_api.wsgi


### usage

list customers:
curl http://localhost:8000/company/1/

Filter and sort customers
curl "http://localhost:8000/customer/?company__id=2" 
curl "http://localhost:8000/customer/?company__id=1&ordering=-lastName" 
curl "http://localhost:8000/customer/?status=active" 
curl "http://localhost:8000/customer/?company__id=2&status=prospective" 

Creating note for customer 1 with POST
curl 'http://127.0.0.1:8000/company/customer/note/' -H 'Content-Type: application/json' \
  --data-raw $'{"text": "new", "customer": "http://127.0.0.1:8000/company/customer/1/", "version": 1}' 

Same idea for customer and company. The API is explorable with web browser: http://127.0.0.1:8000/company/customer/ and  http://127.0.0.1:8000/company/customer/ 

Optimistically-locked PUT of customer record (version must match):
curl 'http://127.0.0.1:8000/company/customer/note/4/' -X PUT  --data-raw $'{"id": 4,"text": "new32","customer": "http://127.0.0.1:8000/company/customer/1/", "version": 1616022919256964}'


### total development time

A bit over 3 hours
== customer-api ==


=== choice of technology ===
Django-rest + sqlite was chosen primarily because of development time constraint. "Include a persistent data store" and "no Java" were also factors in choice.

Development time is still an important consideration in other cases. python-django is in no way a performance dead end. Simple API-s like this will more or less comfortably scale to 100-s of RPS per core.


If 10000+ RPS was in sight, I would suggest (not in particular order)
1) compiled language, like Rust or C++
2) scalable data store, loke postgres or MariaDB for given task 
3) nginx reverse proxy
4) denser serialization format, like protobuf


=== installation === 

python3 -m venv customer-api-venv
. ./customer-api-venv/bin/activate

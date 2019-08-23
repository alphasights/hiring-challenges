# AlphaSights New Strategy

After extensive research, AlphaSight's Product team figured out that we can significantly improve our relationship with our clients if the links we share with them are shorter because it would make it easier for them to share those links.

## Dependencies
* Flask==1.1.1
* requests==2.22.0
* hashids==1.2.0

## Running the application
FLASK_APP=app flask run

## Running the tests
python -m  unittest -v


## Sample requests

```bash
# shortens an url
curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" -d '{"url": "http://alphasights.com"}'
# {"short_url":"http://localhost:5000/vwM8r32"}

curl -X POST http://localhost:5000/shorten -H "Content-Type: application/json" -d '{"url": "http://google.com"}'
# {"short_url":"http://localhost:5000/75jNXXr"}

# listening shortened urls
curl http://localhost:5000/list
# [{"vwM8r32":{"original":"http://alphasights.com","shortened":"http://localhost:5000/vwM8r32"}},{"75jNXXr":{"original":"http://google.com","shortened":"http://localhost:5000/75jNXXr"}}]

# checking a redirection
curl -I http://localhost:5000/vwM8r32
# HTTP/1.0 302 FOUND
# Content-Type: text/html; charset=utf-8
# Location: http://alphasights.com

# deleting a shortened url
curl -I http://localhost:5000/75jNXXr
# Location: http://google.com
curl -I -X DELETE http://localhost:5000/75jNXXr
# 200
curl -I http://localhost:5000/75jNXXr
# 404



```
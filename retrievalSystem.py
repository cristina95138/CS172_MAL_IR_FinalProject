from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

f = open('output.txt', 'r')
contents = f.read()
f.close()

doc = {
	    "settings" : {
	        "number_of_shards": 5,
	        "number_of_replicas": 1
	    },

	    'mappings': {
	        'examplecase': {
	            'properties': {
	                'anime': {'index': 'not_analyzed', 'type': 'string'},
	                'rating': {'index': 'not_analyzed', 'type': 'string'},
	                'description': {'index': 'not_analyzed', 'type': 'string'},
	                'rank': {'index': 'analyzed', 'type': 'string'},
	                'episodes': {'index': 'not_analyzed', 'type': 'string'},
	            }}}
	}

index = es.indices.create(index='mal_index', body=doc)

result = es.search(
          index="contents",
          body={
              "query": {
                  "match_all": {}
              }
          }
)

all_hits = result['hits']['hits']
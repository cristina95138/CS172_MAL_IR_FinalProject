from elasticsearch import Elasticsearch, helpers
import csv
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

with open('output.csv') as f:
	reader = csv.DictReader(f)
	helpers.bulk(es, reader, index='animes')

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
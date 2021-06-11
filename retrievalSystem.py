from elasticsearch import Elasticsearch, helpers
import csv
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def createIndex():
	with open('output.csv') as f:
		reader = csv.DictReader(f)
		#es.indices.delete(index='animes')
		helpers.bulk(es, reader, index='animes')

result = es.search(
        index="animes",
        body={
            "query": {
                "match_all": {}
            }
        }
)

all_hits = result['hits']['hits']

all_hits
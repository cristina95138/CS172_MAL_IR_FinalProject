from elasticsearch import Elasticsearch, helpers
import csv
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def createIndex():
    with open('output.csv') as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader, index='animes')

createIndex()

result = es.search(
        index="animes",
        body={
            "query": {
                "match": {
                    "name": "Boku"
                }
            }
        }
)

all_hits = result['hits']['hits']

all_hits

#es.indices.delete(index='animes')
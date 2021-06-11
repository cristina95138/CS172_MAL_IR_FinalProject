from elasticsearch import Elasticsearch, helpers
import csv
import sys
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

with open('output.csv') as f:
    reader = csv.DictReader(f)
    es.indices.delete(index='animes')
    helpers.bulk(es, reader, index='animes')

searching = True

while searching:
    search = input("Search (to exit type 'exit'): ")

    if (search == 'exit') or (search == 'Exit'):
        break
    else:
        result = es.search(
            index="animes",
            body={
                "query": {
                    "multi_match": {
                        "query": search,
                        "fields": ["name", "rating", "description", "rank", "num_episodes"]
                    }
                }
            }
        )
    all_hits = result['hits']['hits']

    for hit in all_hits:
        print("Name:", hit['_source']['name'])
        print("Rating:", hit['_source']['rating'])
        print("Description:", hit['_source']['description'])
        print("Rank:", hit['_source']['rank'])
        print("Number of Episodes:", hit['_source']['num_episodes'])
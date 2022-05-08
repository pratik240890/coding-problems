# codility problem
# Read the json file and find the first matching tag from the movie list using generator
# Use search function as generator to find movie with matching tag
# Use first function to get the first matching resutl

import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        if not self.query or not self._data:
            raise StopIteration

        try:
            self._data['items']
        except KeyError:
            raise StopIteration

        for item in self._data['items']:
            if not item:
                raise StopIteration

            tags = item.get('tags', None)

            if not tags:
                continue

            if self.query in tags:
                yield item

    def first(self):
        return self.search().__next__()


if __name__ == "__main__":
    search_1 = SearchByTag('problems/codility/movies.json', 'crime')
    first = search_1.first()
    print(first)

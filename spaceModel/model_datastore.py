# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, email, date, message ]
    where name, email, and message are Python strings
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['title'],entity['dayOf'],entity['url'],entity['explanation'],entity['copyright']]


class model(Model):
    def __init__(self):
        self.client = datastore.Client('nasapotdf21')

    def select(self):
        query = self.client.query(kind = 'potd')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self, title, dayOf, url, explanation, copyright):
        key = self.client.key('potd')
        rev = datastore.Entity(key)
        rev.update( {
            'title': title,
            'dayOf' : dayOf,
            'url' : url,
            'explanation' : explanation,
            'copyright': copyright
            })
        self.client.put(rev)
        return True

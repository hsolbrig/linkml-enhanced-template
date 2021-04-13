import pyld
from rdflib_pyld_compat import rdflib_graph_from_pyld_jsonld

from examples.basic import Person
from linkml.dumpers import json_dumper, rdf_dumper, yaml_dumper
from linkml.loaders import yaml_loader, rdf_loader

sam = Person("1172438", first_name=["Samual", "J"], last_name="Snooter")
print(sam)
fred = Person("a117", first_name="John")
ann = Person("17a3923", first_name="Jill", last_name="Jones", knows=[sam.id])

print(json_dumper.dumps(ann))
print(yaml_dumper.dumps(ann))

print(rdf_dumper.dumps(ann, contexts="../examples/jsonld/basic.context.jsonld"))

inp = """[
  {
    "@type": [
      "https://schema.org/Person"
    ],
    "https://schema.org/givenName": [
      {
        "@value": "Jill"
      }
    ],
    "@id": "https://example.org/linkml/hello-world/17a3923",
    "http://xmlns.com/foaf/0.1/knows": [
      {
        "@id": "https://example.org/linkml/hello-world/1172438"
      }
    ],
    "https://schema.org/familyName": [
      {
        "@value": "Jones"
      }
    ]
  }
]"""
g = rdflib_graph_from_pyld_jsonld(inp)
g.bind('sdo', "https://schema.org/")
g.bind('foaf', "http://xmlns.com/foaf/0.1/")
print(g.serialize(format="turtle").decode())

from linkml.loaders import yaml_loader

fred = yaml_loader.load('input/fred.yaml', target_class=Person)
print(fred.first_name)


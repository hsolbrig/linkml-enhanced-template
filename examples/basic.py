# Auto generated from basic.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-08 14:00
# Schema: person
#
# id: https://example.org/linkml/person
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EX = CurieNamespace('ex', 'https://example.org/linkml/hello-world/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EX


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = EX.String


# Class references
class PersonId(extended_str):
    pass


@dataclass
class Person(YAMLRoot):
    """
    Minimal information about a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SDO.Person
    class_class_curie: ClassVar[str] = "sdo:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = EX.Person

    id: Union[str, PersonId] = None
    first_name: Union[str, List[str]] = None
    last_name: str = None
    knows: Optional[Union[Union[str, PersonId], List[Union[str, PersonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.first_name is None:
            raise ValueError("first_name must be supplied")
        elif not isinstance(self.first_name, list):
            self.first_name = [self.first_name]
        elif len(self.first_name) == 0:
            raise ValueError(f"first_name must be a non-empty list")
        self.first_name = [v if isinstance(v, str) else str(v) for v in self.first_name]

        if self.last_name is None:
            raise ValueError("last_name must be supplied")
        if not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self.knows is None:
            self.knows = []
        if not isinstance(self.knows, list):
            self.knows = [self.knows]
        self.knows = [v if isinstance(v, PersonId) else PersonId(v) for v in self.knows]

        super().__post_init__(**kwargs)


# Enumerations


# Slots


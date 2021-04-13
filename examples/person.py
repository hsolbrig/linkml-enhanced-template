# Auto generated from person.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-08 14:00
# Schema: person
#
# id: http://example.org/sample/person
# description: A small example of a particular view of a person
# license:

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
from linkml.utils.metamodelcore import Bool

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PERS = CurieNamespace('pers', 'http://example.org/sample/person/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = PERS


# Types
class String(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = PERS.String


class Int(int):
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "int"
    type_model_uri = PERS.Int


class Boolean(Bool):
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = PERS.Boolean


# Class references
class PersonId(extended_str):
    pass


class FriendlyPersonId(PersonId):
    pass


@dataclass
class Person(YAMLRoot):
    """
    A person, living or dead
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Person
    class_class_curie: ClassVar[str] = "foaf:Person"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = PERS.Person

    id: Union[str, PersonId] = None
    last_name: str = None
    first_name: Optional[Union[str, List[str]]] = empty_list()
    living: Optional[Bool] = None
    age: Optional[int] = None
    knows: Optional[Union[Union[str, PersonId], List[Union[str, PersonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.last_name is None:
            raise ValueError("last_name must be supplied")
        if not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self.first_name is None:
            self.first_name = []
        if not isinstance(self.first_name, list):
            self.first_name = [self.first_name]
        self.first_name = [v if isinstance(v, str) else str(v) for v in self.first_name]

        if self.living is not None and not isinstance(self.living, Bool):
            self.living = Bool(self.living)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if self.knows is None:
            self.knows = []
        if not isinstance(self.knows, list):
            self.knows = [self.knows]
        self.knows = [v if isinstance(v, PersonId) else PersonId(v) for v in self.knows]

        super().__post_init__(**kwargs)


@dataclass
class FriendlyPerson(Person):
    """
    A person that knows at least one other person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PERS.FriendlyPerson
    class_class_curie: ClassVar[str] = "pers:FriendlyPerson"
    class_name: ClassVar[str] = "friendly_person"
    class_model_uri: ClassVar[URIRef] = PERS.FriendlyPerson

    id: Union[str, FriendlyPersonId] = None
    last_name: str = None
    knows: Union[Union[str, PersonId], List[Union[str, PersonId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, FriendlyPersonId):
            self.id = FriendlyPersonId(self.id)

        if self.knows is None:
            raise ValueError("knows must be supplied")
        elif not isinstance(self.knows, list):
            self.knows = [self.knows]
        elif len(self.knows) == 0:
            raise ValueError(f"knows must be a non-empty list")
        self.knows = [v if isinstance(v, PersonId) else PersonId(v) for v in self.knows]

        super().__post_init__(**kwargs)


# Enumerations


# Slots


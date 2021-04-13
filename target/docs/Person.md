
# Class: Person


A person (alive, dead, undead, or fictional).

URI: [sdo:Person](https://schema.org/Person)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Person&#124;givenName:Text%20*;additionalName:Text%20*;gender:gender_enum%20%3F;identifier(i):Text%20*;url(pk)(i):URL;name(i):Text])

## Parents

 *  is_a: [Thing](Thing.md) - The most generic type of item.

## Attributes


### Own

 * [additionalName](additionalName.md)  <sub>0..*</sub>
     * Description: An additional name for a person, can be used as a middle name.
     * range: [Text](types/Text.md)
 * [gender](gender.md)  <sub>OPT</sub>
     * Description: Person gender
     * range: 
 * [givenName](givenName.md)  <sub>0..*</sub>
     * Description: Given name. In the U.S., the first name of a Person.
     * range: [Text](types/Text.md)

### Inherited from Thing:

 * [identifier](identifier.md)  <sub>0..*</sub>
     * Description: The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes,
UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings
or as URL (URI) links. See background notes for more details.
     * range: [Text](types/Text.md)
 * [name](name.md)  <sub>REQ</sub>
     * Description: The name of the item.
     * range: [Text](types/Text.md)
 * [url](url.md)  <sub>REQ</sub>
     * Description: URL of the item
     * range: [URL](types/URL.md)

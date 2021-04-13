
# Class: Thing


The most generic type of item.

URI: [sdo:Thing](https://schema.org/Thing)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Thing&#124;identifier:Text%20*;url(pk):URL;name:Text]^-[Person],[Person])

## Children

 * [Person](Person.md) - A person (alive, dead, undead, or fictional).

## Referenced by class


## Attributes


### Own

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


# Class: FriendlyPerson


A person that knows at least one other person

URI: [pers:FriendlyPerson](http://example.org/sample/person/FriendlyPerson)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Person],[Person]<knows%201..*-%20[FriendlyPerson&#124;id(i):string;first_name(i):string%20*;last_name(i):string;living(i):boolean%20%3F;age(i):int%20%3F],[Person]^-[FriendlyPerson])

## Parents

 *  is_a: [Person](Person.md) - A person, living or dead

## Referenced by class


## Attributes


### Own

 * [friendly_person➞knows](friendly_person_knows.md)  <sub>1..*</sub>
     * range: [Person](Person.md)

### Inherited from person:

 * [➞age](person__age.md)  <sub>OPT</sub>
     * Description: The age of a person if living or age of death if not
     * range: [Int](types/Int.md)
 * [➞first_name](person__first_name.md)  <sub>0..*</sub>
     * Description: The first name of a person
     * range: [String](types/String.md)
 * [➞id](person__id.md)  <sub>REQ</sub>
     * Description: The unique identifier of a person
     * range: [String](types/String.md)
 * [➞last_name](person__last_name.md)  <sub>REQ</sub>
     * Description: The last name of a person
     * range: [String](types/String.md)
 * [➞living](person__living.md)  <sub>OPT</sub>
     * Description: Whether the person is alive
     * range: [Boolean](types/Boolean.md)

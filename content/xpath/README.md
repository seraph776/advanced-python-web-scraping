# XPath

## XPath as filesystem addressing
The basic XPath syntax is similar to filesystem addressing. If the path starts with the slash / , then it represents an absolute path to the required element.
- `/AAA`
- `/AAA/CCC`
- `/AAA/DDD/BBB`

## Start with //

If the path starts with // then all elements in the document which fulfill following criteria are selected.
- `//BBB`
- `//DDD/BBB`

## All elements: *
The star * selects all elements located by preceeding path
- `/AAA/CCC/DDD/*`
- `/*/*/*/BBB`
- `//*`

## Further conditions inside []

Expresion in square brackets can further specify an element. A number in the brackets gives the position of the element in the selected set. The function last() selects the last element in the selection.
- `/AAA/BBB[1]`
- `/AAA/BBB[last()]`

## Attributes

Attributes are specified by @ prefix.

- `//@id`
- `//BBB[@id]`
- `//BBB[@name]`
- `//BBB[@*]`
- `//BBB[not(@*)]`

## Attribute values
Values of attributes can be used as selection criteria. Function normalize-space removes leading and trailing spaces and replaces sequences of whitespace characters by a single space.
- `//BBB[@id='b1']`
- `//BBB[@name='bbb']`
- `//BBB[normalize-space(@name)='bbb']`

## Nodes counting

Function count() counts the number of selected elements
- `//*[count(BBB)=2]`
- `//*[count(*)=2]`
- `//*[count(*)=3]`

## Playing with names of selected elements
Function name() returns name of the element, the starts-with function returns true if the first argument string starts with the second argument string, and the contains function returns true if the first argument string contains the second argument string.

`//*[name()='BBB']`
`//*[starts-with(name(),'B')]`
`//*[contains(name(),'C')]`

## Length of string
The string-length function returns the number of characters in the string. You must use &lt; as a substitute for < and &gt; as a substitute for > .
- //*[string-length(name()) = 3]`
- `//*[string-length(name()) < 3]`
- `//*[string-length(name()) > 3]`

## Combining XPaths with |

Several paths can be combined with | separator.
- `//CCC | //BBB`
- `/AAA/EEE | //BBB`
- `/AAA/EEE | //DDD/CCC | /AAA | //BBB`
## Child axis

The child axis contains the children of the context node. The child axis is the default axis and it can be omitted.
- `/AAA`
- `/child::AAA`
- `/AAA/BBB`
- `/child::AAA/child::BBB`
- `/child::AAA/BBB`

## Descendant axis

The descendant axis contains the descendants of the context node; a descendant is a child or a child of a child and so on; thus the descendant axis never contains attribute or namespace nodes
- `/descendant::*`
- `/AAA/BBB/descendant::*`
- `//CCC/descendant::*`
- `//CCC/descendant::DDD`

## Parent axis

The parent axis contains the parent of the context node, if there is one.

- `//DDD/parent::*`

## Ancestor axis
The ancestor axis contains the ancestors of the context node; the ancestors of the context node consist of the parent of context node and the parent's parent and so on; thus, the ancestor axis will always include the root node, unless the context node is the root node.
- `/AAA/BBB/DDD/CCC/EEE/ancestor::*`
- `//FFF/ancestor::*`

## Following-sibling axis
The following-sibling axis contains all the following siblings of the context node.
- `/AAA/BBB/following-sibling::*`
- `//CCC/following-sibling::*`

## Preceding-sibling axis

The preceding-sibling axis contains all the preceding siblings of the context node
- `/AAA/XXX/preceding-sibling::*`
- `//CCC/preceding-sibling::*`

## Following axis

The following axis contains all nodes in the same document as the context node that are after the context node in document order, excluding any descendants and excluding attribute nodes and namespace nodes.
- `/AAA/XXX/following::*`
- `//ZZZ/following::*`

## Preceding axis

The preceding axis contains all nodes in the same document as the context node that are before the context node in document order, excluding any ancestors and excluding attribute nodes and namespace nodes

- `/AAA/XXX/preceding::*`
- `//GGG/preceding::*`

## Descendant-or-self axis
The descendant-or-self axis contains the context node and the descendants of the context node
- `/AAA/XXX/descendant-or-self::*`
- `//CCC/descendant-or-self::*`

## Ancestor-or-self axis
The ancestor-or-self axis contains the context node and the ancestors of the context node; thus, the ancestor-or-self axis will always include the root node.
- `/AAA/XXX/DDD/EEE/ancestor-or-self::*`
- `//GGG/ancestor-or-self::*`

## Orthogonal axes

The ancestor, descendant, following, preceding and self axes partition a document (ignoring attribute and namespace nodes): they do not overlap and together they contain all the nodes in the document.

- `//GGG/ancestor::*`
- `//GGG/descendant::*`
- `//GGG/following::*`
- `//GGG/preceding::*`
- `//GGG/self::*`
- `//GGG/ancestor::* | //GGG/descendant::* | //GGG/following::* | //GGG/preceding::* | //GGG/self::*`

## Numeric operations
The div operator performs floating-point division, the mod operator returns the remainder from a truncating division. The floor function returns the largest (closest to positive infinity) number that is not greater than the argument and that is an integer.The ceiling function returns the smallest (closest to negative infinity) number that is not less than the argument and that is an integer.
- `//BBB[position() mod 2 = 0 ]`
- `//BBB[ position() = floor(last() div 2 + 0.5) or position() = ceiling(last() div 2 + 0.5) ]`
- `//CCC[ position() = floor(last() div 2 + 0.5) or position() = ceiling(last() div 2 + 0.5) ]`

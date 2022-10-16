<div id="top"  align="center">

# Render JavaScript

</div>


**HTML document**

```html

  <div id='footer'>
            <p>Footer Information</p>
        </div>
        <script>
        var para = document.createElement("p");
        var node = document.createTextNode("This is text generated by JavaScript.");
        para.appendChild(node);
        var element = document.getElementById("footer");
        element.appendChild(para);
        </script>
    </body>
</html>/html>
```

**Python file**


```python
from requests_html import HTMLSession, HTML

with open('test.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()


match = html.find('#footer', first=True).text
print(match)
```

**Output**


```cmd
Footer Information
This is text generated by JavaScript.
```
<div align="right">

[[↑] Back to top](#top)

</div>  
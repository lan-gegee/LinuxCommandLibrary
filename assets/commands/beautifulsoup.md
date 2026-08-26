# TAGLINE

解析并提取 HTML 和 XML 文档中的数据

# TLDR

**解析 HTML 并找出所有链接**

```python3 -c "from bs4 import BeautifulSoup; import requests; print([a['href'] for a in BeautifulSoup(requests.get('[url]').text, 'html.parser').find_all('a', href=True)])"```

**从 HTML 文件提取文本**

```python3 -c "from bs4 import BeautifulSoup; print(BeautifulSoup(open('[file.html]'), 'html.parser').get_text())"```

**按 CSS 类查找元素**

```python3 -c "from bs4 import BeautifulSoup; soup=BeautifulSoup(open('[file.html]'), 'html.parser'); print(soup.find_all(class_='[classname]'))"```

**按 ID 查找元素**

```python3 -c "from bs4 import BeautifulSoup; soup=BeautifulSoup(open('[file.html]'), 'html.parser'); print(soup.find(id='[element_id]'))"```

**用 CSS 选择器选取元素**

```python3 -c "from bs4 import BeautifulSoup; soup=BeautifulSoup(open('[file.html]'), 'html.parser'); print(soup.select('[div.class > p]'))"```

**格式化打印解析后的 HTML**

```python3 -c "from bs4 import BeautifulSoup; print(BeautifulSoup(open('[file.html]'), 'html.parser').prettify())"```

# SYNOPSIS

```python3 -c "from bs4 import BeautifulSoup; ..."```

# COMMON METHODS

**BeautifulSoup(markup, parser)**
> 用指定的解析器解析 HTML/XML 标记。

**soup.find(name, attrs)**
> 查找第一个匹配的元素。

**soup.find_all(name, attrs)**
> 查找所有匹配的元素。

**soup.select(css_selector)**
> 查找所有匹配 CSS 选择器的元素。

**soup.select_one(css_selector)**
> 查找第一个匹配 CSS 选择器的元素。

**element.get_text()**
> 从元素中提取文本内容。

**element['attribute']**
> 访问元素的属性值。

**element.string**
> 获取元素的直接字符串内容。

**soup.prettify()**
> 返回格式化后的 HTML 字符串。

# PARSERS

**html.parser**
> Python 内置解析器（无需额外依赖）。

**lxml**
> 基于 C 的高速解析器（需要 lxml 包）。

**lxml-xml**（或 **xml**）
> 使用 lxml 的 XML 解析器。

**html5lib**
> 类浏览器式解析（需要 html5lib 包）。

# DESCRIPTION

**Beautiful Soup** 是一个用于解析 HTML 和 XML 文档的 Python 库。它本身不是命令行工具，但常被用于 Python 单行命令和脚本中，执行网页抓取、数据提取和 HTML 处理等任务。

该库从 HTML 文档构建解析树，支持对树的遍历、搜索和修改。它可以配合多种解析器工作，并能优雅地处理格式错误的标记，因此非常适合抓取真实世界的网站。

Beautiful Soup 为解析树的遍历提供了符合 Python 习惯的方式，包括迭代、属性访问和 CSS 选择器支持。与处理 HTTP 的 requests 结合使用后，它构成了大多数 Python 网页抓取工作流的基础。

# INSTALLATION

```pip install beautifulsoup4```

```pip install lxml```  （可选，用于更快的解析）

```pip install html5lib```  （可选，用于类浏览器的解析）

# CAVEATS

Beautiful Soup 只负责解析；抓取网页需使用 requests 或 httpx。JavaScript 渲染的内容需要 Selenium 之类的浏览器自动化工具。默认的 html.parser 比 lxml 慢。网页抓取可能违反网站的服务条款；请务必检查 robots.txt 并限制请求频率。

# HISTORY

Beautiful Soup 由 **Leonard Richardson** 创建，于 **2004** 年首次发布。**2012** 年发布的版本 4（bs4）增加了对多种解析器和 Python 3 的支持。该库凭借简洁的 API 和处理残缺 HTML 的能力，成为最受欢迎的 Python 网页抓取工具之一。至今仍在积极维护并被广泛使用。

# SEE ALSO

[python](/man/python)(1), [scrapy](/man/scrapy)(1), [curl](/man/curl)(1), [wget](/man/wget)(1), [pup](/man/pup)(1)

# RESOURCES

```[Homepage](https://www.crummy.com/software/BeautifulSoup/)```

```[Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)```

<!-- verified: 2026-06-19 -->

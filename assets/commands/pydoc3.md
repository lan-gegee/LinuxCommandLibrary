# TAGLINE

Python 3 文档浏览器

# TLDR

**查看模块文档**

```pydoc3 [module]```

**搜索文档**

```pydoc3 -k [keyword]```

**启动文档服务器**

```pydoc3 -p [8080]```

**生成 HTML 文档**

```pydoc3 -w [module]```

**查看内置函数**

```pydoc3 [print]```

# SYNOPSIS

**pydoc3** [_options_] [_name_]

# PARAMETERS

**-k** _keyword_
> 搜索关键字。

**-p** _port_
> 启动 HTTP 服务器。

**-b**
> 打开浏览器访问服务器。

**-w** _module_
> 写入 HTML 文件。

**-n** _host_
> 服务器主机名。

# DESCRIPTION

**pydoc3** 是 Python 3 的文档浏览器。它显示 docstring 和模块内容，并可生成 HTML 文档或通过内置 Web 服务器提供文档。

# EXAMPLES

```bash
# View module docs
pydoc3 os
pydoc3 json.loads

# Search for topic
pydoc3 -k sort

# Start doc server
pydoc3 -p 8080
# Then browse http://localhost:8080

# With browser auto-open
pydoc3 -b

# Generate HTML
pydoc3 -w mymodule
```

# IN PYTHON

```python
# Get help in interpreter
help(str.split)

# Same as pydoc
import pydoc
pydoc.doc(str.split)
```

# CAVEATS

只显示 docstring 而非源码。要查看源码请使用 inspect 模块。属于 Python 标准库。

# HISTORY

pydoc 是 **Python** 标准库的一部分，自 Python 2.1 起就提供文档访问功能。

# INSTALL

```apt: sudo apt install python3```

```dnf: sudo dnf install python3```

```apk: sudo apk add python3```

```brew: brew install python3```

```nix: nix profile install nixpkgs#python3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python3](/man/python3)(1), [pydoc](/man/pydoc)(1), [pip](/man/pip)(1)

# TAGLINE

查看 Python 模块文档

# TLDR

**查看模块**的文档

```pydoc [module]```

**查看类或函数**的文档

```pydoc [module.ClassName]```

**按关键字搜索**模块概要

```pydoc -k [keyword]```

**启动本地文档 HTTP 服务器**

```pydoc -p [8080]```

**启动服务器并在**默认浏览器中打开

```pydoc -b```

**将 HTML 文档写入**当前目录下的文件

```pydoc -w [module]```

# SYNOPSIS

**pydoc** [**-k** _keyword_] [**-p** _port_] [**-b**] [**-w**] [_name_...]

# PARAMETERS

_name_
> 要生成文档的模块、软件包、类、函数或关键字。

**-k** _keyword_
> 在所有可用模块的概要行中搜索关键字。

**-p** _port_
> 在指定端口启动 HTTP 文档服务器。

**-b**
> 启动 HTTP 服务器并打开浏览器访问其页面。

**-w** _name_
> 将模块的 HTML 文档写入当前目录下的文件。

**-n** _host_
> HTTP 服务器的主机名（默认为 localhost）。需要 Python 3.11+。

# DESCRIPTION

**pydoc** 是 Python 内置的文档工具，显示由 docstring 和内省机制生成的模块文档。它可以在终端中显示模块、类、函数和关键字的文档，用 **-k** 在所有已安装模块中搜索，或用 **-w** 生成静态 HTML 文件。

**-p** 标志启动本地 HTTP 文档服务器，提供所有已安装 Python 模块的可浏览界面；**-b** 会自动在默认浏览器中打开该服务器。pydoc 属于 Python 标准库，提供与交互式 **help()** 函数相同的功能。

**PAGER** 环境变量控制终端显示所用的程序。**BROWSER** 环境变量控制 **-b** 所使用的浏览器。

# CAVEATS

文档质量取决于模块源码中是否含有 docstring。导入模块进行检查时可能执行模块级代码。用于指定服务器主机名的 **-n** 标志需要 Python 3.11+。

# HISTORY

**pydoc** 自 **Python 2.1**（2001 年）起就是 Python 标准库的一部分，由 **Ka-Ping Yee** 编写，作为内置文档查看器，提供与交互式 **help()** 函数相同的功能。

# SEE ALSO

[python](/man/python)(1), [python3](/man/python3)(1), [pydoc3](/man/pydoc3)(1)

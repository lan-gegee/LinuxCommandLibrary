# TAGLINE

Python 3.4 文档查看器

# TLDR

**查看模块文档**

```pydoc3.4 [module]```

**在模块概要中搜索**关键字

```pydoc3.4 -k [keyword]```

**启动文档 HTTP 服务器**

```pydoc3.4 -p [8080]```

**将 HTML 文档写入**文件

```pydoc3.4 -w [module]```

**查看类或函数**的文档

```pydoc3.4 [module.ClassName]```

# SYNOPSIS

**pydoc3.4** [_options_] [_name_]

# PARAMETERS

_name_
> 要生成文档的模块、软件包、类、函数或关键字。名称中的 '/' 会被用作 Python 源文件的路径。

**-k** _KEYWORD_
> 在所有可用模块的概要行中搜索关键字。

**-p** _PORT_
> 在指定端口启动 HTTP 文档服务器。使用端口 0 表示任选未占用的端口。

**-b**
> 启动 HTTP 服务器并打开网页浏览器。

**-w** _name_
> 将 HTML 文档写入当前目录下的文件。

# DESCRIPTION

**pydoc3.4** 是 pydoc 文档工具的 Python 3.4 版本。它显示模块文档、搜索已安装的软件包，并可通过本地 HTTP 服务器提供文档，专门服务于 Python 3.4 解释器及其已安装的库。

这个版本专属的二进制文件存在于安装了多个 Python 版本的系统上。当前开发请使用最新的 **pydoc3**。如果 name 为 'keywords'、'topics' 或 'modules'，则显示这些类别的列表。

# CAVEATS

Python 3.4 已于 2019 年 3 月终止支持。当前开发请使用最新的 **pydoc3**。

# SEE ALSO

[pydoc](/man/pydoc)(1), [pydoc3](/man/pydoc3)(1), [python3.4](/man/python3.4)(1), [python3](/man/python3)(1)

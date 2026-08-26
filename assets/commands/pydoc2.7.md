# TAGLINE

Python 2.7 文档查看器

# TLDR

**查看 Python 2.7 文档**

```pydoc2.7 [module]```

**搜索文档**

```pydoc2.7 -k [keyword]```

**启动文档服务器**

```pydoc2.7 -p [8080]```

# SYNOPSIS

**pydoc2.7** [_options_] [_module_]

# PARAMETERS

_MODULE_
> 要生成文档的模块。

**-k** _KEYWORD_
> 搜索关键字。

**-p** _PORT_
> 启动 HTTP 服务器。

**-w**
> 写入 HTML 文件。

# DESCRIPTION

**pydoc2.7** 是 pydoc 文档工具的 Python 2.7 版本。它显示模块文档、搜索已安装的软件包，并可通过本地 HTTP 服务器提供文档，专门服务于 Python 2.7 解释器及其已安装的库。

这个版本专属的二进制文件存在于安装了多个 Python 版本的系统上。由于 Python 2 已停止维护，进行活跃的 Python 开发时应迁移到 **pydoc3**。

# CAVEATS

Python 2 已弃用。请改用 pydoc3。

# HISTORY

pydoc2.7 是 **Python 2.7** 的文档工具。

# SEE ALSO

[pydoc](/man/pydoc)(1), [pydoc3](/man/pydoc3)(1), [python2.7](/man/python2.7)(1)

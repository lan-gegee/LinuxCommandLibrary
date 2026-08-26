# TAGLINE

查看软件包索引的版本信息

# TLDR

**列出软件包的可用版本**

```pip index versions [package]```

**显示包括预发布版在内的可用版本**

```pip index versions --pre [package]```

**从自定义软件包索引列出版本**

```pip index versions --index-url [https://pypi.example.com/simple] [package]```

**为特定平台列出版本**

```pip index versions --platform [manylinux2014_x86_64] [package]```

# SYNOPSIS

**pip** **index** _command_ [_options_] _package_

# PARAMETERS

**versions** _package_
> 列出软件包的可用版本。

**--pre**
> 包含预发布版和开发版本。

**-i**, **--index-url** _url_
> Python Package Index 的基础 URL（默认：https://pypi.org/simple）。

**--extra-index-url** _url_
> 在 --index-url 之外额外使用的软件包索引 URL。

**--platform** _platform_
> 仅使用与指定平台兼容的 wheel。

**--python-version** _version_
> 用于兼容性检查的 Python 版本（例如 3.11）。

**--implementation** _impl_
> Python 实现（例如 cp 表示 CPython，pp 表示 PyPy）。

**--abi** _abi_
> 仅使用与指定 ABI 标签兼容的 wheel。

**--no-binary** _format_control_
> 不使用二进制软件包。

# DESCRIPTION

**pip index** 用于检查软件包索引信息。显示来自 PyPI 或自定义索引的可用版本。适合在安装前确认有哪些版本可用。

**versions** 子命令列出软件包的所有可用版本，最新版本排在最前。平台和 Python 版本过滤器可将结果限制为兼容的软件包。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-install](/man/pip-install)(1), [pip-show](/man/pip-show)(1), [pip-list](/man/pip-list)(1)

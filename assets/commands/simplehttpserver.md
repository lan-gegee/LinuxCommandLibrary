# TAGLINE

通过 Python HTTP 服务器提供文件服务

# TLDR

在端口 8000 **提供当前目录**的服务

```python3 -m http.server```

在指定端口提供服务

```python3 -m http.server [8080]```

仅**绑定到 localhost**

```python3 -m http.server --bind [127.0.0.1]```

**提供指定目录**的服务（Python 3.7+）

```python3 -m http.server --directory [path/to/dir]```

启用 CGI 脚本执行

```python3 -m http.server --cgi```

Python 2 等价写法（已弃用）

```python -m SimpleHTTPServer [8080]```

# SYNOPSIS

**python3 -m http.server** [**-b** _address_] [**-d** _directory_] [**--cgi**] [**--protocol** _version_] [_port_]

**python -m SimpleHTTPServer** [_port_]

# PARAMETERS

_port_
> 端口号（默认：8000）。

**-b**, **--bind** _ADDRESS_
> 绑定到指定地址（默认：所有接口）。仅限 Python 3。

**-d**, **--directory** _DIR_
> 提供指定目录而不是当前目录（Python 3.7+）。

**--cgi**
> 允许执行 /cgi-bin 下的 CGI 脚本。

**--protocol** _VERSION_
> HTTP 协议版本（默认：HTTP/1.0）。

# DESCRIPTION

**http.server**（Python 3）和 **SimpleHTTPServer**（Python 2）是 Python 标准库模块，用于启动一个基本的 HTTP 服务器来提供静态文件。它们无需安装或配置，非常适合快速文件共享、本地开发和测试。

在 Python 2 中，模块以 **python -m SimpleHTTPServer** 调用；Python 3 将其更名为 **python3 -m http.server**。该服务器可在浏览器中提供目录列表，并处理 GET 和 HEAD 请求。默认绑定所有接口的 8000 端口，但可以自定义端口和绑定地址。

# CAVEATS

不适合生产环境使用。没有身份验证、加密或访问控制。Python 2 和 SimpleHTTPServer 已弃用；请改用 Python 3 的 http.server。**--cgi** 选项自 Python 3.13 起已弃用。

# HISTORY

**SimpleHTTPServer** 自 Python 2 起就是标准库的一部分。Python 3 将其重组为 **http.server**，并增加了绑定地址、目录选择和 CGI 支持等选项。

# INSTALL

```aur: yay -S simplehttpserver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [serve](/man/serve)(1), [http-server](/man/http-server)(1)

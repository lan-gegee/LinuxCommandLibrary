# TAGLINE

在本地网络设备之间共享文件

# TLDR

用一个码**发送**文件

```airshare [mycode] [file.txt]```

使用一个码**接收**文件

```airshare [mycode]```

**发送**多个文件

```airshare [mycode] [file1.txt] [file2.txt]```

直接**发送文本**内容

```airshare [mycode] -t "[Hello, World!]"```

架设**接收（上传）服务器**

```airshare [mycode] -u```

以文本形式**发送剪贴板**内容

```airshare [mycode] -cs```

**指定自定义端口**

```airshare [mycode] [file.txt] -p [9000]```

# SYNOPSIS

**airshare** [_options_] _code_ [_files_]

# DESCRIPTION

**airshare** 是一款基于 Python 的跨平台文件共享工具，用于在同一本地网络上的设备之间传输文件。它使用 mDNS 进行设备发现，并用简单的代码字标识传输会话。接收方只需使用相同的码即可访问共享内容。

该工具为复杂的文件共享方案提供了简单的替代方式，无需配置服务器或创建账户。共享内容也可以通过 Web 浏览器在 `http://<code>.local:8000` 访问。

# PARAMETERS

_CODE_
> 标识共享会话的代码字。

_FILES_
> 要发送的一个或多个文件或目录。

**-p**, **--port** _INTEGER_
> 指定服务器的端口号（默认：8000）。

**-t**, **--text** _TEXT_
> 直接发送文本内容。多个单词需用引号括起。

**-u**, **--upload**
> 架设接收服务器，接受上传的文件。

**-cs**, **--clip-send**
> 以文本形式发送剪贴板内容。

**-cr**, **--clip-receive**
> 接收内容并复制到剪贴板。

**-fp**, **--file-path**
> 发送路径已复制到剪贴板的文件。

**--version**
> 显示版本信息。

# CAVEATS

两台设备必须位于同一本地网络。大文件分块处理，但耗时取决于网络速度。该工具要求网络支持 mDNS。

# HISTORY

**airshare** 作为 AirDrop 的基于 Python 的替代品而开发，用于跨平台本地文件共享，借助 mDNS 实现零配置组网。

# INSTALL

```brew: brew install airshare```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[croc](/man/croc)(1), [wormhole](/man/wormhole)(1), [scp](/man/scp)(1)

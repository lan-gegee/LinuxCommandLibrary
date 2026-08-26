# TAGLINE

使用人类可读口令的安全文件传输工具

# TLDR

**发送文件**

```wormhole send [file]```

**发送目录**（会自动压缩为 zip）

```wormhole send [directory/]```

**发送文本**而不是文件

```wormhole send --text "[message]"```

**用自定义口令发送**

```wormhole send --code [custom-code] [file]```

**接收文件**

```wormhole receive [code]```

**接收并自动确认**

```wormhole receive --accept-file [code]```

**接收并保存到指定输出文件**

```wormhole receive --output-file [filename] [code]```

# SYNOPSIS

**wormhole** _command_ [_options_] [_arguments_]

# PARAMETERS

**send**
> 发送文件、目录或文本消息。

**receive**
> 接收文件或文本消息。

**--text**, **-t**
> 发送文本消息而非文件。

**--code** _code_
> 使用指定的 wormhole 口令而不是自动生成。

**-c**, **--code-length** _n_
> 生成的口令包含的单词数量。

**--verify**
> 要求接收方校验数据校验和。

**--accept-file**
> 自动接受传入的文件（需谨慎使用）。

**--output-file** _file_
> 将接收到的数据保存为指定文件名。

**--relay-url** _url_
> 使用自定义的汇合服务器。

**--hide-progress**
> 传输过程中不显示进度条。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**Magic-Wormhole** 在两台计算机之间提供安全、简单的文件传输。发送方生成一个简短的、人类可读的口令，接收方输入该口令即可建立加密连接。

其安全性基于 SPAKE2+ 口令认证密钥交换，用一个简单的口令即可实现强加密。数据尽可能直接点对点传输；否则通过加密的中继服务器隧道传输。服务器都无法看到未加密的内容。

目录会自动压缩成 zip 进行传输，接收后自动解压。也可以发送文本消息，方便快速分享密码或小段数据。

# CAVEATS

发送方和接收方都必须安装 wormhole。wormhole 口令必须通过安全途径告知对方（最好是口头或可信渠道）。对不可信的发送方使用 **--accept-file** 有风险，因为文件会在未经确认的情况下直接保存。

# HISTORY

Magic-Wormhole 由 **Brian Warner** 创建，于 **2015 年**首次发布。它旨在解决无需复杂配置即可在计算机之间安全传输文件的问题。基于 PAKE 的安全模型让易输入的口令也能实现强加密。此外还有 Go（wormhole-william）和 Rust 的替代实现。

# INSTALL

```apk: sudo apk add wormhole-william```

```brew: brew install wormhole-william```

```nix: nix profile install nixpkgs#wormhole-william```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [rsync](/man/rsync)(1), [croc](/man/croc)(1), [ffsend](/man/ffsend)(1)

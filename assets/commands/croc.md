# TAGLINE

安全文件传输工具

# TLDR

**发送文件**

```croc send [file]```

**发送多个文件**

```croc send [file1] [file2] [file3]```

**发送目录**

```croc send [directory/]```

**接收文件**

```croc [code-phrase]```

**使用自定义代码发送**

```croc send --code [my-secret-code] [file]```

**使用自定义中继服务器**

```croc --relay [relay.example.com:9009] send [file]```

**运行中继服务器**

```croc relay```

# SYNOPSIS

**croc** [_options_] send [_send_options_] _file_
**croc** [_options_] _code-phrase_

# DESCRIPTION

**croc** 是一款在计算机之间安全传输文件的工具。它借助中继服务器和 PAKE（口令认证密钥交换）实现端到端加密，确保所传输的文件不会被中继服务器读取，也不会在网络上被截获。

该工具可以跨不同网络工作，无需端口转发或防火墙配置。用户共享一个简短的代码短语，双方连接到中继服务器，文件便通过加密通道完成传输。在局域网内传输时，若条件允许会自动改用直连以获得更快的速度。

其特性包括可断点续传（传输中断后能从中断处继续）、支持一次发送多个文件和整个目录、跨平台兼容（Linux、macOS、Windows），以及可自行架设中继服务器以获得完全控制权。

# COMMANDS

**send**
> 发送文件或文件夹

**relay**
> 运行中继服务器

# PARAMETERS

**--code** _phrase_
> 使用自定义代码短语

**--relay** _address_
> 指定中继服务器

**--yes**
> 不经提示直接接受传输

**--out** _path_
> 接收文件的输出目录

**--overwrite**
> 覆盖已有文件

**--curve** _type_
> 加密曲线（p256、p384、p521、siec）

**--hash** _algorithm_
> 哈希算法（xxhash、imohash、md5）

**--no-compress**
> 禁用压缩

**--no-local**
> 禁用本地网络传输

**--ports** _range_
> 本地传输使用的端口范围

# ENVIRONMENT

**CROC_RELAY**
> 默认中继服务器

**CROC_PASS**
> 默认代码短语

# HOW IT WORKS

1. 发送方生成代码短语
2. 双方连接到中继服务器
3. PAKE 建立加密通道
4. 文件经由中继传输（或在局域网内直接传输）

# CAVEATS

默认的中继服务器是公开的（croc.schollz.com）。传输敏感内容时请自行架设中继。代码短语应通过安全渠道分享。

# INSTALL

```pacman: sudo pacman -S croc```

```apk: sudo apk add croc```

```brew: brew install croc```

```nix: nix profile install nixpkgs#croc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [scp](/man/scp)(1)

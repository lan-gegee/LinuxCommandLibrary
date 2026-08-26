# TAGLINE

音频合成编程语言解释器

# TLDR

**启动 SuperCollider 解释器**

```sclang```

**运行 SuperCollider 脚本**

```sclang [script.scd]```

**以守护进程模式启动**（无输入）

```sclang -D```

**启动时运行 Main.run**

```sclang -r [script.scd]```

**设置初始堆大小**

```sclang -m [8m]```

**设置 UDP 监听端口**

```sclang -u [57120]```

**设置运行时目录**

```sclang -d [/path/to/runtime]```

# SYNOPSIS

**sclang** [_options_] [_file_]

# PARAMETERS

**-d** _path_
> 设置运行时目录。

**-D**
> 进入守护进程模式（无用户输入）。

**-g** _size_
> 设置堆增长大小（默认 256k）。可加 k 或 m 后缀。

**-h**
> 显示帮助信息。

**-l** _path_
> 设置库配置文件。

**-m** _size_
> 设置初始堆大小（默认 2m）。可加 k 或 m 后缀。

**-r**
> 启动时调用 Main.run。

**-s**
> 关闭时调用 Main.stop。

**-u** _port_
> 设置 UDP 监听端口（默认 57120）。

# DESCRIPTION

**sclang** 是 SuperCollider 编程语言的解释器。SuperCollider 是一个音频合成与算法作曲平台，被音乐人、艺术家和研究人员用于实时音频处理和声音设计。

该解释器充当 **scsynth**（SuperCollider 音频合成服务器）的客户端。它解释 SuperCollider 代码并向合成服务器发送 OSC（Open Sound Control）消息来控制音频生成。

SuperCollider 脚本（.scd 文件）可以直接从命令行执行，用于无头音频处理或批处理操作。守护进程模式允许在没有终端的情况下运行 SuperCollider，适合服务器部署。

在 Linux 上，通过设置环境变量 QT_QPA_PLATFORM=offscreen，sclang 可以在没有显示服务器的情况下运行。

# CAVEATS

音频合成需要 scsynth 音频服务器。SuperCollider IDE 提供更集成的开发体验。从命令行运行时，脚本文件必须组织为单个可执行块。处理复杂作品时可能需要调整内存设置。

# HISTORY

**SuperCollider** 由 James McCartney 于 1996 年开始开发。它最初是 Macintosh 上的专有软件，2002 年以 GPL 许可证作为自由软件发布。该语言已成为计算机音乐社区的标准工具，被用于现场编码表演和学术研究。

# INSTALL

```pacman: sudo pacman -S supercollider```

```zypper: sudo zypper install supercollider```

```nix: nix profile install nixpkgs#supercollider```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[csound](/man/csound)(1)

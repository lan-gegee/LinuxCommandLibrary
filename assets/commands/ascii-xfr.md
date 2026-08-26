# TAGLINE

通过串行连接进行 ASCII 文件传输

# TLDR

通过串行线路**发送**文件

```ascii-xfr -s [path/to/file]```

从串行线路**接收**文件

```ascii-xfr -r [path/to/file]```

以 **100 毫秒的行间延迟****发送**文件

```ascii-xfr -s -l 100 [path/to/file]```

以 **10 毫秒的字符间延迟****发送**文件

```ascii-xfr -s -c 10 [path/to/file]```

**发送**文件并在完成时传输一个**文件结束（EOF）**字符

```ascii-xfr -s -e [path/to/file]```

以**详细输出**模式**接收**文件

```ascii-xfr -r -v [path/to/file]```

# SYNOPSIS

**ascii-xfr** **-s**|**-r** [**-ednv**] [**-l** _linedelay_] [**-c** _characterdelay_] _filename_

# PARAMETERS

**-s**
> 发送文件

**-r**
> 接收文件

**-e**
> 上传完成后发送文件结束（EOF）字符（Control-Z）

**-d**
> 使用 Control-D 而不是 Control-Z 作为 EOF 字符

**-n**
> 不转换 CR/LF；跳过自动 CRLF 转换

**-v**
> 详细模式；在 stderr 上显示传输统计信息

**-l** _milliseconds_
> 行延迟；发送时每行之后等待指定的毫秒数

**-c** _milliseconds_
> 字符延迟；发送时每个字符之后等待指定的毫秒数

# DESCRIPTION

**ascii-xfr** 是一个文件传输工具，它使用纯 ASCII 的逐行传输方式在串行连接上收发文件。它是 **minicom** 软件包的一部分，被设计为远程系统不支持 ZMODEM、XMODEM 或 Kermit 等正规文件传输协议时的最后手段。

发送时，行尾字符以 **CRLF** 形式传输。接收时，传入数据中的 **CR** 字符会被剔除。该工具接收时从 stdin 读取，发送时写入 stdout，因此需要将 I/O 重定向到串行设备，这通常由 minicom 或类似的终端模拟器提供。

# CAVEATS

没有任何错误检测或纠正机制。传输过程中的数据损坏无法察觉，因此不适合二进制文件或不可靠的链路。该工具专为文本文件传输设计；除非使用 **-n**，否则 CRLF 转换会破坏二进制文件。man page 本身就建议：只有当远程系统不支持其他任何方案时才使用它。

# HISTORY

**ascii-xfr** 由 **minicom** 的作者 **Miquel van Smoorenburg** 和 **Jukka Lahtinen** 编写。Minicom 起源于 1990 年代初，作为 DOS 程序 Telix 的自由文本界面替代品出现，后来成为 Linux 上事实上的标准串行终端模拟器。ascii-xfr 则是为其最简陋的文件传输场景而编写的配套工具。

# INSTALL

```apt: sudo apt install minicom```

```dnf: sudo dnf install minicom```

```pacman: sudo pacman -S minicom```

```apk: sudo apk add minicom```

```zypper: sudo zypper install minicom```

```brew: brew install minicom```

```nix: nix profile install nixpkgs#minicom```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[minicom](/man/minicom)(1)

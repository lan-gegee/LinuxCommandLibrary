# TAGLINE

面向二进制格式的 jq

# TLDR

**查看**二进制文件

```fq . [file]```

按指定格式**解码**

```fq -d [mp4|flac|jpeg|...] . [file]```

**查询**特定字段

```fq '.tracks[0].duration' [file]```

**打开**交互式 REPL

```fq -i [file]```

# SYNOPSIS

**fq** [_options_] [_query_] [_file_]

# PARAMETERS

**-d, --decode** _FORMAT_
> 按指定格式解码。

**-i, --interactive**
> 启动交互式 REPL。

**-n, --null-input**
> 使用 null 作为输入值。

**-r, --raw-output**
> 输出原始字符串。

**-c, --compact-output**
> 紧凑输出（不进行格式化打印）。

**--help**
> 显示帮助并退出。

**--version**
> 显示版本并退出。

# DESCRIPTION

**fq** 是一个使用类 jq 查询语言检查二进制文件的工具。它可以解码并查询 100 多种二进制格式，包括 MP4、FLAC、JPEG、PCAP、ELF 等。

该工具提供带自动补全的 REPL，支持以交互方式探索二进制结构。它适用于调试、逆向工程以及理解文件格式。

# USAGE

基本查看：

```fq . file.mp4```

查询特定字段：

```fq '.meta.moov.tracks[0].mdia.minf.stbl.sample_descriptions[0].width' video.mp4```

按原始字节解码：

```fq -d raw '.[0:10]' file```

列出支持的格式：

```fq -h```

# CAVEATS

大文件可能消耗大量内存。部分格式的支持尚不完整。输出二进制数据可能需要编码支持良好的终端。复杂的嵌套查询可能较慢。

# HISTORY

**fq** 由 **Mattias Wadman** 创建，于 **2021** 年首次发布，将 jq 的强大能力带入二进制数据领域，让检查和理解二进制文件格式不再需要专门的工具。

# INSTALL

```apt: sudo apt install fq```

```pacman: sudo pacman -S fq```

```zypper: sudo zypper install fq```

```brew: brew install fq```

```nix: nix profile install nixpkgs#fq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [xxd](/man/xxd)(1), [hexdump](/man/hexdump)(1), [binwalk](/man/binwalk)(1)

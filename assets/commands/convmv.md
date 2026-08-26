# TAGLINE

文件名编码转换工具

# TLDR

**预览文件名转换**：从 Latin1 到 UTF-8

```convmv -f latin1 -t utf-8 [path/to/files/*]```

**真正执行文件名转换**（应用更改）

```convmv -f latin1 -t utf-8 --notest [path/to/files/*]```

**递归转换文件名**（作用于整个目录）

```convmv -f latin1 -t utf-8 -r --notest [path/to/directory]```

**从 Windows 编码转换**为 UTF-8

```convmv -f cp1252 -t utf-8 --notest [path/to/files/*]```

**将所有文件名转为小写**

```convmv --lower --notest [path/to/files/*]```

**修复双重编码的 UTF-8** 文件名

```convmv --fixdouble -f utf-8 -t utf-8 --notest [path/to/files/*]```

# SYNOPSIS

**convmv** [_options_] _file_...

# PARAMETERS

**-f** _ENCODING_
> 源编码（from encoding）。

**-t** _ENCODING_
> 目标编码（to encoding）。

**-r**
> 递归处理子目录。

**--notest**
> 真正执行转换（默认仅试运行）。

**--nfc**
> 规范化为 Unicode NFC 形式。

**--nfd**
> 规范化为 Unicode NFD 形式。

**--lower**
> 将文件名转换为小写。

**--upper**
> 将文件名转换为大写。

**--fixdouble**
> 修复双重编码的 UTF-8 文件名。

**--list**
> 列出可用的编码。

**--preserve-mtimes**
> 保留目录的修改时间。

# DESCRIPTION

**convmv** 是一个在不同字符编码之间转换文件名的实用工具。当在一个系统上以特定 locale 创建的文件需要用到另一个使用不同字符编码的系统时，它必不可少。

常见用例包括把文件从 Windows（使用 cp1252 或 ISO-8859-1）迁移到使用 UTF-8 的 Linux，或者修复因错误编码假设而创建的文件名。该工具还能修复双重编码的 UTF-8，这种情况是 UTF-8 字节被错误地再次按 UTF-8 编码导致的。

默认情况下，convmv 会执行一次试运行，显示将要发生的更改。必须显式提供 **--notest** 标志才会真正重命名文件。这一安全机制可以防止意外的大批量重命名操作。

# CAVEATS

请始终先不带 **--notest** 运行以预览更改。该工具无法自动检测源编码；你必须知道原始使用的编码。转换为表达能力较弱的编码可能造成数据丢失。符号链接和硬链接需要谨慎处理。

# HISTORY

convmv 由 Björn Jacke 编写，长期以来都是 Unix 系统上处理编码问题的标准工具。在 2000 年代从各 locale 专用编码向通用标准 UTF-8 过渡期间，它尤为重要。

# INSTALL

```dnf: sudo dnf install convmv```

```pacman: sudo pacman -S convmv```

```zypper: sudo zypper install convmv```

```brew: brew install convmv```

```nix: nix profile install nixpkgs#convmv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mv](/man/mv)(1), [rename](/man/rename)(1), [iconv](/man/iconv)(1), [recode](/man/recode)(1)

# RESOURCES

```[Homepage](https://www.j3e.de/linux/convmv/)```

<!-- verified: 2026-06-23 -->

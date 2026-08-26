# TAGLINE

列出归档文件的内容

# TLDR

**列出归档内容**

```lsar [archive.zip]```

**列出详细信息**

```lsar -l [archive.rar]```

**以超长格式列出**

```lsar -L [archive.7z]```

**测试归档完整性**

```lsar -t [archive.zip]```

**带密码列出**

```lsar -p [password] [encrypted.zip]```

**指定编码列出**

```lsar -e [shift_jis] [japanese.zip]```

**仅打印文件名**

```lsar -1 [archive.tar.gz]```

# SYNOPSIS

**lsar** [_-l_] [_-L_] [_-t_] [_-p password_] [_-e encoding_] [_archive_]

# PARAMETERS

**-l**
> 长列表，包含大小、日期、权限。

**-L**
> 超长列表，包含更多细节。

**-t**
> 测试归档完整性。

**-p** _PASSWORD_
> 为加密归档指定密码。

**-e** _ENCODING_
> 强制指定文件名的字符编码。

**-1**
> 仅打印文件名，每行一个。

**-j**
> 以 JSON 输出。

**-q**
> 安静模式。

**-nr**
> 不递归进入嵌套归档。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**lsar** 列出归档文件的内容。它支持多种格式，包括 Zip、RAR、7-Zip、tar、gzip、bzip2、ISO 以及许多旧式格式。

该工具属于 The Unarchiver 套件。unar 用于解压文件，而 lsar 提供不解压即可检查的能力。它能处理标准工具可能失败的情况，包括损坏或非标准的归档。

编码检测会自动处理国际化文件名。对编码标注错误的归档，可用 -e 标志强制指定字符集，如 Shift_JIS、GBK 或 EUC-KR。

长列表会显示文件大小（压缩前后）、修改日期以及可获得的权限信息。测试模式（-t）在不解压的情况下验证归档完整性。

JSON 输出便于脚本处理和与其他工具集成。

# CAVEATS

大多数系统默认不安装——需要 The Unarchiver 软件包。某些格式的元数据支持有限。加密的 RAR5 归档需要特定的构建版本。

# HISTORY

**lsar** 属于 **The Unarchiver** 项目，由 **Dag Ågren** 自 **2006 年**前后开始创建。它最初是 macOS 应用程序，命令行工具为后来添加。该项目专注于兼容多种归档格式并正确处理国际化文件名。

# INSTALL

```apt: sudo apt install unar```

```dnf: sudo dnf install unar```

```zypper: sudo zypper install unar```

```brew: brew install unar```

```nix: nix profile install nixpkgs#unar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unar](/man/unar)(1), [unzip](/man/unzip)(1), [tar](/man/tar)(1), [7z](/man/7z)(1), [unrar](/man/unrar)(1)

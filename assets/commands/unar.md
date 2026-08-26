# TAGLINE

通用多格式归档解压器

# TLDR

**解压归档文件**

```unar [archive.zip]```

**解压到目录**

```unar -o [output_dir] [archive.rar]```

**使用密码解压**

```unar -p [password] [encrypted.zip]```

**强制覆盖**

```unar -f [archive.zip]```

**不创建目录直接解压**

```unar -D [archive.tar.gz]```

**仅列出内容**

```lsar [archive.7z]```

**以指定编码解压**

```unar -e [shift_jis] [japanese.zip]```

# SYNOPSIS

**unar** [_-o dir_] [_-p password_] [_-e encoding_] [_options_] _archive_

# PARAMETERS

**-o** _DIR_
> 输出目录。

**-p** _PASSWORD_
> 归档密码。

**-e** _ENCODING_
> 文件名编码。

**-f**, **--force**
> 不询问直接覆盖。

**-D**, **--no-directory**
> 不创建包含目录。

**-d**, **--directory**
> 总是创建目录。

**-k** _MODE_
> 如何处理已存在的文件。

**-q**, **--quiet**
> 安静模式。

**-t**, **--test**
> 测试归档文件。

**-nr**, **--no-recursion**
> 不解压嵌套的归档文件。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**unar** 可解压多种格式的归档文件。它支持 Zip、RAR、7-Zip、tar、gzip、bzip2、ISO 以及许多传统格式。

格式检测是自动进行的。该工具会检查归档内容，而不是仅仅依赖扩展名。

编码处理能正确处理国际化文件名。日语、中文、韩语等编码均受支持并可自动检测。

密码处理适用于加密归档。同时支持头部加密和内容加密两种格式。

该工具可以处理其他解压器拒绝的损坏或非标准归档。它会尽力恢复其中的内容。

默认情况下，归档会解压到以归档文件命名的目录中。可以使用 -d 或 -D 选项控制此行为。

# CAVEATS

并非默认安装。某些格式的元数据支持有限。非常古老的格式可能存在特殊问题。

# HISTORY

**unar** 是 **The Unarchiver** 的一部分，由 **Dag Ågren** 从 **2006 年**前后开始开发。最初是一个 macOS 图形界面应用，后来为满足脚本需求添加了命令行工具。

# INSTALL

```apt: sudo apt install unar```

```dnf: sudo dnf install unar```

```zypper: sudo zypper install unar```

```brew: brew install unar```

```nix: nix profile install nixpkgs#unar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsar](/man/lsar)(1), [unzip](/man/unzip)(1), [unrar](/man/unrar)(1), [7z](/man/7z)(1), [tar](/man/tar)(1)

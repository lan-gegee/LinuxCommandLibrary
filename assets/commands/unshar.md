# TAGLINE

从 shell 归档中提取文件

# TLDR

**解压 shell 归档**

```unshar [archive.shar]```

**解压到指定目录**

```unshar -d [/path/to/directory] [archive.shar]```

**覆盖已有文件**

```unshar -c [archive.shar]```

**从压缩归档中提取**

```gzip -dc [archive.shar.gz] | unshar```

**从一个文件中提取多个归档**

```unshar -e [combined.shar]```

**从邮件正文中提取**

```unshar [message.txt]```

# SYNOPSIS

**unshar** [_options_] [_file_...]

# PARAMETERS

**-d**, **--directory** _dir_
> 解压前切换到指定目录。

**-c**, **--overwrite**
> 将 -c 传递给 shar 脚本以覆盖已存在的文件。

**-e**, **--exit-0**
> 在 "exit 0" 行处分隔归档。

**-E**, **--split-at** _string_
> 在指定字符串处分割归档。

**-f**, **--force**
> 强制覆盖，不进行提示。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**unshar** 从 shell 归档（shar 文件）中提取文件。它会扫描输入内容以查找 shell 归档头，然后通过 shell 执行每个归档来提取其中的内容。

Shell 归档是一种自解压脚本，其中包含被编码为 shell 命令的文件。在现代归档格式成为标准之前，它曾被广泛用于通过电子邮件分发源代码。

处理邮件消息时，unshar 会自动定位并提取内嵌的 shell 归档，同时忽略邮件头和签名。多个归档可以拼接在一起，并用 -e 选项一并提取。

# CAVEATS

会执行来自归档的 shell 代码，处理不可信文件存在安全风险。解压前务必核实归档的来源和内容。某些归档可能依赖特定的 shell 特性。属于 sharutils 软件包的一部分。

# HISTORY

**unshar** 与 shell 归档的历史可以追溯到早期 Unix 时代，当时电子邮件是共享软件的主要方式。shar 格式允许将二进制文件和文本文件编码成能够经受邮件传输的形式。虽然在很大程度上已被 tar 和 zip 取代，但 shar 归档仍出现在遗留代码分发和邮件列表存档中。

# INSTALL

```apt: sudo apt install sharutils```

```dnf: sudo dnf install sharutils```

```pacman: sudo pacman -S sharutils```

```apk: sudo apk add sharutils```

```zypper: sudo zypper install sharutils```

```nix: nix profile install nixpkgs#sharutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shar](/man/shar)(1), [tar](/man/tar)(1), [unzip](/man/unzip)(1), [uudecode](/man/uudecode)(1)

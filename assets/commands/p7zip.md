# TAGLINE

7-Zip 的 Unix 移植版，提供高压缩比

# TLDR

**解压归档**

```7z x [archive.7z]```

**解压到指定目录**

```7z x [archive.7z] -o[/path/to/output]```

**创建 7z 归档**

```7z a [archive.7z] [files_or_dirs]```

**以最大压缩率创建归档**

```7z a -mx=9 [archive.7z] [files]```

**列出归档内容**

```7z l [archive.7z]```

**测试归档完整性**

```7z t [archive.7z]```

**添加密码加密**

```7z a -p[password] [archive.7z] [files]```

**创建加密归档**（包括文件名）

```7z a -p[password] -mhe=on [archive.7z] [files]```

# SYNOPSIS

**7z** _command_ [_-mhe_] [_-mx=level_] [_-p[password]_] [_-o[dir]_] [_options_] _archive_ [_files_]

# PARAMETERS

**a**
> 将文件添加到归档。

**x**
> 以完整路径解压。

**e**
> 解压到当前目录。

**l**
> 列出归档内容。

**t**
> 测试归档完整性。

**d**
> 从归档中删除。

**u**
> 更新归档中的文件。

**-mx=** _LEVEL_
> 压缩级别（0=仅存储、1=最快、5=常规、7=最大、9=极限）。

**-p**_PASSWORD_
> 设置密码（开关与值之间不加空格；若省略则交互式询问）。

**-mhe=on**
> 加密文件头，使归档内的文件名也被隐藏。

**-o**_DIR_
> `x`/`e` 的输出目录（`-o` 与路径之间不加空格）。

**-r**
> 递归处理子目录。

**-y**
> 对所有提示自动回答"是"。

**-t** _TYPE_
> 归档类型：7z、zip、tar、gzip、bzip2。

**-v** _SIZE_
> 创建指定大小的分卷。

**-m0=** _METHOD_
> 压缩方法：lzma、lzma2、bzip2、ppmd。

**-ms=on**
> 启用固实归档模式。

# DESCRIPTION

**p7zip** 是 7-Zip 的 Unix 移植版，提供高压缩比。借助 LZMA/LZMA2 算法，7z 格式的压缩率通常比 ZIP 高 30-70%。

该软件包提供三个命令：**7z**（功能完整）、**7za**（独立版）和 **7zr**（精简版，仅支持 7z 格式）。大多数用户使用 7z 或 7za。

支持的归档格式包括：7z、ZIP、GZIP、BZIP2、XZ、TAR，以及从许多其他格式（RAR、CAB、ISO、DMG 等）解压。-t 选项可覆盖自动格式检测。

固实归档（-ms=on）将多个文件作为一个整体块进行压缩，在归档大量相似文件时能提高压缩率。但这也意味着提取其中一个文件时，需要先解压其前面的所有文件。

加密采用 AES-256。-mhe 选项在加密内容之外还加密文件名，从而隐藏归档内的内容。密码可以在命令行提供（会在进程列表中可见），也可以交互式输入。

# CAVEATS

7z 格式默认不保存 Unix 权限、所有者或符号链接——如需保留时间戳请使用 `-mtc=on -mta=on -mtm=on`；当 POSIX 元数据很重要时，建议改用 **tar**（或 `tar | 7z`）。RAR 支持仅限于解压。在命令行提供的密码会出现在 `/proc/<pid>/cmdline` 中。固实归档（`.7z` 的默认方式）使单个文件的提取开销与前序全部数据量成正比。最初的 p7zip 项目自 2016 年起已无人维护；许多发行版现在改为附带 Igor Pavlov 官方的 **7-Zip** Linux 版本（`7zz` 二进制文件）。

# HISTORY

**7-Zip** 由 **Igor Pavlov** 于 **1999** 年为 Windows 开发。**p7zip** 是 Myspace 于 **2004** 年开始的 POSIX 移植版。自 2021 年起，Pavlov 发布官方的 Linux/macOS 二进制程序（`7zz`），使 p7zip 基本被取代。

# INSTALL

```apt: sudo apt install 7zip```

```dnf: sudo dnf install 7zip```

```pacman: sudo pacman -S 7zip```

```zypper: sudo zypper install 7zip```

```brew: brew install 7zip```

```nix: nix profile install nixpkgs#p7zip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zip](/man/zip)(1), [unzip](/man/unzip)(1), [gzip](/man/gzip)(1), [xz](/man/xz)(1), [tar](/man/tar)(1)

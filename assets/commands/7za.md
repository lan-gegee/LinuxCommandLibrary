# TAGLINE

7-Zip 家族中的独立版文件归档工具

# TLDR

**创建归档**

```7za a [archive.7z] [files...]```

**解压归档**

```7za x [archive.7z]```

**列出归档内容**

```7za l [archive.7z]```

**创建 zip 归档**

```7za a -tzip [archive.zip] [files]```

带密码解压

```7za x -p[password] [archive.7z]```

# SYNOPSIS

**7za** _command_ [_switches_] _archive_ [_files_...]

# COMMANDS

**a**
> 向归档添加文件

**x**
> 按完整路径解压

**e**
> 解压（扁平化，不带路径）

**l**
> 列出归档内容

**t**
> 测试归档完整性

**d**
> 从归档中删除

**u**
> 更新归档

# PARAMETERS

**-o**_dir_
> 输出目录

**-p**_password_
> 设置密码

**-mx=**_n_
> 压缩级别（0-9）

**-t**_type_
> 归档类型（7z、zip、gzip、bzip2、xz、tar）

**-r**
> 递归处理子目录

**-y**
> 询问时自动回答 yes

**-si**
> 从标准输入读取

**-so**
> 写到标准输出

**-mhe=on**
> 加密归档头（7z 格式）

# DESCRIPTION

**7za** 是 7-Zip 命令行工具的独立版本。与可能调用外部插件的 **7z** 不同，7za 将所有编解码器包含在单个可执行文件中。

7za 支持的格式少于完整的 7z，但作为单一二进制文件更具可移植性。它可处理 7z、ZIP、GZIP、BZIP2、XZ、TAR 和 CAB 格式。

其命令语法与 **7z** 完全相同。对于只需要常见格式的脚本，7za 因简单可靠而常被优先选用。

# CAVEATS

7za 支持的格式少于 7z。要解压 RAR、CAB 或 ISO，请使用完整的 7z 命令。

7za 中的 "a" 代表 "alone"（独立），而不是 "alpha" 或 "advanced"。

对所支持的格式而言，性能与 7z 相同。

# INSTALL

```apt: sudo apt install 7zip```

```dnf: sudo dnf install 7zip```

```pacman: sudo pacman -S 7zip```

```zypper: sudo zypper install 7zip```

```brew: brew install 7zip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[7z](/man/7z)(1), [7zr](/man/7zr)(1), [tar](/man/tar)(1), [gzip](/man/gzip)(1)

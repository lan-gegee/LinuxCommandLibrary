# TAGLINE

仅支持 7z 格式的精简版文件归档工具

# TLDR

**创建 7z 归档**

```7zr a [archive.7z] [files...]```

**解压 7z 归档**

```7zr x [archive.7z]```

**列出归档内容**

```7zr l [archive.7z]```

**测试归档完整性**

```7zr t [archive.7z]```

以最大压缩率创建

```7zr a -mx=9 [archive.7z] [files]```

# SYNOPSIS

**7zr** _command_ [_switches_] _archive_ [_files_...]

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

**-mx=**_n_
> 压缩级别（0-9）

**-r**
> 递归处理子目录

**-y**
> 询问时自动回答 yes

# DESCRIPTION

**7zr** 是 7-Zip 命令行工具的最小化精简版本，仅支持 7z 格式。它是 7-Zip 家族中最轻量的选择。

当只需要 7z 格式、希望依赖最少，或要在脚本及有体积限制的系统中内嵌时，7zr 是理想选择。

其命令语法与 7z 和 7za 一致。对于仅涉及 7z 的操作，7zr 占用的资源最小。

# CAVEATS

7zr 只能处理 7z 格式。它无法处理 ZIP、TAR、GZIP 或任何其他格式。

部分构建版本不支持加密。

"r" 代表 "reduced"（精简）——指支持的格式少，并非递归之意。

# INSTALL

```apt: sudo apt install 7zip```

```dnf: sudo dnf install 7zip```

```pacman: sudo pacman -S 7zip```

```zypper: sudo zypper install 7zip```

```brew: brew install 7zip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[7z](/man/7z)(1), [7za](/man/7za)(1), [tar](/man/tar)(1)

# RESOURCES

```[Source code](https://github.com/ip7z/7zip)```

```[Homepage](https://www.7-zip.org/)```

<!-- verified: 2026-06-10 -->

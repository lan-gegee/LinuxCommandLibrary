# TAGLINE

压缩可执行文件的同时保持其可执行性

# TLDR

**原地压缩**可执行文件

```gzexe [path/to/executable]```

**将**压缩过的可执行文件**解压**回二进制文件

```gzexe -d [path/to/compressed_executable]```

# SYNOPSIS

**gzexe** [_-d_] _file_...

# PARAMETERS

**-d**
> 解压可执行文件（将 shell 脚本还原为二进制文件）

# DESCRIPTION

**gzexe** 在压缩可执行文件的同时保持其可执行性。它会创建一个自解压的 shell 脚本，该脚本把原始二进制文件解压到临时位置、执行它，然后清理现场。

原始文件会附加 **~** 后缀作为备份保留。生成的"可执行文件"实际上是一个包含压缩二进制数据的 shell 脚本。

这适用于在存储空间有限的系统上节省磁盘空间，尤其适合不常使用的大型二进制文件。代价是解压导致启动时间增加。

# CAVEATS

由于需要解压，压缩后的可执行文件启动较慢。shell 脚本包装器未必适用于所有类型的二进制文件（尤其是检查自身路径的程序）。setuid/setgid 位不会被保留。与进程名显示等依赖二进制特性的功能不兼容。

# HISTORY

gzexe 是 gzip 软件包的一部分，自 20 世纪 90 年代初起就已可用。它的诞生是为了在存储昂贵的年代为 Unix 系统节省磁盘空间，提供了一种在不改变调用方式的前提下压缩二进制文件的简单方法。

# INSTALL

```apt: sudo apt install gzip```

```dnf: sudo dnf install gzip```

```pacman: sudo pacman -S gzip```

```apk: sudo apk add gzip```

```zypper: sudo zypper install gzip```

```brew: brew install gzip```

```nix: nix profile install nixpkgs#gzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [upx](/man/upx)(1), [strip](/man/strip)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/gzip/)```

```[Source code](https://git.savannah.gnu.org/cgit/gzip.git)```

<!-- verified: 2026-07-17 -->

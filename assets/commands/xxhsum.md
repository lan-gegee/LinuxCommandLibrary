# TAGLINE

打印或校验 xxHash 非加密校验和

# TLDR

计算 **XXH64 校验和**（默认）

```xxhsum [path/to/file]```

计算 **XXH32 校验和**

```xxhsum -H0 [path/to/file]```

计算 **XXH128 校验和**

```xxhsum -H2 [path/to/file]```

从文件**校验校验和**

```xxhsum -c [path/to/checksums.xxh]```

运行**基准测试**

```xxhsum -b```

# SYNOPSIS

**xxhsum** [_OPTION_]... [_FILE_...]

**xxhsum -b** [_OPTION_]...

# PARAMETERS

**-H** _HASHTYPE_
> 哈希算法：0（XXH32）、1（XXH64，默认）、2（XXH128）、3（XXH3）。也接受 32、64、128 作为别名。

**-b**
> 启用基准测试模式

**-B** _BLOCKSIZE_
> 设置基准测试块大小（字节）（默认：102400）

**-i** _ITERATIONS_
> 设置基准测试迭代次数（默认：3）

**-c, --check** _FILE_
> 从文件校验校验和

**-q, --quiet**
> 校验时抑制 OK 消息

**-w, --warn**
> 对格式错误的校验和行发出警告

**--strict**
> 遇到无效校验和行时返回错误

**--status**
> 静默校验；仅通过退出码指示结果

**--tag**
> 以 BSD 风格格式输出

**--little-endian**
> 以小端序格式显示校验和（默认为大端序）

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# DESCRIPTION

**xxhsum** 打印或校验 xxHash（32、64 或 128 位）校验和。xxHash 是一种极快的非加密哈希函数，适合在对速度要求高的完整性检查场景中使用。

未指定 FILE 时从标准输入读取。命令行语法类似于 md5sum(1)。

等效的快捷命令：**xxh32sum**（同 xxhsum -H0）、**xxh64sum**（同 xxhsum -H1）、**xxh128sum**（同 xxhsum -H2）。

# CAVEATS

不具备加密安全性。不应用于安全敏感场景。安全用途请使用 SHA-256 等。

# INSTALL

```apt: sudo apt install xxhash```

```dnf: sudo dnf install xxhash```

```pacman: sudo pacman -S xxhash```

```apk: sudo apk add xxhash```

```zypper: sudo zypper install xxhash```

```brew: brew install xxhash```

```nix: nix profile install nixpkgs#xxhash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1), [b2sum](/man/b2sum)(1), [cksum](/man/cksum)(1)

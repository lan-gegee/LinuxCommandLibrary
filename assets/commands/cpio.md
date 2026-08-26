# TAGLINE

支持从 stdin 读取文件列表的归档工具

# TLDR

**创建**归档

```find . -depth | cpio -o > [archive.cpio]```

**解压**归档

```cpio -i < [archive.cpio]```

**列出**归档内容

```cpio -t < [archive.cpio]```

**复制**文件

```find . | cpio -pd [/destination]```

# SYNOPSIS

**cpio** [_options_]

# DESCRIPTION

**cpio**（copy in/out）是一个归档工具，它从 stdin 读取文件列表并创建或提取归档。它常用于 initramfs 镜像、RPM 软件包，以及复制目录树。

该工具有三种工作模式：copy-out（创建归档）、copy-in（提取归档）和 pass-through（不经过归档直接复制文件）。与直接接受文件参数的 tar 不同，cpio 从标准输入读取文件名，通常由 find 通过管道提供。这种设计可以借助 find 强大的过滤能力，更灵活地选取文件。

由于简单且受内核支持，cpio 是 Linux 初始 ramdisk 镜像的首选格式。RPM 软件包内部也使用 cpio 存储文件。该格式支持多种归档类型，并能保留权限、所有者和时间戳等文件元数据。

# PARAMETERS

**-o**, **--create**
> 创建归档（copy-out 模式）

**-i**, **--extract**
> 提取归档（copy-in 模式）

**-p**, **--pass-through**
> 复制文件（pass-through 模式）

**-t**, **--list**
> 列出归档内容

**-v**, **--verbose**
> 详细模式

**-d**, **--make-directories**
> 按需创建目录

**-u**, **--unconditional**
> 无条件覆盖文件

**-m**, **--preserve-modification-time**
> 保留修改时间

# MODES

**Copy-out (-o):**
> 从文件列表创建归档

**Copy-in (-i):**
> 从归档中提取

**Pass-through (-p):**
> 不经归档直接复制文件

# WORKFLOW

```bash
# Create archive
find . -name "*.txt" | cpio -o > textfiles.cpio

# Create with verbose output
find . | cpio -ov > backup.cpio

# Extract archive
cpio -i < archive.cpio

# Extract with verbose
cpio -idv < archive.cpio

# List contents
cpio -t < archive.cpio

# Copy directory tree (like cp -r but preserves more)
find /source | cpio -pdm /destination

# Extract specific files
cpio -i "*.conf" < archive.cpio
```

# COMPRESSION

```bash
# Create compressed archive
find . | cpio -o | gzip > archive.cpio.gz

# Extract compressed archive
gunzip < archive.cpio.gz | cpio -i

# With bzip2
find . | cpio -o | bzip2 > archive.cpio.bz2
zcat archive.cpio.bz2 | cpio -i
```

# COMMON USES

**Initramfs extraction:**
```bash
mkdir initramfs
cd initramfs
gunzip -c /boot/initramfs.img | cpio -i
```

**RPM content extraction:**
```bash
rpm2cpio package.rpm | cpio -idmv
```

# CAVEATS

不如 tar 直观。需要从 stdin 提供文件列表。没有内置压缩。路径名长度有限制。GNU 与 POSIX 版本行为不同。使用范围不如 tar 广泛。

# HISTORY

**cpio** 于 **1977** 年被收入 Unix PWB/UNIX，后来成为 POSIX 的一部分。它比 tar 出现得更早，并提供更灵活的文件选择方式。

# INSTALL

```apt: sudo apt install cpio```

```dnf: sudo dnf install cpio```

```pacman: sudo pacman -S cpio```

```apk: sudo apk add cpio```

```zypper: sudo zypper install cpio```

```brew: brew install cpio```

```nix: nix profile install nixpkgs#cpio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tar](/man/tar)(1), [find](/man/find)(1), [pax](/man/pax)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/cpio.git)```

```[Homepage](https://www.gnu.org/software/cpio/)```

```[Documentation](https://www.gnu.org/software/cpio/manual/)```

<!-- verified: 2026-06-23 -->

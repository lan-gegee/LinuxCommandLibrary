# TAGLINE

从 squashfs 文件系统中提取文件

# TLDR

**解压**到 squashfs-root

```unsquashfs [filesystem.squashfs]```

解压到**指定**目录

```unsquashfs -d [path/to/directory] [filesystem.squashfs]```

解压时显示**文件名**

```unsquashfs -i [filesystem.squashfs]```

显示带**属性**的文件

```unsquashfs -li [filesystem.squashfs]```

仅**列出**文件而不解压

```unsquashfs -l [filesystem.squashfs]```

**列出**带属性的文件

```unsquashfs -ll [filesystem.squashfs]```

**解压**特定文件或目录

```unsquashfs [filesystem.squashfs] [path/to/file] [path/to/dir]```

显示文件系统**超级块**信息

```unsquashfs -s [filesystem.squashfs]```

# SYNOPSIS

**unsquashfs** [_OPTIONS_] _FILESYSTEM_

# PARAMETERS

**-d, -dest** _DIR_
> 解压到指定目录

**-i, -info**
> 解压过程中显示文件名

**-li, -linfo**
> 解压过程中显示文件名和属性

**-l, -ls**
> 列出文件而不解压

**-ll, -lls**
> 列出文件及其属性而不解压

**-f, -force**
> 覆盖已存在的文件

**-s, -stat**
> 显示文件系统超级块信息

**-n, -no-progress**
> 不显示进度条

**-p** _NUMBER_, **-processors** _NUMBER_
> 使用 NUMBER 个处理器进行解压

**-e** _FILE_, **-ef** _FILE_
> 要解压的目录或文件的列表，每行一个

# DESCRIPTION

**unsquashfs** 从 squashfs 压缩文件系统中提取并列出文件。Squashfs 是一种只读压缩文件系统，常用于 Linux 发行版、Live CD 和嵌入式系统。

默认情况下，文件会被解压到当前工作目录下的 squashfs-root 目录。

# CAVEATS

解压可能需要大量磁盘空间。某些文件系统包含需要 root 权限的设备节点。以 root 身份运行时会保留原始权限和所有者信息。

# INSTALL

```apt: sudo apt install squashfs-tools```

```dnf: sudo dnf install squashfs-tools```

```pacman: sudo pacman -S squashfs-tools```

```apk: sudo apk add squashfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mksquashfs](/man/mksquashfs)(1), [sqfscat](/man/sqfscat)(1)

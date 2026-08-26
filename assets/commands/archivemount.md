# TAGLINE

通过 FUSE 将归档文件挂载为虚拟文件系统

# TLDR

将归档**挂载**到指定挂载点

```archivemount [path/to/archive] [path/to/mount_point]```

将归档挂载为**只读**

```archivemount -o readonly [path/to/archive] [path/to/mount_point]```

**卸载**归档文件系统

```fusermount -u [path/to/mount_point]```

# SYNOPSIS

**archivemount** [_options_] _archive_ _mountpoint_

# DESCRIPTION

**archivemount** 是一个基于 FUSE 的文件系统，可将归档挂载为虚拟目录。它支持多种归档格式，包括 tar、zip、cpio、ISO 9660 以及压缩变体（gzip、bzip2、xz、lzma）。

挂载后即可像访问普通目录一样访问归档内容。这对于浏览大型归档或从中提取特定文件非常有用，无需完整解压。

# PARAMETERS

**-o readonly**
> 将归档挂载为只读

**-o nosave**
> 卸载时不保存对归档的更改

**-o nobackup**
> 修改归档前不创建备份

**-f**
> 在前台运行（不守护进程化）

# CAVEATS

写入支持尚属实验性，并非对所有归档格式都可靠。修改内容先缓存在内存中，只在卸载时写入，大量更改可能占用较多内存。归档格式必须受 libarchive 支持。

# HISTORY

**archivemount** 作为 FUSE 生态系统的一部分而开发，用于提供对归档内容的透明访问。它利用 **libarchive** 实现格式支持，自 2000 年代中期起可用。

# INSTALL

```apt: sudo apt install archivemount```

```dnf: sudo dnf install archivemount```

```aur: yay -S archivemount```

```apk: sudo apk add archivemount```

```brew: brew install archivemount```

```nix: nix profile install nixpkgs#archivemount```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[fusermount](/man/fusermount)(1), [tar](/man/tar)(1), [mount](/man/mount)(8)

# RESOURCES

```[Source code](https://github.com/cybernoid/archivemount)```

<!-- verified: 2026-06-11 -->

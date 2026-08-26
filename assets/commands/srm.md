# TAGLINE

带覆写的安全文件删除

# TLDR

**安全删除文件**

```srm [file.txt]```

**递归删除目录**

```srm -r [directory/]```

**简单覆写（更快）**

```srm -s [file.txt]```

**中等安全（7 次覆写）**

```srm -m [file.txt]```

**最高安全（38 次覆写）**

```srm -z [file.txt]```

**详细输出**

```srm -v [file.txt]```

**强制删除**

```srm -f [file.txt]```

# SYNOPSIS

**srm** [_-r_] [_-s_|_-m_|_-z_] [_-f_] [_-v_] _files_

# PARAMETERS

**-r**, **-R**
> 递归删除。

**-s**
> 简单覆写。

**-m**
> 中等安全（7 次覆写）。

**-z**
> Gutmann 算法（38 次覆写）。

**-f**
> 强制执行，不提示确认。

**-v**
> 详细输出。

**-l**
> 降低安全性以换取速度。

**-x**
> 仅限单一文件系统。

# DESCRIPTION

**srm**（secure rm）在解除链接之前先覆写文件内容，使数据恢复远比使用标准 **rm** 困难。它提供多种安全级别：简单模式（**-s**）为求速度只执行一次覆写；中等模式（**-m**）基于 DoD 5220.22-M 标准进行 7 次覆写；默认的 Gutmann 模式（**-z**）则以各种模式执行 38 次覆写，旨在对抗磁力显微镜恢复技术。

该工具通过 **-r** 处理递归目录删除，并支持强制模式（**-f**）跳过确认提示。文件名也会在删除前被覆写，以防从目录项中恢复出文件名。

# CAVEATS

SSD 的 trim 操作可能绕过覆写。日志式文件系统可能保留副本。处理大文件时速度较慢。

# HISTORY

**srm** 为安全删除文件而开发。它实现了多种覆写方法以阻止数据恢复。

# INSTALL

```apt: sudo apt install secure-delete```

```zypper: sudo zypper install srm```

```nix: nix profile install nixpkgs#srm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[shred](/man/shred)(1), [rm](/man/rm)(1), [wipe](/man/wipe)(1)

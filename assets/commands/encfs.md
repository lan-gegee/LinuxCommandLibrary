# TAGLINE

基于 FUSE 的用户空间加密文件系统

# TLDR

**创建/挂载加密目录**

```encfs [~/.encrypted] [~/private]```

**以标准模式创建**

```encfs -s [~/.encrypted] [~/private]```

**卸载加密目录**

```fusermount -u [~/private]```

**更改密码**

```encfsctl passwd [~/.encrypted]```

**显示卷信息**

```encfsctl info [~/.encrypted]```

空闲超时后自动**卸载**

```encfs -i [10] [~/.encrypted] [~/private]```

# SYNOPSIS

**encfs** [_options_] _encdir_ _mountpoint_

# DESCRIPTION

**encfs** 使用 FUSE 在用户空间提供加密文件系统。它逐个加密文件，将它们以加密的文件名和内容存储在一个目录中。

该工具适合加密云同步文件夹或敏感目录。每个文件独立加密，因此变更过的文件可以高效同步。

# PARAMETERS

**-s**
> 单线程模式。

**-f**
> 以前台方式运行。

**-v**
> 详细输出模式。

**-i** _minutes_
> 卸载前的空闲超时时间。

**-o** _options_
> FUSE 挂载选项。

**--standard**
> 使用标准（更安全）设置。

**--paranoid**
> 使用偏执（paranoid）设置。

**--reverse**
> 用于备份的反向模式。

**--extpass** _cmd_
> 外部密码程序。

# CONFIGURATION

**.encfs6.xml**
> 存储在加密目录中的配置文件，包含加密参数与设置。

# CAVEATS

会泄露文件大小和目录结构。无法抵抗水印攻击。可考虑 gocryptfs 等更新的替代品。FUSE 会带来额外开销。口令一旦遗失无法恢复。

# HISTORY

**encfs** 由 **Valient Gough** 于 **2003 年**创建，是 Linux 上用户空间加密文件系统的先驱。它多年来广受欢迎，但安全审计暴露了一些弱点，因此新部署被建议改用 gocryptfs 等替代方案。

# INSTALL

```apt: sudo apt install encfs```

```pacman: sudo pacman -S encfs```

```apk: sudo apk add encfs```

```zypper: sudo zypper install encfs```

```brew: brew install encfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gocryptfs](/man/gocryptfs)(1), [cryptsetup](/man/cryptsetup)(1), [fusermount](/man/fusermount)(1), [ecryptfs](/man/ecryptfs)(1)

# RESOURCES

```[Source code](https://github.com/vgough/encfs)```

<!-- verified: 2026-07-14 -->

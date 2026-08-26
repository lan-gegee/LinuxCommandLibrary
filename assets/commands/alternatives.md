# TAGLINE

管理默认命令的符号链接

# TLDR

此命令是 update-alternatives 的**别名**

查看原始命令的文档

```tldr update-alternatives```

# SYNOPSIS

**alternatives**

# DESCRIPTION

**alternatives** 维护一组符号链接，用于决定某个通用名称实际运行的默认命令（例如使用哪个 **java** 或 **editor**）。它让多个软件包可以提供同一功能，并在它们之间进行选择。

在 Debian 和 Ubuntu 上，**alternatives** 只是 **update-alternatives** 的另一个名称，后者随 dpkg 一同发布。在 Fedora、RHEL 及相关发行版上，它是由 chkconfig 软件包提供的另一个独立实现，行为相似但不完全相同。完整的 Debian 文档参见 **update-alternatives**。

# INSTALL

```dnf: sudo dnf install alternatives```

```aur: yay -S alternatives```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[update-alternatives](/man/update-alternatives)(1)

# RESOURCES

```[Source code](https://git.dpkg.org/cgit/dpkg/dpkg.git)```

```[Documentation](https://manpages.ubuntu.com/manpages/noble/man1/update-alternatives.1.html)```

<!-- verified: 2026-06-11 -->

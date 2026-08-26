# TAGLINE

显示邮件队列

# TLDR

**显示邮件队列**

```mailq```

**显示队列摘要**

```mailq -p```

**显示详细输出**

```mailq -v```

# SYNOPSIS

**mailq** [_options_]

# PARAMETERS

**-p**
> 打印队列摘要。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mailq** 显示邮件队列。它会列出等待投递的邮件。

该工具通常是指向 sendmail 或 postfix 的符号链接。它列出排队、延迟和暂挂的邮件。

# CAVEATS

输出取决于所用的 MTA。查看完整细节可能需要 root 权限。属于 MTA 软件包的一部分。

# HISTORY

mailq 提供了一个标准接口，用于在不同**邮件传输代理**（MTA）之间查看邮件队列。

# INSTALL

```apt: sudo apt install dma```

```dnf: sudo dnf install postfix```

```pacman: sudo pacman -S postfix```

```apk: sudo apk add postfix```

```zypper: sudo zypper install postfix```

```nix: nix profile install nixpkgs#dma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sendmail](/man/sendmail)(8), [postqueue](/man/postqueue)(1), [postfix](/man/postfix)(1)

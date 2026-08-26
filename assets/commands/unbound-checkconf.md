# TAGLINE

校验 Unbound DNS 配置文件

# TLDR

**检查默认配置文件**

```unbound-checkconf```

**检查指定配置文件**

```unbound-checkconf [/etc/unbound/unbound.conf]```

**输出指定选项的值**

```unbound-checkconf -o [verbosity]```

**安静地检查配置**（成功时无输出）

```unbound-checkconf -q [/etc/unbound/unbound.conf]```

# SYNOPSIS

**unbound-checkconf** [_options_] [_configfile_]

# PARAMETERS

**-h**
> 显示帮助并退出。

**-f**
> 输出应用 chroot 后的完整路径名。与 -o 选项一起使用。

**-o** _option_
> 将特定选项的值输出到 stdout。

**-q**
> 安静模式，成功时不输出内容。

# DESCRIPTION

**unbound-checkconf** 校验 Unbound DNS 解析器配置文件中的语法错误和配置问题。它检查指定的文件，若未给出文件则检查默认配置位置。

该工具验证配置语法、检查选项值是否有效，并确保被引用的文件（如密钥文件和证书）存在且可读。在重启 Unbound 之前运行此命令可以避免因配置错误导致的服务中断。

-o 选项用于提取特定的配置值，便于脚本编写或验证设置。对于已禁用的选项，会输出一个空行。

# EXIT STATUS

配置有效时返回 0，发现错误时返回 1。错误消息会指出问题的性质和位置。

# CAVEATS

某些错误（如缺少自动生成的文件）只在运行时出现。不校验远程服务器的连通性。默认配置路径因安装方式而异。

# HISTORY

**unbound-checkconf** 是由 NLnet Labs 开发的 Unbound DNS 解析器的一部分。Unbound 被设计为一个现代、安全、支持 DNSSEC 的验证型递归 DNS 解析器，旨在作为仅解析器部署场景中 BIND 的替代品。

# INSTALL

```apt: sudo apt install unbound```

```dnf: sudo dnf install unbound```

```pacman: sudo pacman -S unbound```

```apk: sudo apk add unbound```

```zypper: sudo zypper install unbound```

```brew: brew install unbound```

```nix: nix profile install nixpkgs#unbound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unbound](/man/unbound)(8), [unbound-control](/man/unbound-control)(8), [unbound-host](/man/unbound-host)(1)

# TAGLINE

生成适用于 /etc/shadow 等用途的密码哈希

# TLDR

**生成密码哈希**

```mkpasswd [password]```

**用指定方法生成**

```mkpasswd -m sha-512 [password]```

**带盐值生成**

```mkpasswd -S [salt] [password]```

**生成随机密码**

```mkpasswd -l [16]```

**列出可用的方法**

```mkpasswd -m help```

# SYNOPSIS

**mkpasswd** [_options_] [_password_]

# DESCRIPTION

**mkpasswd** 生成适用于 /etc/shadow 或类似用途的密码哈希。它支持多种哈希算法，还可选地生成随机密码。

该工具适合为系统配置文件和自动化部署创建加密密码。

# PARAMETERS

**-m** _method_
> 哈希方法（sha-512、sha-256、md5、des）。

**-S** _salt_
> 指定盐值。

**-R** _rounds_
> SHA 轮数。

**-l** _length_
> 生成指定长度的随机密码。

**-s**, **--stdin**
> 从标准输入读取密码。

**-5**
> 使用 MD5（快捷方式）。

**-P** _fd_
> 从文件描述符读取密码。

# CAVEATS

不同版本的选项不同。whois 软件包的版本与 expect 软件包的不同。推荐使用强哈希方法（sha-512）。避免存储明文密码。

# HISTORY

**mkpasswd** 存在多种实现。whois 软件包版本在 Debian/Ubuntu 上常见，其他系统可能是 expect 软件包的版本。两者都提供密码哈希功能但选项各异。

# INSTALL

```apt: sudo apt install whois```

```dnf: sudo dnf install whois```

```pacman: sudo pacman -S whois```

```apk: sudo apk add expect```

```zypper: sudo zypper install whois```

```brew: brew install whois```

```nix: nix profile install nixpkgs#whois```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[passwd](/man/passwd)(1), [openssl](/man/openssl)(1), [chpasswd](/man/chpasswd)(1)

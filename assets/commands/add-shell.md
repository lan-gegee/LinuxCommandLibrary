# TAGLINE

注册有效的登录 Shell

# TLDR

将 Shell **添加**到 /etc/shells

```sudo add-shell [/usr/local/bin/zsh]```

添加**多个**Shell

```sudo add-shell [/bin/fish] [/bin/zsh]```

# SYNOPSIS

**add-shell** _shell_ [_shell_...]

# DESCRIPTION

**add-shell** 是 Debian 的实用工具，用于安全地向 /etc/shells 添加新的 Shell 路径。/etc/shells 文件列出用户可通过 **chsh** 选择的有效登录 Shell。

它会先把 /etc/shells 复制为 /etc/shells.tmp，追加其中尚未存在的给定 Shell，再把临时文件复制回 /etc/shells。由于会跳过已存在的条目，因此可在软件包维护者脚本中放心地重复调用。与之对应的 **remove-shell** 则用于删除条目。

# PARAMETERS

**shell**
> 要添加的 Shell 可执行文件的绝对路径

# CAVEATS

需要 root 权限。Shell 可执行文件必须存在且有效。并非所有发行版都提供此命令；在没有该命令的系统上，请手动编辑 /etc/shells。

# HISTORY

**add-shell** 是 Debian 打包实用工具的一部分，其诞生是为了在软件包安装脚本中对 /etc/shells 进行安全的操作。

# INSTALL

```apt: sudo apt install debianutils```

```aur: yay -S debianutils```

```zypper: sudo zypper install debianutils```

```brew: brew install debianutils```

```nix: nix profile install nixpkgs#debianutils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[chsh](/man/chsh)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/debianutils)```

```[Documentation](https://manpages.ubuntu.com/manpages/noble/man8/add-shell.8.html)```

<!-- verified: 2026-06-11 -->

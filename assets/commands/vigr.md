# TAGLINE

以加锁方式编辑 group 或 shadow-group 文件

# TLDR

**编辑 /etc/group 文件**

```sudo vigr```

**编辑 /etc/gshadow（影子组）文件**

```sudo vigr -s```

**在 chroot 环境中编辑组文件**

```sudo vigr -R [/path/to/chroot]```

# SYNOPSIS

**vigr** [_options_]

# DESCRIPTION

**vigr** 编辑 `/etc/group` 文件（使用 **-s** 时编辑 `/etc/gshadow`），同时设置适当的锁以防止并发访问导致文件损坏。它会先锁定文件，创建一个临时副本，在用户偏好的编辑器中打开（依次检查 `$VISUAL`、`$EDITOR`，最后回退到 `vi`），编辑完成后执行语法检查，然后原子性地替换原文件。

# PARAMETERS

**-g**, **--group**
> 编辑组数据库（默认）。

**-s**, **--shadow**
> 编辑 gshadow（影子组）数据库。

**-p**, **--passwd**
> 编辑 passwd 数据库（等同于运行 vipw）。

**-q**, **--quiet**
> 安静模式。

**-R**, **--root** _CHROOT_DIR_
> 在 chroot 环境中应用更改。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

应始终使用 **vigr** 命令而不是直接编辑 `/etc/group`，以防并发访问损坏文件。更改立即生效。需要 root 权限。如果编辑了 `/etc/group`，还应运行 `vigr -s` 检查 `/etc/gshadow` 的一致性。

# HISTORY

**vigr** 是 **shadow-utils** 软件包的一部分，用于安全地编辑组文件，类似于 vipw 编辑密码文件的方式。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vipw](/man/vipw)(8), [group](/man/group)(5), [gshadow](/man/gshadow)(5), [groupadd](/man/groupadd)(8), [groupmod](/man/groupmod)(8), [groupdel](/man/groupdel)(8)

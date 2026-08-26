# TAGLINE

显示已录入的指纹

# TLDR

列出**特定用户**已录入的指纹

```fprintd-list [username]```

列出**多个用户**已录入的指纹

```fprintd-list [username1] [username2] ...```

显示**帮助**

```fprintd-list```

# SYNOPSIS

**fprintd-list** _username_ [_username_...]

# DESCRIPTION

**fprintd-list** 显示指定用户在 fprintd 数据库中已录入的指纹。输出会展示每个用户注册了哪些手指。

该命令通过 D-Bus 查询 fprintd 守护进程以获取录入信息。在尝试认证之前，或决定还要录入哪些手指时，可以用它来确认哪些手指已经注册。

# CAVEATS

需要 fprintd 守护进程正在运行。列出其他用户的指纹可能需要相应的权限。

# INSTALL

```apt: sudo apt install fprintd```

```dnf: sudo dnf install fprintd```

```pacman: sudo pacman -S fprintd```

```apk: sudo apk add fprintd```

```zypper: sudo zypper install fprintd```

```nix: nix profile install nixpkgs#fprintd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fprintd](/man/fprintd)(1), [fprintd-enroll](/man/fprintd-enroll)(1), [fprintd-delete](/man/fprintd-delete)(1), [fprintd-verify](/man/fprintd-verify)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/libfprint/fprintd)```

<!-- verified: 2026-07-15 -->

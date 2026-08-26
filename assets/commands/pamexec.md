# TAGLINE

对多图像 PAM 流中的每幅图像执行指定的 shell 命令

# TLDR

**对流中每幅图像应用命令**

```pamexec "[pnmflip -lr]" [input.pam] > [output.pam]```

# SYNOPSIS

**pamexec** _command_ [_file_]

# PARAMETERS

_command_
> 要对每幅图像执行的 shell 命令。

# DESCRIPTION

**pamexec** 对多图像 PAM 流中的每幅图像运行指定的 shell 命令。命令从 stdin 接收每幅图像并输出到 stdout。属于 Netpbm 工具集。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pamsplit](/man/pamsplit)(1)

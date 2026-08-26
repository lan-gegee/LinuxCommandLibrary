# TAGLINE

列出 yadm 跟踪的 dotfiles

# TLDR

**列出被跟踪的文件**

```yadm list```

**列出并包含属性**

```yadm list -a```

# SYNOPSIS

**yadm** **list** [_options_]

# PARAMETERS

**-a**
> 包含属性信息。

# DESCRIPTION

**yadm list** 显示由 yadm 跟踪的文件，即纳入版本控制的全部 dotfiles。适合用于审计受管理的文件。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1)

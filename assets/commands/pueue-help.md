# TAGLINE

显示 pueue 命令的帮助信息

# TLDR

**显示常规帮助**

```pueue help```

**显示某命令的帮助**

```pueue help [command]```

**显示 add 命令帮助**

```pueue help add```

# SYNOPSIS

**pueue help** [_command_]

# PARAMETERS

_COMMAND_
> 要获取帮助的命令。

# DESCRIPTION

**pueue help** 显示 pueue 命令的用法信息。不带参数调用时，它会列出所有可用的子命令和全局选项。指定命令名时，则显示该子命令的详细帮助，包括其全部标志和参数。

# CAVEATS

也可通过 --help 标志获取。

# HISTORY

pueue help 为 pueue 命令提供**内置文档**。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1)

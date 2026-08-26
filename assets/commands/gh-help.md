# TAGLINE

显示命令文档和用法

# TLDR

**显示常规帮助**

```gh help```

**获取某条命令的帮助**

```gh help [pr]```

**获取某个子命令的帮助**

```gh help [pr] [create]```

**显示环境变量**

```gh help environment```

**列出格式化选项**

```gh help formatting```

# SYNOPSIS

**gh help** [_command_] [_subcommand_]

# PARAMETERS

_COMMAND_
> 要获取帮助的命令。

_SUBCOMMAND_
> 要获取帮助的子命令。

**environment**
> 显示环境变量。

**formatting**
> 显示输出格式化选项。

**mintty**
> 显示 MinTTY 配置帮助。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh help** 提供 GitHub CLI 命令的文档。它会显示任意 gh 命令或子命令的用法信息、可用标志、示例和相关命令。

帮助系统还包含一些特殊主题，例如影响 gh 行为的环境变量，以及用于自定义输出的格式化选项。帮助内容内置于 gh 二进制文件中，可离线查看。

gh help 是了解命令功能和正确用法的重要途径。

# CAVEATS

帮助内容与已安装的 gh 版本对应。在线文档可能更新。部分帮助主题与特定平台相关。

# HISTORY

gh help 遵循 Unix man page 惯例，作为 **GitHub CLI** 的一部分提供全面的命令文档。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [man](/man/man)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->

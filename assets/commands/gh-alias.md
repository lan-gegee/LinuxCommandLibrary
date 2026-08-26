# TAGLINE

GitHub CLI 命令别名管理

# TLDR

**列出别名**

```gh alias list```

**设置别名**

```gh alias set [name] "[command]"```

**删除别名**

```gh alias delete [name]```

**设置支持 shell 展开的别名**

```gh alias set --shell [name] "[shell command]"```

# SYNOPSIS

**gh** **alias** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出已定义的别名。

**set**
> 创建别名。

**delete**
> 移除别名（用 **--all** 移除全部）。

**import**
> 从 YAML 文件导入别名（或用 `-` 表示 stdin）。

# PARAMETERS

**--shell**
> 按 shell 命令展开。

# DESCRIPTION

**gh alias** 管理 GitHub CLI 的命令别名。为常用或复杂的命令创建快捷方式，简化你的 GitHub 工作流程。

别名可以简化多步操作、为常见任务提供简写形式，并让 CLI 更贴合你的开发习惯。Shell 别名支持管道和高级命令组合，而普通别名适用于 gh 子命令和标志。

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

[gh](/man/gh)(1), [gh-config](/man/gh-config)(1)

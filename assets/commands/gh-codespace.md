# TAGLINE

管理云端托管的开发环境

# TLDR

**列出 codespace**

```gh codespace list```

**创建 codespace**

```gh codespace create```

为特定仓库创建

```gh codespace create -r [owner/repo]```

**SSH 进入 codespace**

```gh codespace ssh```

**停止 codespace**

```gh codespace stop -c [codespace_name]```

**删除 codespace**

```gh codespace delete -c [codespace_name]```

**在 VS Code 中打开**

```gh codespace code```

# SYNOPSIS

**gh** **codespace** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出 codespace。

**create**
> 创建 codespace。

**ssh**
> SSH 进入 codespace。

**code**
> 在 VS Code 中打开。

**stop**
> 停止 codespace。

**delete**
> 删除 codespace。

**ports**
> 管理端口。

**logs**
> 查看日志。

# PARAMETERS

**-r**, **--repo** _owner/repo_
> 仓库。

**-c**, **--codespace** _name_
> Codespace 名称。

**-m**, **--machine** _type_
> 机器类型。

# DESCRIPTION

**gh codespace** 管理 GitHub Codespaces——云端托管的开发环境。可以在 CLI 中创建、连接和管理 codespace。

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

[gh](/man/gh)(1), [gh-repo](/man/gh-repo)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_codespace)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->

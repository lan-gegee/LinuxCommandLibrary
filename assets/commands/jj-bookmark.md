# TAGLINE

管理 Jujutsu 中指向修订的命名引用

# TLDR

在当前修订上创建书签

```jj bookmark create [name]```

在特定修订上创建书签

```jj bookmark create [name] -r [revision]```

列出版本书签

```jj bookmark list```

删除书签

```jj bookmark delete [name]```

移动书签

```jj bookmark move [name] --to [revision]```

# SYNOPSIS

**jj** **bookmark** _subcommand_ [_options_]

# SUBCOMMANDS

**create** _name_
> 创建新书签。

**delete** _name_
> 删除书签。

**list**
> 列出所有书签。

**move** _name_
> 将书签移动到其他修订。

**track**
> 跟踪远程书签。

# PARAMETERS

**-r**, **--revision** _rev_
> 目标修订。

**--to** _rev_
> move 的目标位置。

# DESCRIPTION

**jj bookmark** 管理 Jujutsu 中指向修订的命名引用。类似于 Git 分支，书签指向特定提交，可以推送到远程或从远程拉取。提交被改写时，书签会跟随移动。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-git-push](/man/jj-git-push)(1)

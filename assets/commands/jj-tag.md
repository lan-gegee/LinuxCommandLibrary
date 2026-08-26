# TAGLINE

管理 Jujutsu 仓库中的标签

# TLDR

列出所有标签

```jj tag list```

创建标签

```jj tag set [tagname]```

删除标签

```jj tag delete [tagname]```

# SYNOPSIS

**jj** **tag** _subcommand_ [_options_]

# PARAMETERS

**list** [_pattern_]
> 列出标签，可选过滤条件。

**set** _name_
> 创建或更新标签。

**delete** _name_
> 删除标签。

# DESCRIPTION

**jj tag** 管理 Jujutsu 仓库中的标签。标签是指向特定提交的轻量级引用，适合标记发布或历史中的重要节点。与书签不同，标签不会移动。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-bookmark](/man/jj-bookmark)(1)

# TAGLINE

在最近一次提交信息后追加标识戳

# TLDR

**为最近一次提交加盖标识戳**，含 id 和消息

```git stamp [Reviewed-by] "[Jane Doe]"```

**只带 id 加戳**

```git stamp [Fixes-123]```

**替换已有的同 id 标识戳**

```git stamp --replace [Reviewed-by] "[Jane Doe]"```

# SYNOPSIS

**git** **stamp** [_-r_ | _--replace_] _id_ [_message_...]

# PARAMETERS

_ID_
> 戳的标识符（如 `Reviewed-by`、`Fixes`）。

_MESSAGE_
> 可选文本，附加在 id 之后。

**-r**, **--replace**
> 在追加新戳之前，先移除消息中所有具有相同 id（不区分大小写）的既有戳行。

# DESCRIPTION

**git stamp** 会修补最近一次提交，在其消息中追加一个形如 `<id> <message>` 的新段落。它属于 git-extras，可以快速给提交打上 `Reviewed-by`、`Tested-by` 或 issue 引用之类的元数据，无需手动编辑提交信息。

使用 `--replace` 时，消息中所有以相同 id 开头的既有段落都会先被剔除，然后再加入新戳，因此重复运行该命令是更新而非叠加。

# CAVEATS

它会修补 HEAD，因此会重写提交哈希；不要对已经推送并分享给他人的提交使用。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-commit](/man/git-commit)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-stamp)```

<!-- verified: 2026-07-17 -->

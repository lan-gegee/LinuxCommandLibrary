# TAGLINE

创建、列出和管理标签

# TLDR

**列出标签**

```git tag```

**创建轻量标签**

```git tag [name]```

**创建附注标签**

```git tag -a [name] -m "[message]"```

**创建签名标签**

```git tag -s [name] -m "[message]"```

**给指定提交打标签**

```git tag [name] [commit]```

**删除标签**

```git tag -d [name]```

**将标签推送到远程**

```git push origin [name]```

**列出匹配模式的标签**

```git tag -l "[v1.*]"```

# SYNOPSIS

**git** **tag** [_options_] [_name_] [_commit_]

# PARAMETERS

**-a**, **--annotate**
> 创建附注标签。

**-m**, **--message** _msg_
> 标签信息。

**-s**, **--sign**
> 创建签名标签。

**-d**, **--delete**
> 删除标签。

**-f**, **--force**
> 强制替换标签。

**-l**, **--list** _pattern_
> 列出匹配的标签。

**-n** _num_
> 显示若干行附注内容。

**--contains** _commit_
> 包含某提交的标签。

**--sort** _key_
> 对标签排序。

**--points-at** _object_
> 列出指向给定对象的标签。

**--format** _format_
> 使用 `git for-each-ref` 风格的占位符字符串来格式化输出。

**-v**, **--verify**
> 验证签名标签的 GPG 签名。

# DESCRIPTION

**git tag** 用于创建、列出、删除和验证标签对象。标签用来把历史中的特定时点标记为重要节点，最常用于发布版本。

轻量标签只是指向某个提交的简单指针，而附注标签会保存额外的元数据，如打标者姓名、日期和信息。签名标签还会附加 GPG 签名以便验证。

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

[git-branch](/man/git-branch)(1), [git-commit](/man/git-commit)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-tag)```

<!-- verified: 2026-07-17 -->

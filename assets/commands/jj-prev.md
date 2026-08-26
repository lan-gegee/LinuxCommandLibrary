# TAGLINE

相对于父修订移动工作副本修订

# TLDR

移动到父修订

```jj prev```

向后移动多步

```jj prev [3]```

移动并直接编辑父修订

```jj prev --edit```

跳到上一个存在冲突的祖先

```jj prev --conflict```

# SYNOPSIS

**jj** **prev** [_OPTIONS_] [_OFFSET_]

# PARAMETERS

_OFFSET_
> 向后移动的修订数量。默认：**1**。

**-e**, **--edit**
> 直接编辑父修订，而不是移动工作副本提交。覆盖 **ui.movement.edit** 配置。

**-n**, **--no-edit**
> --edit 的反向操作；在目标位置之上创建新的工作副本提交。

**--conflict**
> 跳到上一个存在冲突的祖先。

# DESCRIPTION

**jj prev** 将工作副本提交移动到某个祖先修订。默认情况下，它会在目标祖先之下创建一个新的空工作副本修订。使用 **--edit** 时，它会直接编辑该祖先修订。

该命令是 Jujutsu 版本控制系统中向后浏览提交历史的便捷简写。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-next](/man/jj-next)(1), [jj-log](/man/jj-log)(1)

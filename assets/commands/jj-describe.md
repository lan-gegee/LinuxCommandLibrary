# TAGLINE

更新变更的描述

# TLDR

描述当前变更

```jj describe -m "[message]"```

描述特定修订

```jj describe -r [rev] -m "[message]"```

打开编辑器撰写描述

```jj describe```

清空描述

```jj describe -m ""```

通过 stdin 描述

```echo "[message]" | jj describe --stdin```

# SYNOPSIS

**jj describe** [_options_]

# PARAMETERS

**-m**, **--message** _MESSAGE_
> 设置描述而不打开编辑器。可多次传入。

**-r** _REV_
> 要描述的修订。默认为 `@`（当前变更）。

**--stdin**
> 从标准输入读取描述。

**--edit**
> 即使提供了消息也强制打开编辑器。

**--no-edit**
> 不打开编辑器；在没有提供其他输入时保留当前描述。

**--reset-author**
> 将变更的作者重置为已配置的用户（较新版本的 jj）。

**--author** _NAME_EMAIL_
> 覆盖作者（较新版本的 jj）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj describe** 更新变更的描述。它用于设置或修改等价于提交说明的内容。

该命令默认打开编辑器，也接受内联消息。描述可以随时更新。

# CAVEATS

jj 的子命令。描述可以随时更改。允许空描述。

# HISTORY

jj describe 是 **Jujutsu** 的一部分，支持可在整个开发过程中随时修改的灵活变更描述。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-new](/man/jj-new)(1), [jj-log](/man/jj-log)(1)

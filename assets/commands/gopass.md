# TAGLINE

面向团队、兼容 pass 的密码管理器

# TLDR

**初始化密码库**

```gopass init```

**生成新密码**

```gopass generate [site/username]```

**显示密码**

```gopass show [site/username]```

**将密码复制到剪贴板**

```gopass show -c [site/username]```

**录入新的机密条目**

```gopass insert [site/username]```

**列出所有条目**

```gopass ls```

**搜索条目**

```gopass find [query]```

**与远程同步**

```gopass sync```

# SYNOPSIS

**gopass** [_options_] _command_ [_args_]

# PARAMETERS

**init**
> 初始化密码库。

**generate** _name_ [_length_]
> 生成新密码。

**insert** _name_
> 录入新的机密条目。

**show** _name_
> 显示机密内容。

**ls** [_folder_]
> 列出条目。

**find** _query_
> 搜索条目。

**edit** _name_
> 编辑已有条目。

**rm** _name_
> 删除条目。

**mv** _old_ _new_
> 移动/重命名条目。

**sync**
> 与 git 远程仓库同步。

**-c**, **--clip**
> 复制到剪贴板。

# DESCRIPTION

**gopass** 是一个与 pass（标准 Unix 密码管理器）兼容的密码管理器。它把用 GPG 加密的密码存储在 git 仓库中，从而实现版本控制和同步。

该工具支持多个密码库、团队共享、TOTP 生成以及与浏览器和其他工具的集成。相比标准 pass，它还提供了更完善的多用户处理和子库挂载等特性。

# CONFIGURATION

**~/.config/gopass/config**
> gopass 配置文件，包含密码库位置、挂载点和默认设置。

**~/.local/share/gopass/stores/**
> 密码库数据的默认存储位置。

# CAVEATS

需要先配置 GPG 密钥。同步功能需要 git 配置。剪贴板会在超时后自动清空。多个接收者之间需要交换密钥。

# HISTORY

**gopass** 作为一款用 Go 编写、兼容 pass 的密码管理器而诞生，增加了面向团队使用和更好机密管理的特性。它出现于 **2017 年**前后，当时各组织正需要基于 GPG 加密的共享密码管理方案。

# INSTALL

```dnf: sudo dnf install gopass```

```pacman: sudo pacman -S gopass```

```apk: sudo apk add gopass```

```zypper: sudo zypper install gopass```

```brew: brew install gopass```

```nix: nix profile install nixpkgs#gopass```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [gpg](/man/gpg)(1), [git](/man/git)(1), [op](/man/op)(1)

# RESOURCES

```[Source code](https://github.com/gopasspw/gopass)```

```[Homepage](https://www.gopass.pw/)```

```[Documentation](https://github.com/gopasspw/gopass/tree/master/docs)```

<!-- verified: 2026-07-17 -->

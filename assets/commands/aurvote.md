# TAGLINE

从命令行为 AUR 软件包投票

# TLDR

以交互方式**配置** AUR 凭据

```aurvote --configure```

为一个或多个 AUR 软件包**投票**

```aurvote [package1] [package2] ...```

为一个或多个 AUR 软件包**取消投票**

```aurvote -u [package1] [package2] ...```

**检查**软件包是否已被投票

```aurvote -c [package1] [package2] ...```

**显示版本**信息

```aurvote -V```

# SYNOPSIS

**aurvote** [_options_] [_packages_]

# DESCRIPTION

**aurvote** 允许从命令行对 Arch 用户仓库中的软件包投票。投票有助于反映软件包的热门程度，也是对维护者有用的反馈。

凭据存储在 **~/.config/aurvote** 中，使用前必须先完成配置。该文件包含你的 AUR 用户名和密码。

# PARAMETERS

**--configure**
> 以交互方式创建凭据文件。

**-v**, **--vote**
> 为指定软件包投票（默认动作）。

**-u**, **--unvote**
> 取消对指定软件包的投票。

**-c**, **--check**
> 检查软件包是否已被投票。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

需要有 AUR 账户。凭据以明文形式存储在 **~/.config/aurvote** 中。投票需要对 AUR 网站进行身份验证。

# SEE ALSO

[yay](/man/yay)(1), [paru](/man/paru)(1), [auracle](/man/auracle)(1)

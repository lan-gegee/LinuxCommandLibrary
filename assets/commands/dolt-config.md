# TAGLINE

管理仓库级和全局设置

# TLDR

**设置全局用户**名

```dolt config --global --add user.name "[Your Name]"```

**设置全局邮箱**

```dolt config --global --add user.email "[email@example.com]"```

**列出全部配置**

```dolt config --list```

**获取指定值**

```dolt config --get user.name```

**设置本地配置**

```dolt config --local --set [key] [value]```

**删除配置项**

```dolt config --global --unset [key]```

# SYNOPSIS

**dolt config** [**--global**|**--local**] **--list**

**dolt config** [**--global**|**--local**] **--add**|**--set** _name_ _value_

**dolt config** [**--global**|**--local**] **--get** _name_

**dolt config** [**--global**|**--local**] **--unset** _name_...

# PARAMETERS

**--global**
> 操作全局配置，该配置由当前用户的所有仓库共享。

**--local**
> 操作仓库本地的配置。

**--set** _name_ _value_
> 设置一个或多个配置参数的值。

**--add** _name_ _value_
> 设置一个或多个配置参数的值（**--set** 的同义词）。

**--get** _name_
> 打印一个或多个配置参数的值。

**--unset** _name_...
> 移除一个或多个配置参数。

**--list**
> 列出所有配置参数的值。

# DESCRIPTION

**dolt config** 管理全局和仓库本地两个层级的 Dolt 配置。核心配置包括用于提交署名的用户身份（姓名和邮箱）。

全局配置对该用户的所有仓库生效，本地配置只作用于单个仓库。两者同时存在时，本地配置优先。

配置体系沿用了 Git 的 config 系统，包括其优先级规则，但值以 JSON 而非 INI 格式存储。除 `user.name` 和 `user.email` 外，常见键还包括 `init.defaultbranch`、用于服务器默认值的 `sqlserver.global.*`，以及用于关闭使用情况上报的 `metrics.disabled`。

# CONFIGURATION

**~/.dolt/config_global.json**
> 当前用户全部 Dolt 仓库共用的全局配置。

**.dolt/config.json**
> 仓库本地配置，其优先级高于全局设置。

# CAVEATS

首次提交前必须设置身份信息（`user.name` 和 `user.email`）；否则 Dolt 会拒绝提交。未知键会被静默接受，键名拼写错误不会报错，只会悄悄失效。**--local** 只能在 Dolt 数据库目录内使用。`sqlserver.global.*` 下的服务器相关设置只在启动时读取，因此修改后必须重启 `dolt sql-server` 才能生效。

# HISTORY

dolt config 有意紧贴 **git config** 的约定：Dolt 的整套界面都力求让熟悉 Git 的人一看就会用，而配置命令正是 2019 年 Dolt 发布时最早移植的命令之一。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt](/man/dolt)(1), [dolt-commit](/man/dolt-commit)(1), [git-config](/man/git-config)(1)

# RESOURCES

```[Source code](https://github.com/dolthub/dolt)```

```[Documentation](https://www.dolthub.com/docs/cli-reference/cli/)```

<!-- verified: 2026-07-14 -->

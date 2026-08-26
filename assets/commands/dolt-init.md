# TAGLINE

创建新的 Dolt 数据仓库

# TLDR

**在当前目录初始化 Dolt 仓库**

```dolt init```

**使用指定的初始分支名称**初始化

```dolt init -b [main]```

以作者姓名和邮箱**初始化**

```dolt init --name "[John Doe]" --email "[john@example.com]"```

**为初始提交指定自定义日期**

```dolt init --date "[2024-01-01T00:00:00]"```

# SYNOPSIS

**dolt** **init** [_options_]

# PARAMETERS

**-b**, **--initial-branch** _string_
> 初始分支的名称。未提供时使用全局配置中的 `init.defaultbranch`（默认 "main"）。

**--name** _string_
> 初始提交的作者姓名。未提供时使用全局配置中的 `user.name`。

**--email** _string_
> 初始提交的作者邮箱。未提供时使用全局配置中的 `user.email`。

**--date** _string_
> 初始提交使用的日期。未指定时使用当前系统时间。

**--fun**
> 创建仓库时附带一条有趣的初始提交消息。

# DESCRIPTION

**dolt init** 在当前目录创建一个新的空 Dolt 仓库。它会初始化 `.dolt` 目录结构，其中包含元数据、配置以及版本化 SQL 数据库的底层存储。

这通常是开始一个新的 Dolt 项目时运行的第一个命令。初始化完成的仓库立刻就能接受建表、插入数据和提交操作。同时会创建一个初始分支（默认名为 "main"，可用 `-b` 自定义）。

用户身份信息（姓名和邮箱）可以在初始化时提供，也可以继承自全局配置。该身份将用于后续所有提交的署名。

如果当前目录已经存在初始化过的 Dolt 仓库，该命令会失败。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolt-clone](/man/dolt-clone)(1), [dolt-status](/man/dolt-status)(1), [dolt-commit](/man/dolt-commit)(1), [dolt-sql](/man/dolt-sql)(1), [git-init](/man/git-init)(1)

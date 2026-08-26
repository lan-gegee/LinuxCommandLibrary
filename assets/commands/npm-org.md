# TAGLINE

管理 npm 组织的成员

# TLDR

**列出组织成员**

```npm org ls [org-name]```

**向组织添加成员**

```npm org set [org-name] [username] [developer]```

**移除成员**

```npm org rm [org-name] [username]```

# SYNOPSIS

**npm** **org** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 组织管理子命令。

**ls** _ORG_
> 列出成员。

**set** _ORG_ _USER_ _ROLE_
> 添加/更新成员。

**rm** _ORG_ _USER_
> 移除成员。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm org** 管理 npm 组织的成员，控制对带作用域软件包的访问。

该命令用于管理组织团队，需要组织管理员权限。

# CAVEATS

需要 npm 组织。需要管理员权限。属于付费功能。

# HISTORY

npm org 为共享带作用域软件包的团队提供**组织管理**功能。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-team](/man/npm-team)(1), [npm-access](/man/npm-access)(1)

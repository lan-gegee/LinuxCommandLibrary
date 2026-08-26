# TAGLINE

管理组织团队

# TLDR

**列出团队**

```npm team ls [@org]```

**创建团队**

```npm team create [@org:team]```

**销毁团队**

```npm team destroy [@org:team]```

**将用户添加到团队**

```npm team add [@org:team] [user]```

**从团队中移除用户**

```npm team rm [@org:team] [user]```

# SYNOPSIS

**npm** **team** [_command_] [_options_]

# PARAMETERS

**ls** _@org_ | _@org:team_
> 列出组织中的团队，或某个特定团队的成员。

**create** _@org:team_
> 在给定的组织作用域下创建新团队。

**destroy** _@org:team_
> 删除一个已存在的团队（developers 团队无法删除）。

**add** _@org:team_ _user_
> 将用户添加到给定团队。

**rm** _@org:team_ _user_
> 从给定团队中移除用户。

**--otp** _code_
> 提供双因素认证的一次性密码。

**--registry** _url_
> 目标 registry 的 URL（默认为 https://registry.npmjs.org）。

**--parseable**
> 以制表符分隔的可解析格式输出。

**--json**
> 以 JSON 格式输出结果。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm team** 用于管理组织团队，控制软件包的访问组。

该命令处理团队成员关系，是 npm organizations 功能的一部分。

# CAVEATS

需要组织账户。需要管理员权限。为付费功能。

# HISTORY

npm team 为 npm 组织的软件包提供**基于团队的访问控制**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-org](/man/npm-org)(1), [npm-access](/man/npm-access)(1)

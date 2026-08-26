# TAGLINE

管理 npm registry 上已发布软件包的访问级别

# TLDR

**将软件包设为公开**

```npm access public [package]```

**将软件包设为受限**

```npm access restricted [package]```

**授予只读权限**

```npm access grant read-only [scope:team] [package]```

**授予读写权限**

```npm access grant read-write [scope:team] [package]```

**撤销权限**

```npm access revoke [scope:team] [package]```

**列出软件包权限**

```npm access ls-packages [scope:team]```

# SYNOPSIS

**npm access** _command_ [_options_]

# PARAMETERS

**public**
> 将软件包设为公开。

**restricted**
> 将软件包设为私有。

**grant** _level_
> 授予团队访问权限。

**revoke**
> 移除团队访问权限。

**ls-packages**
> 列出用户/团队的软件包。

**ls-collaborators**
> 列出软件包的协作者。

# DESCRIPTION

**npm access** 管理 npm registry 上已发布软件包的访问级别。它控制软件包是公开还是私有，并管理团队权限。

该命令与 npm 组织和带作用域（scoped）的软件包相关。
# Make scoped package public
npm access public @myorg/mypackage

# Grant team access
npm access grant read-write @myorg:developers @myorg/mypackage

# List collaborators
npm access ls-collaborators @myorg/mypackage
```

# CAVEATS

需要身份验证。私有软件包需要付费 npm 账户。带作用域的软件包默认为受限。

# HISTORY

npm access 的加入是为了支持 npm Organizations 和私有软件包，实现基于团队的访问控制。

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1), [npm-owner](/man/npm-owner)(1)

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# TAGLINE

显示已登录的用户名

# TLDR

**显示当前用户**

```npm whoami```

**检查指定的 registry**

```npm whoami --registry=[https://registry.example.com]```

# SYNOPSIS

**npm** **whoami** [_options_]

# PARAMETERS

**--registry** _URL_
> 要检查的 registry。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm whoami** 显示已登录的用户名，用于验证身份认证状态。

该命令显示当前用户，可用于调试认证问题。

# CAVEATS

需要身份验证。按 registry 分别检查。未登录时结果为空。

# HISTORY

npm whoami 为访问 npm registry 提供**身份验证检查**功能。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-login](/man/npm-login)(1), [npm-logout](/man/npm-logout)(1)

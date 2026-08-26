# TAGLINE

在 npm registry 中创建或验证用户账户

# TLDR

**登录 npm registry**

```npm adduser```

**登录指定的 registry**

```npm adduser --registry [https://registry.example.com]```

**使用指定作用域登录**

```npm adduser --scope @[myorg]```

# SYNOPSIS

**npm** **adduser** [_options_]

# PARAMETERS

**--registry** _url_
> 用于身份验证的 registry。

**--scope** _scope_
> 关联的作用域。

**--auth-type** _type_
> 身份验证类型。

# DESCRIPTION

**npm adduser** 在 npm registry 中创建或验证用户账户。会提示输入用户名、密码和电子邮箱，并将凭据存储在 ~/.npmrc 中。它是 npm login 的别名。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-logout](/man/npm-logout)(1)

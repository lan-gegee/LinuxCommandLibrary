# TAGLINE

移除身份验证令牌

# TLDR

**从 npm 登出**

```npm logout```

**从指定的 registry 登出**

```npm logout --registry=[https://registry.example.com]```

**从作用域登出**

```npm logout --scope=[@myorg]```

# SYNOPSIS

**npm** **logout** [_options_]

# PARAMETERS

**--registry** _URL_
> 要登出的 registry。

**--scope** _SCOPE_
> 带作用域的 registry。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm logout** 会使命牌失效并将其从所配置的 registry 中移除。对于由 **npm login** 签发的令牌，还会通知 registry 在服务端撤销该令牌，随后删除本地 **.npmrc** 中对应 registry 的条目。

如果所配置的身份验证是旧式用户名/密码（basic auth），则只会移除本地凭据——服务端没有需要撤销的内容。

# CAVEATS

一次只作用于一个 registry；要登出非默认的 registry，请传入 **--registry** 或 **--scope**。重新登录之前，后续的 **npm publish** 或私有软件包 **npm install** 都会失败。手动写入 **.npmrc**（例如 `_authToken=...`）且没有对应服务端凭据的令牌会被本地移除，但无法在服务端撤销。

# HISTORY

npm logout 为访问 npm registry 提供**身份验证管理**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-login](/man/npm-login)(1), [npm-whoami](/man/npm-whoami)(1)

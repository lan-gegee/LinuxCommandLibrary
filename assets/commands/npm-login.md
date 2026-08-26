# TAGLINE

向 npm registry 进行身份验证

# TLDR

**登录 npm registry**

```npm login```

**登录指定的 registry**

```npm login --registry=[https://registry.example.com]```

**带作用域登录**

```npm login --scope=@[myorg]```

**检查登录状态**

```npm whoami```

**登出**

```npm logout```

# SYNOPSIS

**npm login** [_options_]

# PARAMETERS

**--registry** _url_
> registry 的 URL。

**--scope** _scope_
> 将登录与作用域关联。

**--auth-type** _type_
> 身份验证类型（legacy、web）。

# DESCRIPTION

**npm login**（也叫 npm adduser）向 npm registry 进行身份验证。凭据存储在 ~/.npmrc 中，用于发布软件包和访问私有软件包。

对于 npmjs.com，登录后即可发布软件包并访问组织的私有软件包。命令 `npm adduser` 是 `npm login` 的别名。

# AUTHENTICATION FLOW

```bash
# Standard login
npm login
# Enter username, password, email, OTP if enabled

# Verify
npm whoami
# Output: your-username

# View token
npm token list
```

# NPMRC LOCATIONS

```
~/.npmrc           # User config
./.npmrc           # Project config
/etc/npmrc         # Global config
```

# CAVEATS

令牌以明文形式存储在 .npmrc 中。请使用 npm token 管理令牌。可能需要启用两步验证（2FA）。

# HISTORY

npm login 自 npm 早期版本起就是其组成部分，并逐步演进以支持 2FA 和多个 registry。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1), [npm-whoami](/man/npm-whoami)(1), [npm-token](/man/npm-token)(1), [npm-logout](/man/npm-logout)(1)

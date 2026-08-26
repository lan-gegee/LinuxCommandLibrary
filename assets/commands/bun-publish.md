# TAGLINE

发布软件包到 npm 软件仓库

# TLDR

**发布软件包**到 npm 软件仓库

```bun publish```

**使用特定标签发布**

```bun publish --tag [beta]```

**以公开访问权限发布**（带作用域的软件包）

```bun publish --access public```

**试运行**而不实际发布

```bun publish --dry-run```

# SYNOPSIS

**bun** **publish** [_options_]

# PARAMETERS

**--tag** _tag_
> 使用特定的 dist-tag 发布（默认：latest）。

**--access** _public|restricted_
> 设置带作用域软件包的访问级别。

**--dry-run**
> 显示将要发布的内容，而不实际发布。

**--otp** _code_
> 用于双因素认证（2FA）的一次性密码。

# DESCRIPTION

**bun publish** 将当前软件包发布到 npm 软件仓库。它从 package.json 读取软件包配置并上传软件包 tarball。

发布前，请确保你已通过 **bun login** 登录或已配置好相应的凭据。

# CAVEATS

需要 npm 软件仓库的身份验证。带作用域的软件包（@org/name）默认为私有；公开的作用域软件包请使用 **--access public**。

# SEE ALSO

[bun](/man/bun)(1), [npm-publish](/man/npm-publish)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->

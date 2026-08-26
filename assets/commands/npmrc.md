# TAGLINE

设置 registry

# TLDR

**设置 registry**

```registry=https://registry.npmjs.org/```

**设置认证令牌**

```//registry.npmjs.org/:_authToken=[token]```

**设置作用域 registry**

```@myorg:registry=https://npm.myorg.com/```

**保存精确版本号**

```save-exact=true```

**设置默认许可证**

```init-license=MIT```

# SYNOPSIS

**.npmrc** - npm 配置文件

# PARAMETERS

**registry**
> 默认的 registry URL。

**save-exact**
> 保存精确版本号。

**save-prefix**
> 版本前缀（^、~）。

**init-author-name**
> 默认作者。

**init-license**
> 默认许可证。

**//registry/:_authToken**
> registry 认证令牌。

**@scope:registry**
> 特定作用域使用的 registry。

# DESCRIPTION

**.npmrc** 文件用于配置 npm 的行为。它可以存在于项目级、用户级（~/.npmrc）或全局级。配置按层级级联生效，项目级配置优先。

# FILE LOCATIONS

```
/path/to/project/.npmrc  # Project
~/.npmrc                  # User
$PREFIX/etc/npmrc         # Global
/etc/npmrc                # Built-in
```

# EXAMPLE CONFIG

```ini
# .npmrc
registry=https://registry.npmjs.org/
save-exact=true
@myorg:registry=https://npm.myorg.com/
//npm.myorg.com/:_authToken=${NPM_TOKEN}
```

# CAVEATS

不要提交认证令牌。机密信息请使用环境变量。项目的 .npmrc 会覆盖用户级配置。

# SEE ALSO

[npm](/man/npm)(1), [npm-config](/man/npm-config)(1), [npm-login](/man/npm-login)(1)

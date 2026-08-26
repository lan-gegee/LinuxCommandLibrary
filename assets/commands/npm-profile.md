# TAGLINE

管理 npm registry 上的用户资料

# TLDR

**显示全部资料**属性

```npm profile get```

**获取某个特定**的资料属性（如 email、fullname、homepage）

```npm profile get [property]```

**设置资料字段**（email、fullname、homepage、twitter、github）

```npm profile set [field] [value]```

**修改密码**（交互式提示）

```npm profile set password```

**启用两步验证**（默认为 auth-and-writes）

```npm profile enable-2fa [auth-only|auth-and-writes]```

**禁用两步验证**

```npm profile disable-2fa```

**以 JSON 格式输出**

```npm profile get --json```

# SYNOPSIS

**npm profile enable-2fa** [_auth-only_|_auth-and-writes_]

**npm profile disable-2fa**

**npm profile get** [_key_]

**npm profile set** _key_ _value_

# PARAMETERS

**get** [_property_]
> 显示所有资料属性或某一个特定属性。

**set** _property_ _value_
> 设置资料属性。支持：email、fullname、homepage、freenode、twitter、github。

**set password**
> 以交互方式更改账户密码。

**enable-2fa** [_mode_]
> 启用两步验证。模式为 `auth-only`（仅登录/认证变更）或 `auth-and-writes`（还包括发布、dist-tag、权限变更）。默认为 `auth-and-writes`。

**disable-2fa**
> 禁用两步验证。

**--registry** _URL_
> 覆盖 registry URL（默认 https://registry.npmjs.org/）。

**--otp** _CODE_
> 为受 2FA 保护的操作提供一次性密码。

**--json**
> 以 JSON 格式输出结果。

# DESCRIPTION

**npm profile** 管理你在 npm registry 上的用户资料。它可以查看和更新资料设置（email、fullname、homepage、社交账号），以交互方式修改密码，并配置两步验证以保障账户安全。

该命令依赖于具体的 registry 实现；第三方 registry 可能不支持全部子命令。

# CAVEATS

多数子命令只能用于 npmjs.com 或兼容的 registry。该命令不感知工作区。更改邮箱或启用 2FA 时可能会提示输入 OTP。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-adduser](/man/npm-adduser)(1), [npm-access](/man/npm-access)(1), [npm-config](/man/npm-config)(1)

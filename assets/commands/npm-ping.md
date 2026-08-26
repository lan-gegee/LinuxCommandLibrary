# TAGLINE

检查与 npm registry 的连通性

# TLDR

**ping 默认的 npm registry**

```npm ping```

**ping 自定义 registry**

```npm ping --registry [https://registry.example.com]```

# SYNOPSIS

**npm** **ping** [_options_]

# PARAMETERS

**--registry** _url_
> 要 ping 的 registry URL（默认：https://registry.npmjs.org）。

# DESCRIPTION

**npm ping** 会 ping 所配置或指定的 npm registry，并在已配置凭据时一并验证身份验证。成功时输出 registry URL 和响应时间，失败时输出错误。适合诊断 registry 连通性问题、验证自定义 registry 配置以及排查 npm 身份验证问题。

# CAVEATS

需要网络连通。若已配置身份验证，ping 还会验证令牌的有效性。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-config](/man/npm-config)(1)

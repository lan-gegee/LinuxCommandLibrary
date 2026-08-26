# TAGLINE

来自终端的一次性临时邮箱

# TLDR

**生成地址**

```tmpmail -g```

**检查收件箱**

```tmpmail```

**按 ID 阅读邮件**

```tmpmail [email-id]```

**复制地址**

```tmpmail -c```

**更换域名**

```tmpmail -g [domain]```

**最近的邮件**

```tmpmail -r```

# SYNOPSIS

**tmpmail** [_-g_] [_-c_] [_-r_] [_options_] [_id_]

# PARAMETERS

**-g**
> 生成地址。

**-c**
> 复制到剪贴板。

**-r**
> 最近的邮件。

**-b** _BROWSER_
> 用指定的浏览器打开邮件，而不是在终端中以纯文本显示。

**-t**, **--text**
> 强制以文本模式渲染（不在浏览器中打开）。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**tmpmail** 生成一次性的临时邮箱地址，让你可以直接从终端查看其收件箱。它适合注册各种服务时使用，避免将真实邮箱暴露给潜在的垃圾邮件。

该工具在支持的临时邮箱域名上创建地址，并获取收到的邮件以便在终端或浏览器中查看。当前地址可以用 **-c** 复制到剪贴板，方便快速粘贴到注册表单中。

# CAVEATS

依赖外部服务。可能有使用限制。不适合敏感用途。

# HISTORY

**tmpmail** 为生成临时邮箱地址并在命令行中查看它们而创建。

# INSTALL

```brew: brew install tmpmail```

```nix: nix profile install nixpkgs#tmpmail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mail](/man/mail)(1), [mutt](/man/mutt)(1), [curl](/man/curl)(1)

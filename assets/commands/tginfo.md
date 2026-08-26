# TAGLINE

获取 Telegram 用户名或 URL 的信息

# TLDR

**获取 Telegram 用户名的信息**

```tginfo [username]```

**从 Telegram URL 获取信息**

```tginfo https://t.me/[username]```

**仅显示特定属性**

```tginfo [username] --attrs=title,type,subscribers```

**以 JSON 输出**

```tginfo [username] --json```

# SYNOPSIS

**tginfo** _slug/url_ [_options_]

# PARAMETERS

**--attrs**=_ATTR1,ATTR2_
> 仅显示特定属性。

**--json**
> 显示 JSON 而非人类可读的视图。

**--help**
> 打印帮助信息。

**--version**
> 显示版本。

# DESCRIPTION

**tginfo** 是一个零依赖的 Node.js 模块，用于获取 Telegram 用户名或 URL 的信息。它接受 Web URL（https://t.me/username）、深链接（tg://resolve?domain=username）、纯用户名或邀请码。

输出包含 type、title、webUrl、tgUrl 等属性，并根据实体类型可选包含 username、info、verified、image、subscribers、members 和在线人数等字段。

# CAVEATS

需要 Node.js。可通过 `npm install -g tginfo` 全局安装，或用 `npx tginfo` 运行。

# SEE ALSO

[npx](/man/npx)(1), [npm](/man/npm)(1)

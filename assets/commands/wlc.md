# TAGLINE

Weblate 命令行客户端

# TLDR

**列出项目**

```wlc ls```

**查看组件**

```wlc show [project/component]```

**下载翻译**

```wlc download [project/component]```

**上传翻译**

```wlc upload [project/component]```

**提交更改**

```wlc commit [project/component]```

# SYNOPSIS

**wlc** _command_ [_options_] [_args_]

# PARAMETERS

**ls**
> 列出项目。

**show**
> 显示详情。

**download**
> 获取翻译。

**upload**
> 发送翻译。

**commit**
> 提交更改。

**--config** _FILE_
> 配置文件。

# DESCRIPTION

**wlc** 是 Weblate 的命令行客户端。Weblate 是一个开源的基于 Web 的翻译管理系统。该客户端提供对 Weblate API 的访问，可用于管理翻译项目、下载和上传翻译文件，以及从终端提交更改。

该工具支持列出项目和组件、查看翻译状态，以及对多个翻译文件执行批量操作。它需要 Weblate 服务器 URL 和 API 密钥进行身份验证，为方便起见可以将它们保存在配置文件中。

# CAVEATS

需要 Weblate 服务器。必须有 API 密钥。基于 Python。

# HISTORY

**wlc** 是开源翻译管理系统 **Weblate** 的命令行客户端。

# INSTALL

```nix: nix profile install nixpkgs#wlc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[weblate](/man/weblate)(1), [poedit](/man/poedit)(1)

# TAGLINE

Weblate 翻译管理客户端

# TLDR

**列出项目（使用 wlc 客户端）**

```wlc list-projects```

**列出组件**

```wlc list-components [project/component]```

**下载翻译**

```wlc download [project/component/language]```

**上传翻译文件**

```wlc upload [project/component/language] [file.po]```

**锁定组件以进行编辑**

```wlc lock [project/component]```

**推送更改到仓库**

```wlc push [project/component]```

**显示组件统计信息**

```wlc stats [project/component]```

# SYNOPSIS

**wlc** [_options_] _command_ [_arguments_]

# WLC COMMANDS

**list-projects**：列出所有项目。

**list-components**：列出项目中的组件。

**list-translations**：列出翻译。

**show**：显示对象详情。

**download**：下载翻译文件。

**upload**：上传翻译文件。

**lock** / **unlock**：锁定/解锁翻译。

**push** / **pull**：与仓库同步。

**commit**：提交待处理的更改。

**stats**：显示翻译统计信息。

# PARAMETERS

**--url** _url_
> Weblate 服务器 URL。

**--key** _key_
> 用于身份验证的 API 密钥。

**--format** _fmt_
> 输出格式（text、csv、json、html）。

**-o** _file_
> 输出到文件。

# DESCRIPTION

**wlc**（Weblate Client）通过 REST API 远程管理 Weblate 翻译服务器。它支持翻译工作流自动化、持续本地化以及与构建系统的集成。

该客户端处理常见任务：下载/上传翻译、触发仓库同步、发布期间锁定翻译以及查询统计信息。~/.config/weblate 中的配置保存服务器 URL 和 API 密钥。

服务器端管理使用 Django 的 manage.py 或 weblate 脚本执行数据库操作、导入/导出和管理任务。

# CONFIGURATION

**~/.config/weblate**
> 客户端配置，包含用于身份验证的服务器 URL 和 API 密钥。

# CAVEATS

需要 Weblate 服务器的 API 密钥。可能受速率限制。某些操作需要在服务器上具有相应权限。

# HISTORY

**Weblate** 由 Michal Čihař 创建，是一套基于网页的持续本地化系统。wlc 客户端使命令行和脚本方式操作 Weblate 服务器成为可能，支持自动化的翻译工作流。

# INSTALL

```zypper: sudo zypper install weblate```

```nix: nix profile install nixpkgs#weblate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gettext](/man/gettext)(1), [msgfmt](/man/msgfmt)(1), [poedit](/man/poedit)(1)

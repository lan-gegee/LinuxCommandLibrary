# TAGLINE

轻量级终端 RSS 阅读器

# TLDR

**启动 Snownews** RSS 阅读器

```snownews```

从 OPML 文件**导入订阅源**

```snownews --import [path/to/feeds.opml]```

**使用自定义 URL 文件启动**

```snownews --url [path/to/urls]```

启动时**强制更新**所有订阅源

```snownews --update```

# SYNOPSIS

**snownews** [_options_]

# PARAMETERS

**--import** _file_
> 从 OPML 文件导入订阅源列表。

**--url** _file_
> 使用自定义 URL 文件作为订阅源列表。

**--update**
> 启动时更新所有订阅源。

**--charset** _charset_
> 在自动检测失败时强制使用指定字符集。

**--cursor**
> 始终在屏幕上显示光标。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# KEYBINDINGS

**a**
> 添加新的订阅源 URL。

**D**
> 删除高亮显示的订阅源。

**r**
> 重新加载高亮显示的订阅源。

**R**
> 重新加载所有订阅源。

**T**
> 忽略缓存强制刷新。

**n**, **Down**
> 移动到下一项。

**p**, **Up**
> 移动到上一项。

**Enter**
> 打开/阅读高亮显示的条目。

**o**
> 在浏览器中打开 URL。

**q**
> 退出或返回。

**h**
> 显示上下文相关帮助。

# DESCRIPTION

**Snownews** 是一个为文本终端设计的轻量级命令行 RSS 阅读器。它支持 RSS 0.91、1.0（RDF）和 2.0 格式。界面简洁且以键盘操作为主，订阅源以列表形式显示。

Snownews 维护本地缓存以尽量减少网络流量，并支持 HTTP 代理、HTTP 身份验证（basic 和 digest）以及 cookie。订阅源 URL 可以从 OPML 文件导入，方便从其他阅读器迁移。

默认情况下，订阅源中的 URL 使用 Lynx 等文本模式浏览器打开，但可以配置为使用任何浏览器。配置文件存储在 **~/.snownews/** 中，包括 URL 列表和设置。

# CONFIGURATION

**~/.snownews/urls**
> 已订阅的订阅源 URL 列表，每行一个。

**~/.snownews/browser**
> 用于打开订阅源条目中 URL 的脚本或命令。

# CAVEATS

Snownews 仅支持文本模式，不显示订阅源中的图片或复杂排版。默认浏览器是 Lynx；要使用图形浏览器需配置 browser 设置。RSS 1.0 订阅源必须符合 W3C RDF 规范才能正确解析。

# HISTORY

**Snownews** 作为命令行的轻量级 RSS 阅读器开发而成。它的设计目标是与 Unix 工具及其哲学良好契合，支持管道和过滤。该项目以 GNU 通用公共许可证第 3 版发布，支持 Linux、BSD、macOS 和 Windows（通过 Cygwin）等多个平台。

# INSTALL

```dnf: sudo dnf install snownews```

```brew: brew install snownews```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[newsboat](/man/newsboat)(1), [lynx](/man/lynx)(1), [rss2email](/man/rss2email)(1)

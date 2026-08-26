# TAGLINE

适用于 Linux 的 Edge 浏览器

# TLDR

**打开浏览器**

```microsoft-edge```

**打开 URL**

```microsoft-edge [https://example.com]```

**以隐私模式打开**

```microsoft-edge --inprivate```

**打开文件**

```microsoft-edge [file.html]```

**新建窗口**

```microsoft-edge --new-window [url]```

**指定配置目录**

```microsoft-edge --user-data-dir=[/path/to/profile]```

# SYNOPSIS

**microsoft-edge** [_options_] [_url_]

# PARAMETERS

_URL_
> 要打开的 URL。

**--inprivate**
> 隐私浏览模式。

**--new-window**
> 在新窗口中打开。

**--user-data-dir** _DIR_
> 配置目录。

**--app** _URL_
> 以应用模式打开 URL（无工具栏和地址栏）。

**--incognito**
> 某些版本中 **--inprivate** 的别名。

**--proxy-server** _HOST:PORT_
> 使用指定的代理服务器进行连接。

**--disable-extensions**
> 启动时禁用所有扩展。

**--version**
> 显示浏览器版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**microsoft-edge** 是适用于 Linux 的 Microsoft Edge 浏览器。它基于 Chromium。

该工具提供网页浏览功能，并与 Microsoft 服务集成。支持扩展和同步。

# CAVEATS

基于 Chromium。同步需要 Microsoft 账户。专有软件。

# HISTORY

适用于 Linux 的 Microsoft Edge 于 **2020 年**发布，将这款基于 Chromium 的浏览器带到了 Linux 平台。

# INSTALL

```nix: nix profile install nixpkgs#microsoft-edge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[google-chrome](/man/google-chrome)(1), [firefox](/man/firefox)(1), [chromium](/man/chromium)(1)

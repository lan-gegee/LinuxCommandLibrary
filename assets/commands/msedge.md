# TAGLINE

从命令行启动 Microsoft Edge 浏览器

# TLDR

**打开 Microsoft Edge**

```msedge```

**打开 URL**

```msedge [https://example.com]```

**在新窗口中打开**

```msedge --new-window [https://example.com]```

**在无痕模式下打开**

```msedge --inprivate [https://example.com]```

**打开开发者工具**

```msedge --auto-open-devtools-for-tabs [https://example.com]```

# SYNOPSIS

**msedge** [_options_] [_url_...]

# PARAMETERS

**--new-window**
> 在新窗口中打开。

**--inprivate**
> 以 InPrivate 模式打开。

**--profile-directory** _name_
> 使用特定的配置文件。

**--auto-open-devtools-for-tabs**
> 自动打开 DevTools。

**--headless**
> 以无头模式运行。

**--disable-gpu**
> 禁用 GPU 硬件加速。

**--user-data-dir** _path_
> 自定义用户数据目录。

# DESCRIPTION

**msedge** 从命令行启动 Microsoft Edge 浏览器。这是一款基于 Chromium 的浏览器，完全兼容 Chrome 的标志和选项。支持自动化、调试和测试场景。

# SEE ALSO

[google-chrome](/man/google-chrome)(1), [firefox](/man/firefox)(1), [chromium](/man/chromium)(1)

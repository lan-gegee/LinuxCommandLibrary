# TAGLINE

将网页转换为桌面应用

# TLDR

**将 URL 打包为应用**

```pake [https://example.com]```

**以自定义名称打包**

```pake [url] --name [AppName]```

**以自定义图标打包**

```pake [url] --icon [icon.png]```

**为特定平台打包**

```pake [url] --targets [macos|linux|windows]```

# SYNOPSIS

**pake** [_options_] _url_

# PARAMETERS

_URL_
> 要打包的网页 URL。

**--name** _NAME_
> 应用程序名称。

**--icon** _FILE_
> 应用程序图标。

**--targets** _PLATFORMS_
> 构建目标平台。

**--width** _PIXELS_
> 窗口宽度。

**--height** _PIXELS_
> 窗口高度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**pake** 将网页转换为桌面应用。使用 Rust 和系统 WebView 实现。

该工具创建轻量级的原生包装器。支持跨平台。

# CAVEATS

使用 Rust 编写。采用系统 WebView。体积比 Electron 更小。

# HISTORY

Pake 的定位是 Electron 的**轻量级替代方案**，用于打包 Web 应用。

# INSTALL

```brew: brew install pake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[electron](/man/electron)(1), [tauri](/man/tauri)(1), [nativefier](/man/nativefier)(1)

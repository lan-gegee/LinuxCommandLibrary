# TAGLINE

注重隐私的 Firefox 分支，默认安全设置更为严格

# TLDR

**启动 LibreWolf**

```librewolf```

**打开指定 URL**

```librewolf [https://example.com]```

**以隐私浏览模式打开**

```librewolf --private-window```

在新窗口中**打开 URL**

```librewolf --new-window [url]```

在新标签页中**打开 URL**

```librewolf --new-tab [url]```

**使用指定配置档案**

```librewolf -P [profile-name]```

**启动配置档案管理器**

```librewolf --ProfileManager```

以禁用附加组件的**安全模式启动**

```librewolf --safe-mode```

# SYNOPSIS

**librewolf** [_options_] [_url_...]

# PARAMETERS

**--private-window**
> 打开隐私浏览窗口。

**--new-window** _url_
> 在新窗口中打开 URL。

**--new-tab** _url_
> 在新标签页中打开 URL。

**-P** _profile_
> 使用指定的配置档案。

**--ProfileManager**
> 打开配置档案管理器。

**--safe-mode**
> 禁用附加组件启动。

**--headless**
> 无 GUI 运行。

**--search** _term_
> 使用默认搜索引擎进行搜索。

**--screenshot** _file_
> 为 URL 截取屏幕截图（需配合 --headless 使用）。

# DESCRIPTION

**librewolf** 是一款注重隐私的 Firefox 分支，默认安全设置更为严格。它移除了遥测功能，内置 uBlock Origin，并应用了一系列隐私加固配置。它在优先保障用户隐私的同时保持与 Firefox 的兼容性。由于基于 Firefox，它支持所有标准的 Firefox 命令行选项。

# INSTALL

```apk: sudo apk add librewolf```

```nix: nix profile install nixpkgs#librewolf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firefox](/man/firefox)(1)

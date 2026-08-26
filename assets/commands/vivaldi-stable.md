# TAGLINE

可深度定制的基于 Chromium 的网页浏览器（稳定版渠道）

# TLDR

**打开** Vivaldi

```vivaldi-stable```

**打开指定的 URL**

```vivaldi-stable [https://example.com]```

**以指定配置文件打开**

```vivaldi-stable --profile-directory=[test]```

**在新标签页中打开 URL**

```vivaldi-stable --new-tab [https://example.com]```

**以无痕（隐私）模式启动**

```vivaldi-stable --incognito```

**禁用 GPU**（排查问题时有用）

```vivaldi-stable --disable-gpu```

# SYNOPSIS

**vivaldi-stable** [_options_] [_URL_]

# DESCRIPTION

**vivaldi-stable** 是 Vivaldi 浏览器稳定版在 Linux 上的软件包名称。Vivaldi 是一款基于 Chromium、高度可定制的网页浏览器，面向高级用户，提供标签页堆叠、平铺、内置邮件、笔记以及丰富的主题等功能。

由于 Vivaldi 基于 Chromium，它接受大多数 Chromium 命令行开关。用户专属的开关也可以写入 `~/.config/vivaldi-stable.conf` 以持久生效。

# CAVEATS

并非完全开源：UI 层是专有的，而 Chromium 底层是开源的。由于 Vivaldi 的修改，某些 Chromium 特性的行为可能有所不同。

# INSTALL

```pacman: sudo pacman -S vivaldi```

```nix: nix profile install nixpkgs#vivaldi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chromium](/man/chromium)(1), [google-chrome](/man/google-chrome)(1), [firefox](/man/firefox)(1), [brave](/man/brave)(1)

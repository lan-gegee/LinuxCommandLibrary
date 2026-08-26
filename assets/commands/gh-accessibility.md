# TAGLINE

管理 GitHub CLI 的无障碍设置

# TLDR

**显示无障碍指引和设置**

```gh accessibility```

**在浏览器中打开 GitHub Accessibility 网站**

```gh accessibility --web```

**启用无障碍 4 位色板**

```gh config set accessible_colors enabled```

**为屏幕阅读器启用无障碍提示器**

```gh config set accessible_prompter enabled```

**禁用动画加载指示器，改用文本提示**

```gh config set spinner disabled```

# SYNOPSIS

**gh** **accessibility** [_flags_]

# PARAMETERS

**-w**, **--web**
> 在默认网页浏览器中打开 GitHub Accessibility 网站。

**--help**
> 显示命令帮助。

# DESCRIPTION

**gh accessibility** 显示关于 GitHub CLI 无障碍体验及启用方式的指引。它的别名是 **gh a11y**。

该命令描述四个方面的无障碍支持：

**无障碍颜色** — 启用一套基于终端背景（深色或浅色）、对比度更高的 4 位 ANSI 色板。这让用户可以通过自己的终端偏好来自定义颜色。用 `gh config set accessible_colors enabled` 或 `GH_ACCESSIBLE_COLORS` 环境变量启用。

**标签颜色** — 在支持真彩色的终端中按自定义 RGB 十六进制值显示 issue 和 pull request 标签的颜色。用 `gh config set color_labels enabled` 或 `GH_COLOR_LABELS` 环境变量启用。

**无障碍提示器** — 用非交互式的等价形式取代操作光标的交互式提示，使其能与语音合成器和盲文显示器正确配合工作。用 `gh config set accessible_prompter enabled` 或 `GH_ACCESSIBLE_PROMPTER` 环境变量启用。

**纯文本加载指示器** — 用普通文本进度提示取代动画式加载字符，消除可能引起不适或被屏幕阅读器误读的动态效果。用 `gh config set spinner disabled` 或 `GH_SPINNER_DISABLED` 环境变量启用。

# CAVEATS

无障碍功能于 GitHub CLI v2.72.0 作为**公开预览版**引入。各项功能必须通过 `gh config set` 或环境变量显式启用；单独运行 `gh accessibility` 只会显示指引文字。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-config](/man/gh-config)(1), [gh-environment](/man/gh-environment)(1)

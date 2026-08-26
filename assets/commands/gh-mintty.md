# TAGLINE

关于 Windows 上 MinTTY 终端兼容性的 GitHub CLI 帮助主题

# TLDR

**显示 MinTTY 兼容性帮助**

```gh help mintty```

**用 winpty 规避 MinTTY 输入问题**（可能导致 UI 缺陷）

```winpty gh auth login```

# SYNOPSIS

**gh help mintty**

# DESCRIPTION

**gh-mintty** 是 GitHub CLI 的一个帮助主题，介绍 **gh** 与 MinTTY（Git for Windows 自带的默认终端模拟器）之间的已知兼容性问题。MinTTY 缺少完善的伪控制台支持，会导致 **gh** 的交互式提示无法正常工作。

目前有三种变通办法：

1. 重新安装 Git for Windows 并勾选 "Enable experimental support for pseudo consoles"。
2. 在其他终端模拟器（例如 Windows Terminal）中运行 `C:\Program Files\Git\bin\bash.exe`，这样无需 MinTTY 即可使用 Git for Windows 的工具。
3. 在 **gh** 命令前加上 `winpty`（例如 `winpty gh auth login`），但这可能引发 UI 渲染缺陷。

# CAVEATS

仅限 Windows 的主题。`winpty` 变通办法可能引发 UI 缺陷。启用 Git for Windows 中的实验性伪控制台选项是最彻底的解决方式。

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

[gh](/man/gh)(1), [gh-help](/man/gh-help)(1), [gh-config](/man/gh-config)(1)

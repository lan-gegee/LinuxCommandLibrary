# TAGLINE

Inkscape 附带的简易 SVG 查看器

# TLDR

**查看 SVG 文件**

```inkview [file.svg]```

**查看多个文件**

```inkview [file1.svg] [file2.svg]```

**幻灯片模式**

```inkview [*.svg]```

# SYNOPSIS

**inkview** [_options_] _file_...

# PARAMETERS

_FILE_
> 要查看的 SVG 文件。

**-t** _SECONDS_
> 幻灯片计时器间隔。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**inkview** 是 Inkscape 附带的简易 SVG 查看器，在窗口中显示 SVG 文件以便快速预览。

该查看器支持幻灯片模式，可用于展示多个 SVG。它使用 Inkscape 的渲染引擎，确保显示准确。

# CAVEATS

属于 Inkscape 的一部分。交互功能有限，仅有查看功能。

# HISTORY

inkview 作为 **Inkscape** 的轻量级配套 SVG 查看器而创建，用于快速预览文件。

# INSTALL

```apt: sudo apt install inkscape```

```dnf: sudo dnf install inkscape```

```pacman: sudo pacman -S inkscape```

```apk: sudo apk add inkscape-view```

```zypper: sudo zypper install inkscape```

```nix: nix profile install nixpkgs#inkscape```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkscape](/man/inkscape)(1), [eog](/man/eog)(1), [feh](/man/feh)(1), [display](/man/display)(1)

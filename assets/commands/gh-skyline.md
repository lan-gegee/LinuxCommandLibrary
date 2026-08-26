# TAGLINE

生成你 GitHub 贡献历史的 3D 模型

# TLDR

**为当前用户和当前年份生成 skyline**

```gh skyline```

**为特定用户生成 skyline**

```gh skyline --user [username]```

**为特定年份生成 skyline**

```gh skyline --year [2024]```

**为年份区间生成 skyline**

```gh skyline --year [2020]-[2024]```

**生成自加入 GitHub 以来的完整贡献历史**

```gh skyline --full```

**只显示 ASCII 字符画预览，不生成 STL 文件**

```gh skyline --art-only```

**指定自定义输出文件名**

```gh skyline --output [my-skyline.stl]```

**在网页浏览器中打开 GitHub 个人主页**

```gh skyline --web```

# SYNOPSIS

**gh** **skyline** [_options_]

# PARAMETERS

**-u**, **--user** _username_
> 要为其生成 skyline 的 GitHub 用户名。默认为已认证用户。

**-y**, **--year** _year_
> 年份或年份区间（例如 2024 或 2020-2024）。必须介于 2008 与当前年份之间。

**-f**, **--full**
> 从用户加入的年份到当前年份生成完整的贡献图。

**-a**, **--art-only**
> 只显示 ASCII 字符画预览，不生成 STL 文件。

**-o**, **--output** _filename_
> 输出文件名。默认为 {username}-{year}-github-skyline.stl。

**-w**, **--web**
> 在网页浏览器中打开 GitHub 个人主页。

**-d**, **--debug**
> 启用调试日志。

# DESCRIPTION

**gh skyline** 是一个 GitHub CLI 扩展，可将用户的 GitHub 贡献历史生成为 3D STL 模型。它把贡献图变换成天际线（skyline），每一天的贡献表现为高低不一的建筑物。输出是可用于 3D 打印的 STL 文件。

终端中会显示天际线的 ASCII 字符画预览。模型可以为任意 GitHub 用户生成，可以针对特定年份，也可以覆盖用户自加入 GitHub 以来的完整贡献历史。

# INSTALL

```nix: nix profile install nixpkgs#gh-skyline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-extension](/man/gh-extension)(1)

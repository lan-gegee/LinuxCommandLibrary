# TAGLINE

将文件加入暂存列表，待加入当前 Fossil 检出

# TLDR

**添加文件**到暂存列表

```fossil add [file]```

**添加检出树中的所有新文件**

```fossil add .```

**显示将要添加的内容**而不实际添加

```fossil add --dry-run .```

**包含点文件**

```fossil add --dotfiles [path]```

**添加匹配模式的文件并忽略其他文件**

```fossil add --ignore "[*.log,build/*]" [path]```

**撤销当前检出中待处理的添加**

```fossil add --reset```

**添加**名称在 Windows 上被保留的文件

```fossil add --allow-reserved [file]```

# SYNOPSIS

**fossil add** [_options_] _FILE_...

**fossil add --reset** [**-v**] [**-n**]

# PARAMETERS

**--case-sensitive** _BOOL_
> 匹配文件名时覆盖 `case-sensitive` 设置。

**--dotfiles**
> 包含以点开头的文件（隐藏文件）。不加此标志时 fossil 会忽略它们。

**-f**, **--force**
> 不提示直接添加（当文件在通常范围之外时有用）。

**--ignore** _CSG_
> 以逗号分隔的要跳过的未管理文件 glob 模式。覆盖 `ignore-glob` 设置。

**--clean** _CSG_
> 以逗号分隔的在 `clean` 操作中要忽略的文件的 glob 模式。覆盖 `clean-glob` 设置。

**--reset**
> 移除先前用 `fossil add` 暂存的文件的 ADDED 状态（文件仍留在磁盘上，只是不再为下次提交所跟踪）。

**--allow-reserved**
> 允许 Windows 上保留的文件名（`CON`、`NUL`、`COM1` 等）。主要用于跨平台仓库。

**-v**, **--verbose**
> 报告 `--reset` 影响的每个文件。

**-n**, **--dry-run**
> 显示将要发生的变化而不改动仓库。

# DESCRIPTION

**fossil add** 安排一个或多个文件（或目录，递归处理）在下一次 `fossil commit` 时加入仓库。它不会直接写入仓库：已暂存的添加保存在检出元数据中，直到提交为止。

除非另行覆盖，点文件以及匹配配置的 `ignore-glob` 的文件会被跳过。目录参数会被递归遍历。

用 `fossil addremove` 可以一次调用同时暂存新增和缺失的文件；用 `fossil add --reset` 可撤销待处理的添加。

# CAVEATS

`fossil add` 只做暂存——在运行 `fossil commit` 之前，其他克隆看不到任何变化。文件名默认在 Unix 上区分大小写，在 Windows 上不区分；跨平台混用时可通过全局或按仓库设置 `case-sensitive on` 统一。只有在设置 `allow-symlinks on` 时，符号链接才会作为符号链接添加。

# INSTALL

```apt: sudo apt install fossil```

```dnf: sudo dnf install fossil```

```pacman: sudo pacman -S fossil```

```apk: sudo apk add fossil```

```zypper: sudo zypper install fossil```

```brew: brew install fossil```

```nix: nix profile install nixpkgs#fossil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fossil-commit](/man/fossil-commit)(1), [fossil-rm](/man/fossil-rm)(1)

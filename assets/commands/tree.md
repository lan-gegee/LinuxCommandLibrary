# TAGLINE

以树状格式显示目录内容

# TLDR

显示目录树

```tree```

显示特定目录的树

```tree [path/to/directory]```

包含隐藏文件

```tree -a```

仅显示目录

```tree -d```

限制树的深度

```tree -L [2]```

显示文件大小

```tree -s```

以人类可读格式显示大小

```tree -h```

输出为 JSON 格式

```tree -J```

排除匹配的模式

```tree -I "[pattern|pattern2]"```

显示每个文件的完整路径

```tree -f```

按修改时间**排序**，最新的在前

```tree -t -r```

**显示目录大小并遵循 .gitignore**

```tree --du --gitignore```

# SYNOPSIS

**tree** [_options_] [_directory_...]

# PARAMETERS

**-a**
> 显示所有文件，包括隐藏文件

**-d**
> 仅列出目录

**-L** _level_
> 将深度限制到指定层级

**-f**
> 打印完整路径前缀

**-s**
> 打印每个文件的大小

**-h**
> 以人类可读格式打印大小

**-D**
> 打印最后修改日期

**-p**
> 打印文件权限

**-u**
> 打印用户名

**-g**
> 打印组名

**-I** _pattern_
> 排除匹配模式的文件

**-P** _pattern_
> 仅列出匹配模式的文件

**--dirsfirst**
> 目录排在文件之前

**-C**
> 彩色化输出

**-n**
> 关闭彩色化

**-r**
> 以逆序排列输出

**-t**
> 按最后修改时间排序

**-o** _filename_
> 将输出发送到指定文件

**--du**
> 显示目录的累计大小

**--prune**
> 从输出中剪除空目录

**--gitignore**
> 使用 .gitignore 文件进行过滤

**--noreport**
> 省略列表末尾的文件和目录计数

**--filelimit** _N_
> 不进入条目数超过 N 的目录

**-H** _baseHREF_
> 输出带基础 URL 的 HTML

**-J**
> 输出 JSON

**-X**
> 输出 XML

# DESCRIPTION

**tree** 以树状格式显示目录内容，直观呈现文件与子目录之间的层次关系。

默认输出使用 ASCII 或 Unicode 制表线字符表示树结构。彩色化有助于区分文件类型（目录、可执行文件、符号链接等）。

它支持多种输出格式以便与其他工具集成：JSON（**-J**）用于程序解析，XML（**-X**）用于结构化数据，HTML（**-H**）用于网页展示。

使用 **-I**（排除）和 **-P**（包含）过滤时采用 shell 通配符模式，支持 \* 和 ? 等通配符。

# CAVEATS

大目录可能产生海量输出。浏览陌生结构时，请用 **-L** 限制深度或用 **-d** 只显示目录。

若符号链接会导致递归，tree 默认不跟随它们。使用 **-l** 可跟随所有符号链接。

同时使用 **--prune** 和 **--du** 会让 tree 在输出前将整棵树累积在内存中，对于非常大的目录树可能较慢。

# INSTALL

```apt: sudo apt install tree```

```dnf: sudo dnf install tree```

```pacman: sudo pacman -S tree```

```apk: sudo apk add tree```

```zypper: sudo zypper install tree```

```brew: brew install tree```

```nix: nix profile install nixpkgs#tree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [find](/man/find)(1), [du](/man/du)(1), [exa](/man/exa)(1), [eza](/man/eza)(1), [lsd](/man/lsd)(1)

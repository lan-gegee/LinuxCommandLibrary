# TAGLINE

文本模式的磁盘用量矩形树图可视化工具

# TLDR

扫描**当前目录**

```leaves```

扫描某个**路径**

```leaves ~/Documents```

包含**隐藏**和被忽略的文件

```leaves -A /var```

扫描根目录并**排除**虚拟文件系统

```leaves -A -d 3 / '!/proc' '!/tmp' '!/run' '!/sys' '!/dev'```

以 **x-ray** 模式打开（先按文件类型分组）

```leaves -x ~/Projects```

# SYNOPSIS

**leaves** [_OPTIONS_] [_PATH_] [_OVERRIDES_...]

# PARAMETERS

**PATH**
> 要扫描的根路径（默认：当前目录）

**OVERRIDES**
> Git 风格的 glob 规则；加 **!** 前缀表示排除

**-d**, **--max-depth** _n_
> 内存中保留的最大深度；更深的子树变成汇总节点（默认 5）

**-x**, **--xray**
> 顶层先按类型对文件分组，再按目录拆分

**-A**, **--include-all**
> 不自动跳过任何文件；只有 override 规则会生效

**-H**, **--include-hidden**
> 包含隐藏文件和文件夹

**-I**, **--include-ignored**
> 包含匹配 **.ignore** 规则的文件

**-G**, **--include-gitignored**
> 包含匹配 **.gitignore** 规则的文件

**-E**, **--include-gitexcluded**
> 包含列于 **.git/info/exclude** 的文件

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本信息

# DESCRIPTION

**leaves** 是一个受 WinDirStat 和 QDirStat 启发的终端磁盘用量分析器。扫描完目录树后，它会绘制嵌套矩形的树图，面积与大小成正比，因此在 SSH 会话或没有 GUI 工具的无头系统上，大文件和大目录一眼就能辨认出来。

其界面将可折叠的资源管理器侧边栏与中央树图结合在一起。文件按扩展名着色，目录按名称着色。键盘和鼠标导航支持聚焦进入目录、展开或收起细节，以及切换 x-ray 模式（先按文件类型分组）。深度汇总功能会将较小或较深的条目归组，即使面对数百万个文件依然保持可用。

默认情况下，隐藏路径以及 **.gitignore** / **.ignore** 规则匹配的内容会被跳过。符号链接不会被跟随（它们不增加本地磁盘占用）。硬链接不会去重，可能被重复计数。

# CONFIGURATION

Leaves 读取 **$XDG_CONFIG_HOME/leaves/setings.toml**（Linux 上通常是 **~/.config/leaves/setings.toml**；注意项目本身的拼写就是这样）。大多数设置也可以通过 **LEAVES_** 环境变量来设置。

**dark_mode**（true/false）— 为深色终端使用更亮的配色（**LEAVES_DARK_MODE**）

**color_shift**（0.0–1.0）— 调亮或调暗调色板（**LEAVES_COLOR_SHIFT**）

**colors** — 主题名称：fall、spring、greys、mono 或自定义主题（**LEAVES_COLORS**）

**dir_style** — 目录边框采用粗线或普通线条（**LEAVES_DIR_STYLE**）

自定义主题可以定义 **dirs** 和 **files** 颜色数组（十六进制、命名色、rgb/hsl）。

# CAVEATS

基于字符单元格的树图比 GUI 工具粗糙；由于边框要占用单元格，深层嵌套条目的面积相对于顶层同级条目会被低估。扫描 **/** 时若不排除 **/proc**、**/sys**、**/dev** 等虚拟文件系统，会产生误导性的大小数据。把 **--max-depth** 设得过深会把更多树结构载入内存，还可能拖慢模式切换。

# HISTORY

**leaves** 是 **patonw** 开发的 Rust TUI 项目，以自由软件形式发布，采用 MPL-2.0 许可证。

# SEE ALSO

[ncdu](/man/ncdu)(1), [du](/man/du)(1), [df](/man/df)(1), [tree](/man/tree)(1)

# RESOURCES

```[Source code](https://github.com/patonw/leaves)```

<!-- verified: 2026-07-16 -->

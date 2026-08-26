# TAGLINE

自定义 less 的按键绑定

# TLDR

**编译**默认的按键绑定源文件

```lesskey```

**编译**指定的按键绑定文件

```lesskey [path/to/lesskey_file]```

使用自定义输出文件进行**编译**

```lesskey -o [path/to/output] [path/to/lesskey_file]```

**打印**版本号

```lesskey -V```

# SYNOPSIS

**lesskey** [**-o** _output_] [**--**] [_input_]

# PARAMETERS

**-o** _file_, **--output=**_file_
> 为编译生成的二进制按键绑定文件指定输出路径。默认为 **~/.less**

**-V**, **--version**
> 显示 lesskey 的版本号

**--**
> 表示选项到此结束；当输入文件名以连字符开头时很有用

# DESCRIPTION

**lesskey** 用于为 **less** 分页器指定或自定义按键绑定。它读取包含按键绑定定义的源文件，并将其编译成二进制文件，供 less 在启动时读取。默认输入文件为 **~/.lesskey**，默认输出文件为 **~/.less**。

lesskey 源文件最多可包含四个小节，每节由一行头部引入：**#command** 定义按键绑定，**#line-edit** 定义搜索提示处的编辑行为，**#env** 设置环境变量，**#stop** 标记文件结束。

在 **#command** 小节中，每行将一个按键序列映射到一个 less 动作。按键可以写成字面字符、控制字符（**^X**）、转义序列（**\e**），或者特殊键，如方向键（**\ku**、**\kd**、**\kr**、**\kl**）、翻页键（**\kU**、**\kD**）、Home（**\kh**）、End（**\ke**）和 Delete（**\kx**）。

**#line-edit** 小节控制搜索和命令提示符下的行为，可用动作包括 **forw-complete**、**back-complete**、**delete**、**backspace**、**home**、**end**、**up**、**down** 和 **abort** 等。

**#env** 小节设置 less 启动时可见的环境变量，例如设置默认选项的 **LESS** 和配置字符集的 **LESSCHARSET**。

# CONFIGURATION

lesskey 源文件采用简单的文本格式。**~/.lesskey** 示例：

```
#command
j      forw-line
k      back-line
\kd    forw-line
\ku    back-line
gg     goto-line
G      goto-end
q      quit

#line-edit
^A     home
^E     end
^U     abort

#env
LESS = -i -M -R
```

**#command** 小节可用的动作包括 **forw-line**、**back-line**、**forw-screen**、**back-screen**、**forw-scroll**、**back-scroll**、**goto-line**、**goto-end**、**repaint**、**quit**、**search** 等等。使用 **invalid** 动作可以显式取消某个按键的定义。

# CAVEATS

在 **less 583 版**及之后的版本中，less 可以直接读取 **~/.lesskey** 源文件，无需再经 lesskey 编译。在现代版本中，lesskey 可执行程序已被视为**弃用**，但仍随附分发。如果 **~/.lesskey**（源文件）和 **~/.less**（编译结果）同时存在，新版 less 会优先使用源文件。编译后的二进制格式在不同架构或不同 less 版本之间不可移植。**#env** 小节可以设置会执行外部命令的 **LESSOPEN** 和 **LESSCLOSE**，因此对来自不受信任来源的 lesskey 文件务必谨慎对待。

# HISTORY

**lesskey** 由 **Mark Nudelman** 创建，是他自 **1983 年**起开发的 **less** 分页器的配套工具。早期 less 必须依赖编译好的二进制按键绑定文件，因为当时认为启动阶段解析文本文件太慢。从 less **583 版**（约 2021 年）起，less 具备了直接读取 lesskey 源文件的能力，使这一编译步骤变成可选。

# INSTALL

```apt: sudo apt install less```

```dnf: sudo dnf install less```

```pacman: sudo pacman -S less```

```apk: sudo apk add less```

```zypper: sudo zypper install less```

```brew: brew install less```

```nix: nix profile install nixpkgs#less```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [more](/man/more)(1)

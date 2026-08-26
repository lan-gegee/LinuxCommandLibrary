# TAGLINE

面向 C、C++ 和 Java 的源码浏览工具

# TLDR

为当前目录**构建数据库**

```cscope -b```

**启动交互模式**

```cscope```

从子目录**递归构建数据库**

```cscope -bR```

基于指定文件**构建数据库**

```cscope -b -i [cscope.files]```

**搜索符号**

```cscope -L0 [symbol]```

**查找函数定义**

```cscope -L1 [function]```

**查找调用某函数的函数**

```cscope -L3 [function]```

# SYNOPSIS

**cscope** [_options_] [_files_]

# DESCRIPTION

**cscope** 是一个面向 C、C++ 和 Java 的源码浏览工具。它会建立符号、函数定义和引用的数据库，从而在大规模代码库中实现快速导航。

交互界面可以搜索符号定义、函数的调用者与被调用者、文本字符串以及文件包含关系。它能与 vim、emacs 等编辑器集成，实现流畅的代码导航。

# PARAMETERS

**-b**
> 只构建交叉引用数据库，不进入交互界面。

**-R**
> 搜索源文件时递归进入子目录。

**-q**
> 构建倒排索引以加快符号搜索（会生成 cscope.in.out 和 cscope.po.out）。

**-C**
> 搜索时忽略大小写。

**-u**
> 无条件重建交叉引用（假定所有文件都已更改）。

**-d**
> 不更新交叉引用数据库。

**-i** _file_
> 从 _file_ 读取源文件名列表，而不是默认的 cscope.files。

**-s** _dir_
> 在 _dir_ 中查找额外的源文件。

**-I** _incdir_
> 在标准系统 include 目录之前先在 _incdir_ 中查找 `#include` 文件。

**-f** _reffile_
> 用 _reffile_ 作为交叉引用文件名，而不是默认的 cscope.out。

**-L** _n_ _pattern_
> 面向行的单次搜索。_n_ 是搜索类型编号（0–9）。输出匹配结果后退出。

**-p** _n_
> 列表条目中显示路径的最后 _n_ 个部分（默认 1）。

**-T**
> 匹配 C 符号时只使用前八个字符。

**-V**
> 打印 cscope 版本号。

# CONFIGURATION

**cscope.files**
> 要纳入数据库的源文件列表（每行一个路径）。

**cscope.out**
> cscope 生成的默认交叉引用数据库文件。

# SEARCH TYPES

**0**: 查找此 C 符号
**1**: 查找此全局定义
**2**: 查找此函数调用的函数
**3**: 查找调用此函数的函数
**4**: 查找此文本字符串
**5**: 替换此文本字符串
**6**: 查找匹配此 egrep 模式的内容
**7**: 查找此文件
**8**: 查找 #include 此文件的文件
**9**: 查找对此符号的赋值

# CAVEATS

代码更改后需要重建数据库（除非使用 `-q` 增量模式）。对 C 风格语言效果最佳。大型代码库的初始索引可能较慢。某些现代 C/C++ 特性可能让解析器出错。

# HISTORY

**cscope** 由 **Joe Steffen** 于 20 世纪 70 年代末在 **贝尔实验室** 开发，作为 AT&T Programmer's Workbench 的一部分分发。2000 年由 SCO 以开源形式发布，现由 SourceForge 维护。它凭借出色的速度和与 vim 的紧密集成而至今广受欢迎。

# INSTALL

```apt: sudo apt install cscope```

```dnf: sudo dnf install cscope```

```pacman: sudo pacman -S cscope```

```zypper: sudo zypper install cscope```

```brew: brew install cscope```

```nix: nix profile install nixpkgs#cscope```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ctags](/man/ctags)(1), [vim](/man/vim)(1), [grep](/man/grep)(1)

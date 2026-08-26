# TAGLINE

用于化学结构图的 groff 预处理器

# TLDR

**处理 chem 文件并查看输出**

```chem [path/to/file.chem] | groffer```

**处理并转换为 PostScript**

```chem [path/to/file.chem] | groff -p -Tps > [output.ps]```

**从 stdin 处理**

```echo '.cstart\nCH3\nbond\nCH3\n.cend' | chem | groffer```

**显示版本信息**

```chem --version```

# SYNOPSIS

**chem** [_option..._] [**--**] [_filespec..._]

**chem** **-h** | **--help**

**chem** **-v** | **--version**

# DESCRIPTION

**chem** 是一个用于绘制化学结构图的 groff 预处理器。它将化学记号转换为 **pic** 语言图形，随后交由 groff 处理渲染。

该工具最适合有机化学，支持化学键、环、基团（如 CH3、NH3）和字符串。化学图需置于 **.cstart** 和 **.cend** 标记之间。

**输入示例：**
```
.cstart
CH3
bond
CH3
.cend
```

由于 chem 是 pic 预处理器，因此可以在图中嵌入原始 pic 语句来进行自定义绘图。

# PARAMETERS

**-h, --help**
> 显示用法信息并退出

**-v, --version**
> 显示版本信息并退出

**filespec**
> 输入文件或表示 stdin 的 **-**。不带参数时读取 stdin

# CAVEATS

没有库或文件包含机制。没有针对重复结构的简写方式。扩展机制使用 pic 宏，要正确实现可能比较棘手。

没有行内化学语法（类似 eqn 的 $...$ 结构），也无法控制基团上的化学键接入点。

# HISTORY

GNU 版本的 **chem** 由 **Bernd Warken** 依据 Brian Kernighan 原始 awk 版本的文档编写而成。这种化学结构图语言是在贝尔实验室开发的，与 **eqn**、**pic** 等 troff 预处理器同期诞生。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [pic](/man/pic)(1), [eqn](/man/eqn)(1), [groffer](/man/groffer)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

<!-- verified: 2026-06-22 -->

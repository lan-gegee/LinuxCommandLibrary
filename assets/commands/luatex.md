# TAGLINE

内嵌 Lua 脚本的增强版 TeX 引擎

# TLDR

**编译 LaTeX 文档**

```luatex [document.tex]```

**编译 LuaLaTeX 文档**

```lualatex [document.tex]```

**启用 shell 转义编译**

```luatex --shell-escape [document.tex]```

**编译为 DVI**

```luatex --output-format=dvi [document.tex]```

**指定输出目录**

```luatex --output-directory=[dir] [document.tex]```

# SYNOPSIS

**luatex** [_options_] [_file_]

# PARAMETERS

**--fmt** _format_
> 要使用的格式文件。

**--output-format** _fmt_
> pdf 或 dvi。

**--output-directory** _dir_
> 输出目录。

**--shell-escape**
> 启用 shell 命令。

**--interaction** _mode_
> 设置交互模式：batchmode、nonstopmode、scrollmode 或 errorstopmode。

**--halt-on-error**
> 在第一个错误处停止。

**--lua** _file_
> Lua 初始化文件。若提供此选项，LuaTeX 会进入另一种命令行解析模式。

**--luaonly**
> 将 LuaTeX 仅作为 Lua 解释器而非 TeX 引擎启动。

**--safer**
> 禁用可能被恶意文档滥用的 Lua 命令。

**--nosocket**
> 禁用 luasocket（网络）库。

**--synctex** _NUMBER_
> 启用/禁用用于源码与 PDF 同步的 SyncTeX 扩展。

**--jobname** _STRING_
> 将作业名设置为 STRING。

**--draftmode**
> 跳过 PDF 输出和图片读取以加快编译。

# DESCRIPTION

**LuaTeX** 是 pdfTeX 的增强版本，具有 Unicode 和 OpenType 字体支持、嵌入的 Lua 脚本、e-TeX 和 Omega 扩展，以及集成的 MetaPost 引擎。它可以生成 PDF 和 DVI 两种输出。该引擎将 TeX 的排版能力与 Lua 编程相结合，支持动态文档生成和高级定制。

LuaLaTeX 是 LuaTeX 的 LaTeX 格式，通常用作 pdfLaTeX 的现代替代品。LuaTeX 还可以以 **texlua**（带 TeX 相关库的 Lua 解释器）或 **texluac**（Lua 字节码编译器）的形式调用。

# LUA IN DOCUMENTS

```latex
\directlua{
  tex.print("Hello from Lua!")
  for i=1,5 do
    tex.print(i)
  end
}
```

# CAVEATS

对简单文档而言比 pdfLaTeX 慢。部分宏包需要针对 LuaTeX 引擎进行适配。内存占用高于其他 TeX 引擎。原生支持 Unicode（UTF-8 输入）。

# HISTORY

LuaTeX 开发始于 **2007 年**，由 **Taco Hoekwater**、**Hartmut Henkel** 和 **Hans Hagen** 发起，作为具备脚本能力的 pdfTeX 后继者。

# INSTALL

```apt: sudo apt install texlive-binaries```

```dnf: sudo dnf install texlive-luatex```

```pacman: sudo pacman -S texlive-luatex```

```apk: sudo apk add texlive-luatex```

```zypper: sudo zypper install texlive-luatex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lualatex](/man/lualatex)(1), [pdftex](/man/pdftex)(1), [pdflatex](/man/pdflatex)(1), [xelatex](/man/xelatex)(1), [tex](/man/tex)(1)

# TAGLINE

从 PPD 打印机文件生成 HTML

# TLDR

**将 PPD 转换为 HTML**

```ppdhtml [file.ppd] > [output.html]```

**转换多个文件**

```ppdhtml [file1.ppd] [file2.ppd]```

# SYNOPSIS

**ppdhtml** [_options_] _file_

# PARAMETERS

_FILE_
> 一个或多个要渲染的 PPD 源文件（`.drv` / `.ppd`）。

**-D** _NAME=VALUE_
> 为 PPD 编译器定义一个变量（透传给 `ppdc`）。

**-I** _DIR_
> 向包含搜索路径添加目录。

# DESCRIPTION

**ppdhtml** 读取 PPD 或 PPD 编译器（`.drv`）源文件，并向标准输出写入一份人类可读的 HTML 摘要。生成的页面记录了打印机的选项组、UI 约束、纸张尺寸、分辨率以及其他 PPD 属性。

它最常见的用途是在编写打印机驱动时作为 CUPS DDK 工具链的一部分——与 **ppdc** 编译成可安装 PPD 的是同一批源文件。

# CAVEATS

输出只写到 stdout——没有 `-o` 标志；请用 `> output.html` 重定向。提供 `ppdhtml`、`ppdc`、`ppdi`、`ppdmerge`、`ppdpo` 的 CUPS DDK 已在上游被弃用（CUPS 2.x），可能需要单独安装软件包（例如 Debian/Ubuntu 上的 `cups-ppdc`）。

# HISTORY

ppdhtml 是 **CUPS** 的组成部分，用于生成 PPD 文档。

# INSTALL

```apt: sudo apt install cups-ppdc```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppdc](/man/ppdc)(1), [ppdi](/man/ppdi)(1), [cups](/man/cups)(1)

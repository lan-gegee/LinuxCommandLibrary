# TAGLINE

解压 Microsoft COMPRESS.EXE 压缩的文件

# TLDR

**解压一个压缩文件**（输出写到 stdout）

```msexpand [file.ex_]```

**解压文件并保存结果**

```msexpand [file.ex_] > [file.exe]```

**从标准输入解压**

```cat [file.ex_] | msexpand > [file.exe]```

**解压多个文件**

```msexpand [file1.dl_] [file2.ex_]```

**打印版本信息**

```msexpand -V```

# SYNOPSIS

**msexpand** [**-h**]

**msexpand** [**-V**]

**msexpand** [_name_...]

# PARAMETERS

_name_
> 一个或多个压缩的输入文件。若省略，则从标准输入读取数据。

**-h**
> 显示简短用法消息。

**-V**
> 显示版本信息。

# DESCRIPTION

**msexpand** 解压由 **mscompress**(1) 或 Microsoft **COMPRESS.EXE** 工具生成的文件（例如 Windows 3.x 和早期 Windows 9x 安装介质上的 `*.??_` 文件）。

在不带文件参数调用时，msexpand 从标准输入读取压缩数据，并将解压后的输出写到标准输出。提供一个或多个文件名时，会按顺序将每个文件解压到标准输出；通过重定向可将结果保存到文件。

# CAVEATS

只处理旧式 SZDD/KWAJ 单文件压缩格式。它不识别 Microsoft CAB 归档（请改用 **cabextract**(1)），也不支持现代 ZIP 归档。与 DOS 原版的 `EXPAND.EXE` 不同，msexpand 不会自动重命名输出文件。

# HISTORY

属于 **mscompress** 软件包，是 Microsoft COMPRESS/EXPAND 文件格式的自由再实现，以便在 Unix 系统上解开旧版 Windows 安装文件。

# INSTALL

```apt: sudo apt install mscompress```

```nix: nix profile install nixpkgs#mscompress```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cabextract](/man/cabextract)(1), [unzip](/man/unzip)(1), [7z](/man/7z)(1)

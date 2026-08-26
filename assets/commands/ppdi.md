# TAGLINE

将 PPD 文件导入 CUPS 驱动格式

# TLDR

**导入 PPD 文件**

```ppdi [file.ppd]```

**导入到指定目录**

```ppdi -d [output_dir] [file.ppd]```

**导入多个文件**

```ppdi [file1.ppd] [file2.ppd]```

# SYNOPSIS

**ppdi** [_options_] _files_

# PARAMETERS

_FILES_
> 输入的 PPD 文件。

**-d** _DIR_
> 输出目录。

**-o** _FILE_
> 输出文件名。

# DESCRIPTION

**ppdi** 将现有的 PPD（PostScript Printer Description）文件导入 CUPS 驱动源格式（.drv）。它是 **ppdc** 的逆操作，让管理员能够把独立的 PPD 文件转换为紧凑的驱动源格式，便于维护和分发。

导入的驱动源文件可以继续编辑，以添加新的打印机型号或修改选项，然后用 ppdc 重新编译。这一工作流通过将大量打印机定义整合到共享的驱动源文件中，简化了管理工作。

# CAVEATS

仅适用于 CUPS。生成驱动源文件。

# HISTORY

ppdi 是 **CUPS** 的组成部分，用于导入 PPD 文件。

# INSTALL

```apt: sudo apt install cups-ppdc```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppdc](/man/ppdc)(1), [ppdhtml](/man/ppdhtml)(1), [cups](/man/cups)(1)

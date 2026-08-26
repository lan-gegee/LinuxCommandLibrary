# TAGLINE

从自动进纸器批量扫描

# TLDR

**扫描进纸器中的所有页面**

```scanadf -o [output_%d.pnm]```

**扫描指定数量的页面**

```scanadf -e [5] -o [page_%d.pnm]```

**从指定页码开始扫描**

```scanadf -s [1] -o [scan_%d.pnm]```

**使用指定设备扫描**

```scanadf -d [device_name] -o [output_%d.pnm]```

每扫描一页后**运行一次脚本**

```scanadf -S [process.sh] -o [page_%d.pnm]```

**不覆盖现有文件**进行扫描

```scanadf -N -o [output_%d.pnm]```

# SYNOPSIS

**scanadf** [_-d device_] [_-o file_] [_-s num_] [_-e num_] [_-S script_] [_device-options_]

# PARAMETERS

**-d** _device_, **--device-name**=_device_
> 使用指定的扫描仪设备

**-o** _file_, **--output-file**=_file_
> 输出文件名格式；%d 会被替换为页码

**-s** _num_, **--start-count**=_num_
> 第一张扫描图像的页码

**-e** _num_, **--end-count**=_num_
> 要扫描的最后一页的页码

**-S** _script_, **--scan-script**=_script_
> 每获取一张图像后运行的脚本

**-N**, **--no-overwrite**
> 防止覆盖已有的图像文件

**-r**, **--raw**
> 写入未经解释的原始图像数据

**-L**, **--list-devices**
> 列出可用的扫描仪设备

**-v**, **--verbose**
> 提高详细程度

# DESCRIPTION

**scanadf** 是一款命令行工具，用于从配备自动进纸器（ADF）的扫描仪获取多张图像。它按顺序扫描页面直到进纸器为空，并将每一页写入带编号的输出文件。

该工具使用 SANE 接口，支持任何具有 SANE 后端的扫描仪。输出通常为 PNM 格式（根据扫描模式为 PBM、PGM 或 PPM）。分辨率和来源等扫描仪特定选项可以直接传入。

某些扫描仪需要特定的 source 选项：UMAX 使用 **--source="Automatic Document Feeder"**，HP 使用 **--scantype=ADF**。

# CAVEATS

扫描仪后端必须支持 ADF，并在进纸器为空时返回 SANE_STATUS_NO_DOCS。将 scanadf 用于仅支持平板扫描的设备会反复扫描同一页；务必使用 **-e** 限制页数。输出文件名中的 **%d** 占位符对于多页扫描是必需的。

# HISTORY

scanadf 是 **SANE**（Scanner Access Now Easy）项目的一部分，为文档进纸器提供专门支持。它与 scanimage 相辅相成，处理文档扫描场景中常见的多页工作流程。

# SEE ALSO

[scanimage](/man/scanimage)(1), [sane-find-scanner](/man/sane-find-scanner)(1), [convert](/man/convert)(1)

# TAGLINE

灵活的 I/O 测试与基准测试工具

# TLDR

**顺序读测试**

```fio --name=test --rw=read --size=[1G]```

**随机写测试**

```fio --name=test --rw=randwrite --size=[1G]```

**运行作业文件**

```fio [jobfile.fio]```

**混合读写测试**

```fio --name=test --rw=randrw --rwmixread=[70] --size=[1G]```

**测量延迟**

```fio --name=test --rw=randread --size=[1G] --lat_percentiles=1```

# SYNOPSIS

**fio** [_options_] [_jobfiles_...]

# PARAMETERS

_JOBFILES_
> 作业定义文件。

**--name** _NAME_
> 作业名称。

**--rw** _TYPE_
> I/O 类型：read、write、randread、randwrite、randrw。

**--size** _SIZE_
> I/O 总大小。

**--bs** _SIZE_
> 块大小。

**--iodepth** _N_
> I/O 队列深度。

**--numjobs** _N_
> 并行作业数量。

**--runtime** _SEC_
> 测试持续时间。

**--output** _FILE_
> 输出文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fio**（Flexible I/O Tester）是一款多用途的 I/O 基准测试工具，用于检验存储性能。它能模拟各种负载模式，并测量吞吐量、IOPS 和延迟。

该工具支持众多 I/O 引擎，包括 sync、libaio、io_uring 以及各类网络协议。作业文件可以定义包含多种负载的复杂测试场景。

fio 是存储基准测试领域的标准工具，常用于磁盘选型、文件系统调优和性能验证。

# CAVEATS

结果会随测试参数而变化。可能会用测试文件占满磁盘。要想获得有意义的结果，需要对 I/O 模式有所了解。

# HISTORY

fio 由 Linux 块层维护者 **Jens Axboe** 开发。它是功能最全面的开源存储基准测试工具，几乎所有 I/O 模式和存储后端都在其支持范围内。

# INSTALL

```apt: sudo apt install fio```

```dnf: sudo dnf install fio```

```pacman: sudo pacman -S fio```

```apk: sudo apk add fio```

```zypper: sudo zypper install fio```

```brew: brew install fio```

```nix: nix profile install nixpkgs#fio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [hdparm](/man/hdparm)(1), [ioping](/man/ioping)(1)

# RESOURCES

```[Source code](https://github.com/axboe/fio)```

```[Documentation](https://fio.readthedocs.io/)```

<!-- verified: 2026-07-15 -->

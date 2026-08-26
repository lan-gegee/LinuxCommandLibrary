# TAGLINE

启动 MATLAB，一个用于数值计算的计算环境

# TLDR

**启动 MATLAB**

```matlab```

**不带 GUI 启动**（命令行模式）

```matlab -nodesktop```

**运行脚本后退出**

```matlab -batch "[script_name]"```

**使用指定启动命令运行**

```matlab -r "[startup_commands]"```

**不显示启动画面启动**

```matlab -nosplash```

**带参数运行脚本**

```matlab -batch "[myscript('[arg1]', '[arg2]')]"```

**以更低内存占用启动**

```matlab -nojvm```

**显示版本**

```matlab -help```

# SYNOPSIS

**matlab** [_-nodesktop_] [_-batch command_] [_-r command_] [_-nosplash_] [_options_]

# PARAMETERS

**-nodesktop**
> 不启动桌面 GUI。

**-nodisplay**
> 不启动显示（无图形窗口）。

**-nosplash**
> 跳过启动画面。

**-nojvm**
> 不使用 Java 启动（功能受限）。

**-batch** _COMMAND_
> 运行命令/脚本后退出。

**-r** _COMMAND_
> 启动时运行命令。

**-logfile** _FILE_
> 将输出复制到日志文件。

**-sd** _DIR_
> 设置启动目录。

**-useStartupFolderPref**
> 使用启动文件夹的首选项设置。

**-singleCompThread**
> 限制为单线程。

**-help**
> 显示帮助与版本。

# DESCRIPTION

**matlab** 启动 MATLAB，这是一个用于数值计算、可视化和编程的计算环境，广泛应用于工程、科学和金融领域。

桌面版提供集成环境，包括编辑器、命令行窗口、工作区和图形窗口。无桌面模式则提供命令行交互，适合脚本和自动化任务。

批处理模式（-batch）执行命令后退出，适用于自动化工作流和定时任务。出错时它会返回非零退出码，而 -r 出错后会继续运行。

脚本（.m 文件）包含 MATLAB 代码，函数定义可复用的操作。MATLAB 路径决定了哪些文件可以被访问。

不使用 JVM（-nojvm）时，MATLAB 占用内存更少，但会失去桌面、图形窗口及部分工具箱功能。适用于资源受限系统上的纯计算任务。

# CAVEATS

需要商业许可证。内存占用较大。启动时间可能较长。部分工具箱需要额外许可。并非所有功能都能在 nodesktop 模式下使用。

# HISTORY

**MATLAB** 由 **Cleve Moler** 于 **20 世纪 70 年代末** 创建，目的是让学生无需 Fortran 就能使用 LINPACK 和 EISPACK。**MathWorks** 于 **1984 年**成立并将其商业化。MATLAB 成为学术界和工业界数值计算的标准。

# INSTALL

```aur: yay -S matlab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[octave](/man/octave)(1), [python](/man/python)(1), [julia](/man/julia)(1), [r](/man/r)(1)

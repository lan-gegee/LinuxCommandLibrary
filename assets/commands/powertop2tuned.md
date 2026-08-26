# TAGLINE

将 PowerTOP 建议转换为 TuneD 配置文件

# TLDR

根据当前的 PowerTOP 报告**生成新配置文件**

```sudo powertop2tuned [my_powersave]```

从现有的 PowerTOP HTML 报告**生成配置文件**

```sudo powertop2tuned -i [/path/to/powertop.html] [my_powersave]```

将配置文件**输出到自定义目录**

```sudo powertop2tuned -o [/etc/tuned/my_profile] [my_powersave]```

**创建全新的配置文件**而不是与当前配置合并

```sudo powertop2tuned -n [my_powersave]```

将 PowerTOP 建议与**指定的** TuneD 配置文件**合并**

```sudo powertop2tuned -m [balanced] [my_powersave]```

**启用全部** PowerTOP 调优项（跳过安全确认步骤）

```sudo powertop2tuned -e [my_powersave]```

**强制覆盖**已有的配置文件目录

```sudo powertop2tuned -f [my_powersave]```

# SYNOPSIS

**powertop2tuned** [_options_] _profile_name_

# PARAMETERS

**-i** _FILE_, **--input** _FILE_
> 使用 _FILE_ 作为 PowerTOP HTML 报告，而不是重新生成一份。

**-o** _DIR_, **--output** _DIR_
> 将生成的配置文件写入 _DIR_（默认：TuneD 的用户配置文件目录）。

**-n**, **--new-profile**
> 创建全新的配置文件，而不是与当前活动的 TuneD 配置文件合并。

**-m** _PROFILE_, **--merge-profile** _PROFILE_
> 与指定的 _PROFILE_ 合并，而不是当前活动的配置文件。

**-f**, **--force**
> 如果输出目录已存在则覆盖。

**-e**, **--enable**
> 启用 PowerTOP 建议的所有调优项。被视为有害的调优项（如 **USB_AUTOSUSPEND**）仍保持禁用。

**-h**, **--help**
> 显示用法并退出。

# DESCRIPTION

**powertop2tuned** 将 **PowerTOP** 生成的建议转换为可运行的 **TuneD** 配置文件，在这两个工具之间架起桥梁，使 PowerTOP 发现的节能项得以永久应用，并能像其他 TuneD 配置文件一样回滚。

该工具会在底层运行 PowerTOP（或读取通过 **-i** 提供的现有 HTML 报告），解析每个 "Tunable" 条目，然后生成一个包含 **tuned.conf** 文件和一个辅助 shell 脚本的配置目录。默认情况下，生成的配置文件继承当前活动的 TuneD 配置文件以保留基础优化；**--new-profile** 会创建独立配置文件，而 **--merge-profile** 允许你选择不同的父配置文件。

出于安全考虑，生成的配置文件中每条 PowerTOP 建议最初都被注释掉。管理员应当逐一审查，仅取消注释适合目标硬件的行。**--enable** 标志表示选择启用所有调优项，但脚本认为不安全的除外。

生成的配置文件与其他 TuneD 配置文件的启用方式相同，使用 **tuned-adm profile** _profile_name_ 即可。

# CAVEATS

PowerTOP 标记为 "Bad" 的调优项可能损坏设备：ALPM 和 SATA 链路电源管理可能损坏某些 SSD，USB 自动挂起会断开键盘/摄像头，Wi-Fi 省电在某些芯片上会导致连接中断。务必先在非关键机器上测试，并在启用前检查生成的 **tuned.conf**。运行 PowerTOP 和写入 **/etc/tuned/** 需要 **root** 权限。它是 **tuned-utils** 软件包的一部分，在多数发行版上与核心的 **tuned** 软件包相互独立。

# CONFIGURATION

配置文件会写入 **/etc/tuned/**_profile_name_**/tuned.conf**，并附带 script.sh 辅助脚本。使用 **tuned-adm profile** _profile_name_ 启用；用 **tuned-adm profile** _balanced_（或其他任意配置文件）切回。只要启用了 **tuned.service** systemd 单元，活动的配置文件就会在重启后保持生效。

# HISTORY

**powertop2tuned** 随 Red Hat 的 **TuneD** 项目发布，最初是为了让 Fedora 和 RHEL 用户能够一步把 PowerTOP 的发现成果固化到 TuneD 框架中。它在 Fedora、RHEL、CentOS、openSUSE 和 Arch 上通过 **tuned-utils** 软件包分发。

# INSTALL

```dnf: sudo dnf install tuned-utils```

```apk: sudo apk add tuned-utils```

```zypper: sudo zypper install tuned-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[powertop](/man/powertop)(8), [tuned](/man/tuned)(8), [tuned-adm](/man/tuned-adm)(8)

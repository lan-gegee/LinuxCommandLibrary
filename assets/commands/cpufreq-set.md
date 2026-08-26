# TAGLINE

修改 CPU 频率调节设置

# TLDR

为特定 CPU **设置频率 governor**

```sudo cpufreq-set -c [1] -g [performance]```

**设置允许的最小频率**

```sudo cpufreq-set -c [1] -d [800MHz]```

**设置允许的最大频率**

```sudo cpufreq-set -c [1] -u [2.4GHz]```

**锁定到指定频率**（需要 userspace governor）

```sudo cpufreq-set -c [1] -f [2000MHz]```

**将设置应用到共享同一策略的所有 CPU**

```sudo cpufreq-set -r -g [powersave]```

# SYNOPSIS

**cpufreq-set** [_options_]

# PARAMETERS

**-c**, **--cpu** _cpu_
> 要操作的 CPU 编号。省略时默认为 CPU 0。

**-d**, **--min** _freq_
> 设置 governor 可选择的最小频率。

**-u**, **--max** _freq_
> 设置 governor 可选择的最大频率。

**-g**, **--governor** _governor_
> 选择调频 governor（如 `performance`、`powersave`、`ondemand`、`conservative`、`schedutil`、`userspace`）。

**-f**, **--freq** _freq_
> 将 CPU 锁定到指定频率。需要 `userspace` governor，且不能与 `-d`、`-u` 或 `-g` 组合使用。

**-r**, **--related**
> 同时将更改应用到与所选 CPU 硬件相关的所有 CPU。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**cpufreq-set** 修改某个 CPU 的 Linux 内核 cpufreq 策略，调整调频 governor、最小和最大频率，或锁定固定频率。它是 **cpufrequtils** 软件包的一部分。

频率值可直接在数字后加 `Hz`、`kHz`（未给单位时的默认值）、`MHz`、`GHz` 或 `THz` 后缀（例如 `2400MHz` 或 `2.4GHz`）。当前 CPU 的有效取值可通过 `cpufreq-info -l` 查看。

# CAVEATS

需要 root 权限（或对 `/sys/devices/system/cpu/cpu*/cpufreq/` 的写权限）。锁定固定频率仅在 `userspace` governor 处于活动并加载状态时有效。可用的 governor 取决于内核配置。设置不会跨重启保留；请使用 systemd unit 或 `cpufrequtils` 服务在启动时恢复它们。在使用 `intel_pstate` 驱动的现代内核上，可能只有 `performance` 和 `powersave` 两个 governor 可用。

# HISTORY

**cpufreq-set** 随 **cpufrequtils** 发布，后者最初由 **Dominik Brodowski** 编写。较新的 **cpupower** 套件（来自内核源码树）在近期的发行版上已在很大程度上取代了 cpufrequtils。

# INSTALL

```apk: sudo apk add cpufrequtils```

```nix: nix profile install nixpkgs#cpufrequtils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpufreq-info](/man/cpufreq-info)(1), [cpupower](/man/cpupower)(1)

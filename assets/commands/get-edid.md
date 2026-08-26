# TAGLINE

通过 DDC 从显示器读取原始 EDID

# TLDR

从第一个找到的显示器**读取**原始 EDID（需要 root 权限）

```sudo get-edid```

**读取** EDID 并**解析**成 xorg.conf 风格的显示器 section

```sudo get-edid | parse-edid```

将原始 EDID **保存**到文件

```sudo get-edid > monitor.bin```

**只扫描**指定的 I2C 总线

```sudo get-edid --bus 5 > monitor.bin```

**仅使用**现代 I2C 接口

```sudo get-edid --i2conly | parse-edid```

**仅使用**较旧的 VBE/实模式接口

```sudo get-edid --classiconly | parse-edid```

**安静**模式（不在 stderr 上输出进度信息）

```sudo get-edid -q > monitor.bin```

# SYNOPSIS

**get-edid** [_OPTIONS_]

# DESCRIPTION

**get-edid** 是 **read-edid** 工具集的一员。它使用 VESA Data Display Channel（DDC）从连接的显示器读取原始扩展显示识别数据（EDID）块。它可以通过 Linux I2C（Enhanced DDC）与显示器通信，或在受支持的构建中通过实模式 VBE DDC 调用通信。

该程序将二进制 EDID 写入标准输出。配套工具 **parse-edid** 读取该二进制流并打印人类可读的摘要，外加一个与 **xorg.conf** 兼容的 Monitor section（其中的 modeline 可用于 **xrandr**）。通常的做法是把两者管道连接：**get-edid | parse-edid**。

在现代系统上，读取 **/sys/class/drm/\*/edid** 并用 **edid-decode** 解码通常更简单且不需要 root 权限；当 sysfs 中缺少 EDID 或需要从更底层的 DDC 路径配置显示器时，**get-edid** 仍然有用。

# PARAMETERS

**-b** _BUS_, **--bus** _BUS_
> 只扫描 I2C 总线编号 _BUS_（需在启用 i2c 支持的构建下）。

**-c**, **--classiconly**
> 仅使用较旧的 VBE 接口（当 i2c 和 VBE 都可用时）。

**-h**, **--help**
> 显示简短帮助信息并列出当前构建支持的选项。

**-i**, **--i2conly**
> 仅使用 I2C 接口（当 i2c 和 VBE 都可用时）。

**-m** _NUM_, **--monitor** _NUM_
> 请求第 _NUM_ 号显示器的信息（仅限 VBE 接口）。

**-q**, **--quiet**
> 抑制标准错误上的状态消息。

# CAVEATS

通常需要 root 权限（或 CAP_SYS_RAWIO / 访问相应的 **/dev/i2c-*** 设备）。并非所有显卡和显示器都可靠地实现了 DDC；某些组合会返回部分数据或空数据。多显示器环境可能需要 **--bus** 或 **--monitor** 来选择正确的显示器。当内核 DRM 为连接器暴露 EDID 时，优先使用 **edid-decode** 解析 **/sys/class/drm/\*/edid**。

# HISTORY

**read-edid** 最初由 **John Fremlin** 编写。从版本 1.4.2 起，**Matthew Kern** 成为维护者，并在 3.0.0 版本中大幅重写了这些工具，加入 I2C 支持和当前的选项集合。主页：**http://www.polypux.org/projects/read-edid/**。

# INSTALL

```apt: sudo apt install read-edid```

```pacman: sudo pacman -S read-edid```

```nix: nix profile install nixpkgs#read-edid```

<!-- packages: 2026-08-12 -->

# SEE ALSO

[edid-decode](/man/edid-decode)(1), [xrandr](/man/xrandr)(1), [xorg](/man/Xorg)(1)

# RESOURCES

```[Homepage](http://www.polypux.org/projects/read-edid/)```

<!-- verified: 2026-08-12 -->

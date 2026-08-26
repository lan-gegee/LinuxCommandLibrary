# TAGLINE

自动管理显示器配置档

# TLDR

**保存**当前布局

```autorandr -s profile_name```

**列出**已保存的配置档

```autorandr```

**自动检测**并应用配置档

```autorandr -c```

**加载**指定配置档

```autorandr -l profile_name```

设置**默认**配置档

```autorandr -d profile_name```

# SYNOPSIS

**autorandr** [_OPTIONS_] [_PROFILE_]

# DESCRIPTION

**autorandr** 自动检测已连接的显示器，并根据保存的配置档应用合适的屏幕布局。它与 **xrandr** 集成，可在显示器接入或断开时自动切换配置档。

配置档通过所连接显示器的 EDID 指纹识别，从而在扩展坞、投影仪或笔记本单独使用等不同显示器配置之间无缝切换。该工具可以手动触发，也可以作为 **udev** 或 **systemd** 钩子运行，实现全自动配置档切换。

# PARAMETERS

**-s, --save** _name_
> 将当前屏幕布局保存为配置档

**-l, --load** _name_
> 加载指定的配置档

**-c, --change**
> 自动检测并加载合适的配置档

**-d, --default** _name_
> 设置默认配置档（未找到匹配时使用）

**--fingerprint**
> 显示当前设置的指纹

**--remove** _name_
> 删除一个已保存的配置档

**--list**
> 列出所有已保存的配置档

**--cycle**
> 在所有检测到的配置档之间循环切换

**--force**
> 即使设置已经应用也强制重新配置

**--dry-run**
> 打印将进行的更改但不实际应用

**--batch**
> 以批处理模式运行（无需确认）

**--match-edid**
> 按 EDID 而非输出名称匹配显示器

**--skip-options** _options_
> 比较时跳过某些 xrandr 选项

# CONFIGURATION

**~/.config/autorandr/**
> 存放已保存显示器配置档的目录。每个配置档是一个包含 setup 和 config 文件的子目录。

# CAVEATS

需要安装 xrandr。配置档匹配基于已连接显示器的 EDID。虚拟显示器或没有有效 EDID 的显示器可能无法正确匹配。

# HISTORY

**autorandr** 通过自动检测并应用已保存的配置来简化多显示器设置，常与笔记本扩展坞和外接显示器搭配使用。

# INSTALL

```dnf: sudo dnf install autorandr```

```pacman: sudo pacman -S autorandr```

```apk: sudo apk add autorandr```

```zypper: sudo zypper install autorandr```

```nix: nix profile install nixpkgs#autorandr```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[xrandr](/man/xrandr)(1), [arandr](/man/arandr)(1)

# RESOURCES

```[Source code](https://github.com/phillipberndt/autorandr)```

<!-- verified: 2026-06-17 -->

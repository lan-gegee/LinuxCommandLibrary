# TAGLINE

为 Environment Modules 软件包提供用户界面，支持动态修改环境

# TLDR

显示**可用模块**

```module avail```

**按名称搜索**模块

```module avail [module_name]```

**加载**模块

```module load [module_name]```

显示**已加载的模块**

```module list```

**卸载**特定模块

```module unload [module_name]```

**卸载全部**已加载的模块

```module purge```

**保存**当前已加载模块的集合

```module save [collection_name]```

**恢复**已保存的集合

```module restore [collection_name]```

# SYNOPSIS

**module** [_switches_] _sub-command_ [_sub-command-args_]

# PARAMETERS

**avail [_pattern_]**
> 列出与可选模式匹配的可用 modulefile

**load _modulefile_...**
> 将模块加载进当前环境

**unload _modulefile_...**
> 从环境中移除模块

**list [_pattern_]**
> 列出当前已加载的模块

**purge [-f]**
> 卸载所有已加载的模块

**reload [-f]**
> 先卸载再重新加载所有模块

**switch _old_ _new_**
> 用一个模块替换另一个

**save [_collection_]**
> 将当前环境状态保存到集合

**restore [_collection_]**
> 恢复已保存的环境集合

**savelist**
> 列出已保存的集合

**display _modulefile_**
> 显示 modulefile 内容及其效果

**whatis _string_**
> 搜索 modulefile 的描述

**use _path_...**
> 向 modulefile 搜索路径添加目录

**--json, -j**
> 以 JSON 格式输出

**--long, -l**
> 长格式输出

**--terse, -t**
> 短格式输出

**-v, --verbose**
> 启用详细消息

# DESCRIPTION

**module** 为 Environment Modules 软件包提供用户界面，通过 modulefile 动态修改 shell 环境。每个 modulefile 包含应用程序的配置，通常用于修改 PATH、MANPATH、LD_LIBRARY_PATH 等环境变量。

这套系统让用户无需手动管理环境变量即可加载和卸载软件配置。modulefile 作为 Tcl 脚本解释执行，可以设置变量、创建别名并定义依赖关系。

集合（Collection）可用于保存和恢复一组已加载的模块，便于在不同项目配置或工作流之间切换。

# CAVEATS

modulefile 必须以魔法字符串 #%Module 开头。除非正确定义依赖关系，加载相互冲突的模块可能导致意外行为。module 命令修改的是当前 shell 环境；shell 退出后更改即丢失，除非保存到 shell 初始化文件中。

# HISTORY

**Environment Modules** 系统起源于 20 世纪 90 年代初的美国能源部计算设施。基于 Lua 实现的 **Lmod** 由德克萨斯高级计算中心（TACC）开发，在 HPC 系统上广泛使用。两者都为管理软件环境提供了兼容的用户界面。

# SEE ALSO

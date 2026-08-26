# TAGLINE

打印当前活动 Node.js 版本的安装路径

# TLDR

**打印路径**：显示当前活动的 Node.js 安装位置

```get-nodeinstalllocation```

# SYNOPSIS

**get-nodeinstalllocation**

# DESCRIPTION

**get-nodeinstalllocation** 是一个辅助垫片脚本，输出用户 **PATH** 上当前 Node.js 安装的绝对文件系统路径。它通常由 Node.js 版本管理器或发行版打包脚本提供，以便各种工具（安装程序、构建系统、编辑器集成）无需解析环境变量即可定位活动中的 Node.js 目录树。

用纯 Node.js 实现等价查询的方式是 `node -e "console.log(process.execPath)"`，或者在 POSIX 系统上使用 `dirname "$(readlink -f "$(command -v node)")"`。

# CAVEATS

这是厂商特定的包装脚本，而非上游 Node.js 的命令。其行为取决于你的 Node.js 安装方式；如果系统上不存在这样的脚本，请改用 `which node` / `command -v node` 或 `node -p "process.execPath"` 来获取相同的信息。

# SEE ALSO

[node](/man/node)(1), [which](/man/which)(1), [readlink](/man/readlink)(1)

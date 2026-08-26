# TAGLINE

用 Web 技术构建跨平台桌面应用

# TLDR

**运行 Electron 应用**

```electron [.]```

**运行指定目录**

```electron [path/to/app]```

**启用远程调试运行**

```electron --remote-debugging-port=[9222] [.]```

**显示版本**

```electron --version```

**以详细日志运行**

```electron --enable-logging [.]```

**禁用 GPU 加速**

```electron --disable-gpu [.]```

# SYNOPSIS

**electron** [_options_] [_path_]

# PARAMETERS

_path_
> 应用目录或 package.json 的路径。

**--version**
> 显示 Electron 版本。

**--remote-debugging-port** _port_
> 启用远程调试。

**--enable-logging**
> 启用控制台日志输出。

**--disable-gpu**
> 禁用 GPU 硬件加速。

**--no-sandbox**
> 禁用沙箱（不推荐）。

**--inspect** _port_
> 启用 Node.js 调试器。

**--inspect-brk** _port_
> 启用调试器并在启动时中断。

# DESCRIPTION

**Electron** 是一个使用 Web 技术（HTML、CSS、JavaScript）构建跨平台桌面应用的框架。它内嵌 Chromium 负责渲染，内嵌 Node.js 提供后端功能。

应用会连同各自的 Electron 运行时一起打包，从而在没有系统依赖的情况下部署。知名的 Electron 应用包括 VS Code、Slack、Discord 和 Atom。

# PROJECT STRUCTURE

```
my-app/
├── package.json    # Main entry point defined
├── main.js         # Main process
├── preload.js      # Preload script
├── index.html      # Renderer content
└── renderer.js     # Renderer process
```

# CAVEATS

由于捆绑了 Chromium，应用体积较大。内存占用高。安全性需要正确配置（上下文隔离、preload 脚本）。更新需要谨慎处理。存在多个进程（主进程和渲染进程）。

# HISTORY

Electron 最初由 **GitHub** 为 Atom 编辑器开发，当时名为 **Atom Shell**，诞生于 **2013 年**。它于 **2015 年**更名为 Electron 并开源发布。该项目让 Web 开发者能够构建原生应用，彻底改变了桌面应用的开发方式。

# INSTALL

```pacman: sudo pacman -S electron```

```nix: nix profile install nixpkgs#electron```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npm](/man/npm)(1), [tauri](/man/tauri)(1)

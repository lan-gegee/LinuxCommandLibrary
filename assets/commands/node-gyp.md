# TAGLINE

用于编译 Node 原生扩展的跨平台构建工具

# TLDR

**配置项目**

```node-gyp configure```

**构建原生扩展**

```node-gyp build```

**清理构建文件**

```node-gyp clean```

**重新构建（clean + configure + build）**

```node-gyp rebuild```

**安装 Node.js 头文件**

```node-gyp install```

**指定 Node.js 版本**

```node-gyp rebuild --target=[18.0.0]```

# SYNOPSIS

**node-gyp** _command_ [_options_]

# PARAMETERS

**configure**
> 生成构建文件。

**build**
> 构建原生扩展。

**clean**
> 移除构建目录。

**rebuild**
> 完整重建。

**install**
> 安装 Node.js 头文件。

**--target** _version_
> Node.js 版本。

**--debug**
> 调试构建。

**--arch** _arch_
> 目标架构。

# DESCRIPTION

**node-gyp** 是一个跨平台构建工具，用于编译 Node.js 原生扩展模块。它使用 GYP（Generate Your Projects）生成针对特定平台的构建文件。

node-gyp 需要 Python 和 C++ 编译器（如 gcc、clang 或 MSVC）。

# BINDING.GYP

```json
{
  "targets": [{
    "target_name": "addon",
    "sources": ["src/addon.cc"],
    "include_dirs": [
      "<!(node -p \"require('node-addon-api').include\")"
    ]
  }]
}
```

# CAVEATS

需要 Python 3.x。需要 C++ 构建工具。不同操作系统的要求不同。可能需要 --python 标志。

# HISTORY

node-gyp 由 **Nathan Rajlich**（TooTallNate）创建，旨在简化跨平台构建 Node.js 原生扩展的过程。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

```nix: nix profile install nixpkgs#node-gyp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [node](/man/node)(1)

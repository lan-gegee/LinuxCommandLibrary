# TAGLINE

Rust WebAssembly 应用打包工具

# TLDR

构建项目

```trunk build```

带优化进行发布构建

```trunk build --release```

以热重载方式提供服务

```trunk serve```

在特定端口和地址上提供服务

```trunk serve --port [3000] --address [0.0.0.0]```

使用后端代理提供服务

```trunk serve --proxy-backend=http://localhost:[9000]/api/```

监视变更并重新构建

```trunk watch```

清理构建产物

```trunk clean```

# SYNOPSIS

**trunk** _command_ [_--release_] [_options_]

# PARAMETERS

**build**
> 构建项目，将 Rust 编译为 WASM 并打包资源。

**serve**
> 启动支持热重载的开发服务器。

**watch**
> 监视文件更改并自动重新构建。

**clean**
> 移除构建产物 (dist 目录)。

**--release**
> 启用发布优化，包括缩减 WASM 体积。

**--public-url** _URL_
> 资源路径的公共 URL 前缀。

**--port** _PORT_
> 开发服务器的端口（默认：8080）。

**--address** _ADDR_
> 开发服务器绑定的地址。

**--proxy-backend** _URL_
> 将请求代理到后端服务器。URL 的 URI 路径决定代理路径。

**--proxy-rewrite** _URI_
> 用于监听代理请求的替代 URI。

# DESCRIPTION

**Trunk** 是一个面向 Rust WebAssembly 应用的构建工具，负责编译、打包和服务。它将 Rust 代码编译为 WebAssembly，处理 CSS 和 JavaScript 等资源，并生成在浏览器中运行 WASM 模块所需的 HTML 与 JavaScript 胶水代码。

开发服务器提供热重载能力：源文件发生变化时自动重新构建并刷新浏览器。发布构建会应用包括缩减 WASM 体积在内的各种优化，适合生产部署。

Trunk 集成 wasm-bindgen 以实现 JavaScript 互操作，并可与 Yew、Leptos 和 Seed 等框架配合使用。配置通过项目根目录下的 Trunk.toml 文件管理。

# CONFIGURATION

**Trunk.toml**
> 项目配置文件，指定构建选项、代理设置和资源管线规则。

# CAVEATS

仅针对 Rust/WASM。基于 wasm-bindgen。使用 Trunk.toml 配置。

# HISTORY

**Trunk** 为构建和打包 Rust WebAssembly 应用而创建。

# INSTALL

```dnf: sudo dnf install trunk```

```pacman: sudo pacman -S trunk```

```apk: sudo apk add trunk```

```brew: brew install trunk```

```nix: nix profile install nixpkgs#trunk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wasm-pack](/man/wasm-pack)(1), [cargo](/man/cargo)(1)

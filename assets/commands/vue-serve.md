# TAGLINE

Vue 组件的开发服务器

# TLDR

**以开发模式运行**

```vue serve```

**运行指定文件**

```vue serve [App.vue]```

**在自定义端口上运行**

```vue serve --port [8080]```

**自动打开浏览器**

```vue serve --open```

# SYNOPSIS

**vue** **serve** [_options_] [_entry_]

# PARAMETERS

**-o**, **--open**
> 自动打开浏览器

**-c**, **--copy**
> 将本地 URL 复制到剪贴板

**-p**, **--port** _port_
> 端口号（默认：8080）

**-h**, **--host** _host_
> 主机地址（默认：0.0.0.0）

# DESCRIPTION

**vue serve** 启动一个带热更新的开发服务器，无需完整的项目设置即可对 Vue 单文件组件进行即时原型开发。它要求全局安装 **@vue/cli-service-global** 软件包。

在 Vue CLI v5 中，即时原型功能已被移除，**vue serve** 成为 **npm run serve** 的别名。对于独立的组件原型开发，Vue 现在推荐改用 **Vite**。

# INSTALL

```nix: nix profile install nixpkgs#vue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vue](/man/vue)(1), [vue-build](/man/vue-build)(1), [vite](/man/vite)(1)

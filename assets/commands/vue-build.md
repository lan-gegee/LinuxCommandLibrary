# TAGLINE

为生产环境构建 Vue.js 应用

# TLDR

**为生产环境构建**

```vue build```

**以自定义目标构建**

```vue build --target [lib]```

**构建指定入口**

```vue build [entry.js]```

# SYNOPSIS

**vue** **build** [_options_] [_entry_]

# PARAMETERS

**--target** _target_
> 构建目标（app、lib、wc）。

**--name** _name_
> 库名或组件名。

**--dest** _dir_
> 输出目录。

**--modern**
> 为现代浏览器构建并自动提供旧浏览器回退（仅 Vue CLI 4 支持，CLI 5 中已移除）。

**--no-clean**
> 构建前不清空输出目录。

**--watch**
> 监视变更并自动重新构建。

# DESCRIPTION

**vue build** 为生产环境编译 Vue.js 应用，生成经过压缩和 tree-shaking 优化的打包产物。它是 Vue CLI 即时原型功能的一部分（需要 `@vue/cli-service-global`）。标准的项目构建请使用 `vue-cli-service build`。

# INSTALL

```nix: nix profile install nixpkgs#vue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vue](/man/vue)(1), [vue-serve](/man/vue-serve)(1)

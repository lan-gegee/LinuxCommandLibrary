# TAGLINE

打包 JavaScript 模块以便分发

# TLDR

**打包 JavaScript**

```rollup [main.js] --file [bundle.js]```

**使用配置文件**

```rollup -c```

**输出格式**

```rollup [main.js] -o [bundle.js] -f [es]```

**监视文件变化**

```rollup -c --watch```

**生成 sourcemap**

```rollup [main.js] -o [bundle.js] -m```

**使用指定插件打包**

```rollup [main.js] -o [bundle.js] -p [node-resolve]```

# SYNOPSIS

**rollup** [_options_] _input_

# DESCRIPTION

**rollup** 是一个专注于 ES 模块的 JavaScript 模块打包器。它把小的代码片段编译成更大的包，并凭借出色的 tree-shaking 消除未使用的代码。

该工具为库和应用程序生成高效的打包产物，支持多种输出格式。

# PARAMETERS

**-c** _file_, **--config** _file_
> 配置文件。

**-o** _file_, **--file** _file_
> 输出文件。

**-f** _fmt_, **--format** _fmt_
> 输出格式（es、cjs、umd、iife、amd、system）。

**-n** _name_, **--name** _name_
> UMD/IIFE 全局名称。

**-m**, **--sourcemap**
> 生成 sourcemap。

**-w**, **--watch**
> 监视模式。

**-p** _plugin_, **--plugin** _plugin_
> 使用插件。

**-d** _dir_, **--dir** _dir_
> 输出目录（用于代码拆分）。

**-e** _modules_, **--external** _modules_
> 逗号分隔的外部模块 ID 列表。

**-g** _pairs_, **--globals** _pairs_
> 逗号分隔的 global:module 对，用于 UMD/IIFE。

**--no-treeshake**
> 禁用 tree shaking。

# CONFIGURATION

**rollup.config.js** / **rollup.config.mjs**
> 项目级配置文件，定义输入入口、输出格式、插件和外部依赖。通过 **-c** 或指定路径自动加载。

# CAVEATS

复杂项目需要配置文件。插件生态必不可少。CommonJS 需要插件支持。大型项目的构建时间可能较长。

# HISTORY

**Rollup** 由 **Rich Harris** 于 **2015 年**创建。它率先采用带 tree-shaking 的 ES 模块打包方式，影响了后来的打包器。Harris 也是 Svelte 的作者。

# INSTALL

```zypper: sudo zypper install rollup```

```brew: brew install rollup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[webpack](/man/webpack)(1), [esbuild](/man/esbuild)(1), [vite](/man/vite)(1), [parcel](/man/parcel)(1)

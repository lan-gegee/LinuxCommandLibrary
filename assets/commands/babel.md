# TAGLINE

将现代 JavaScript 转译为向后兼容的版本。

# TLDR

**转译**JavaScript 文件

```babel [input.js] -o [output.js]```

转译**目录**

```babel [src] -d [dist]```

**监视**模式

```babel [src] -d [dist] --watch```

使用**指定预设**

```babel [input.js] -o [output.js] --presets=@babel/preset-env```

**内联** source map

```babel [input.js] -o [output.js] --source-maps inline```

# SYNOPSIS

**babel** [_options_] _files_

# DESCRIPTION

**babel** 是一个 JavaScript 编译器，能把现代 JavaScript（ES6+）转换为向后兼容的版本，以便在较旧的浏览器和环境中运行。它通过插件和预设支持 JSX、TypeScript 以及实验性的 JavaScript 特性。

该工具是现代 JavaScript 开发的重要基石，让开发者既能使用最新的语言特性，又能保持广泛的兼容性。

# PARAMETERS

**-o**, **--out-file** _file_
> 输出文件

**-d**, **--out-dir** _dir_
> 输出目录

**-w**, **--watch**
> 监视文件变动

**-s**, **--source-maps**
> 生成 source map

**--presets** _presets_
> 转换预设

**--plugins** _plugins_
> 转换插件

**--config-file** _path_
> 配置文件路径

**--no-babelrc**
> 忽略 .babelrc 文件

**--minified**
> 压缩输出

**--compact** _mode_
> 紧凑输出（true/false/auto）

**--ignore** _glob_
> 要跳过的文件的 glob 模式

**--extensions** _exts_
> 要编译的文件扩展名（默认：.js,.jsx,.es6,.es,.mjs,.cjs）

# COMMON PRESETS

**@babel/preset-env**
> 将现代 JavaScript 转换为适配目标环境的形式

**@babel/preset-react**
> 为 React 转换 JSX

**@babel/preset-typescript**
> 转换 TypeScript

# CONFIGURATION

**babel.config.json**
> 项目级的 Babel 配置，用于预设、插件和转换选项。

**.babelrc**
> 目录级的 Babel 配置，作用于所在目录内的文件。

# CAVEATS

需要 Node.js。配置可能比较复杂。构建时间随文件数量增加而变长。某些语言特性需要 polyfill（仅靠转译不够）。插件的顺序很重要。

# HISTORY

**Babel** 由 Sebastian McKenzie 于 **2014** 年创建（最初名为 6to5），目的是让开发者能在浏览器尚未广泛支持时就使用 ES6 特性。

# INSTALL

```brew: brew install babel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [npx](/man/npx)(1), [webpack](/man/webpack)(1), [tsc](/man/tsc)(1), [eslint](/man/eslint)(1)

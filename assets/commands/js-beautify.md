# TAGLINE

以一致的缩进和风格格式化 JavaScript、HTML 和 CSS 文件

# TLDR

**美化 JavaScript 文件**

```js-beautify [file.js]```

**美化并原地保存**

```js-beautify -r [file.js]```

**美化 HTML**

```html-beautify [file.html]```

**美化 CSS**

```css-beautify [file.css]```

**设置缩进**

```js-beautify -s [4] [file.js]```

**使用制表符**

```js-beautify -t [file.js]```

**输出到文件**

```js-beautify [input.js] -o [output.js]```

# SYNOPSIS

**js-beautify** [_options_] [_file_...]

# PARAMETERS

**-r**, **--replace**
> 原地替换文件。

**-o** _file_
> 输出到文件。

**-s** _size_
> 缩进宽度（默认 4）。

**-t**, **--indent-with-tabs**
> 使用制表符缩进。

**-e**, **--eol** _chars_
> 行尾字符。

**-n**, **--end-with-newline**
> 以换行符结尾。

**--type** _type_
> 强制指定类型：js、html、css。

**-f** _file_
> 输入文件。

**--config** _file_
> 配置文件。

# DESCRIPTION

**js-beautify** 以一致的缩进和风格格式化 JavaScript、HTML 和 CSS 文件。它非常适合整理压缩过的代码或强制统一的代码风格。

该工具为每种语言提供独立命令（js-beautify、html-beautify、css-beautify），也可以根据扩展名自动检测语言类型。

# CONFIGURATION

```json
// .jsbeautifyrc
{
  "indent_size": 2,
  "indent_with_tabs": false,
  "end_with_newline": true,
  "brace_style": "collapse"
}
```

# CAVEATS

在边缘情况下可能改变代码语义。大文件处理可能较慢。不做代码校验。配置优先级规则可能比较复杂。

# HISTORY

js-beautify 由 **Einar Lielmanis** 最初开发为一个在线工具，后来扩展为命令行工具和库。它被广泛用于代码格式化和还原压缩代码。

# INSTALL

```brew: brew install js-beautify```

```nix: nix profile install nixpkgs#js-beautify```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prettier](/man/prettier)(1), [eslint](/man/eslint)(1)

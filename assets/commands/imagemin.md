# TAGLINE

图像优化工具

# TLDR

**就地压缩图片**

```imagemin [images/*] --out-dir=[images]```

**压缩到不同目录**

```imagemin [src/images/*] --out-dir=[dist/images]```

**使用指定插件**

```imagemin [images/*] --plugin=pngquant --out-dir=[output]```

**设置质量**

```imagemin [images/*] --plugin.mozjpeg.quality=80 --out-dir=[output]```

# SYNOPSIS

**imagemin** [_options_] _files_

# PARAMETERS

**--out-dir**, **-o** _dir_
> 输出目录。

**--plugin** _name_
> 使用指定插件。

**--plugin.**_name_._option_
> 插件选项。

# DESCRIPTION

**imagemin** 是一个图像优化工具。它借助各种插件压缩 PNG、JPEG、GIF 和 SVG 图像，同时保持视觉质量。

它常用于构建流水线中，为 Web 应用减小图片文件体积，在不明显损失质量的情况下提升加载速度。

# PLUGINS

```
imagemin-mozjpeg     JPEG optimization
imagemin-pngquant    PNG optimization
imagemin-gifsicle    GIF optimization
imagemin-svgo        SVG optimization
imagemin-webp        WebP conversion
```

# NODE.JS USAGE

```javascript
const imagemin = require('imagemin');
const mozjpeg = require('imagemin-mozjpeg');

await imagemin(['images/*.jpg'], {
  destination: 'dist/images',
  plugins: [mozjpeg({quality: 75})]
});
```

# CAVEATS

需要 Node.js。插件需单独安装。有损压缩会降低质量。使用相同的 out-dir 时原始文件会被覆盖。

# HISTORY

imagemin 作为一个基于 Node.js 的图像优化工具集诞生。它为各种图像压缩算法提供统一接口，在 Web 开发工作流中广受欢迎。

# SEE ALSO

[optipng](/man/optipng)(1), [jpegoptim](/man/jpegoptim)(1), [svgo](/man/svgo)(1)

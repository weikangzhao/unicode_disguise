# unicode 伪装者
可以将密文隐藏在掩体的伪装下的编解码器, 你的所见可能并不是所得.
原理来源于[https://github.com/paulgb/emoji-encoder](https://github.com/paulgb/emoji-encoder), 简单来说unicode每4个字节中可以藏一个0-255的数, 这些位置应该是预留的没有实际作用的空位, 他们自然也不会被渲染出来, 但是会被复制粘贴传递.
本项目将其原理用python实现, 并且为了方便使用, 增加了和剪切板交互. 使用也更加方便, 毕竟大家都喜欢python.
# 用法
现在你可以将任意文本复制到剪切板, 然后运行
`python unicode_encoder.py -e`, 程序会将剪切板中的数据读出, 进行编码, 并把结果写入剪切板.
你可以将被加密的文本复制到剪切板, 然后运行
`python unicode_encoder.py -d`, 程序会将剪切板中的数据读出, 进行解码, 并把结果写入剪切板.
默认的掩体文本(也就是编码之后渲染出来给第三方看的文本)是'😀', 实际上你可以任意指定掩体文本, 通过-b 参数
`python unicode_encoder.py -e -b abc`
解码并不需要指定掩体文本, 算法会自动解码
# 环境
平台: windows
pandas包用于读写剪切板, 如果你的python环境没有pandas, 使用pip install pandas安装
# 扩展
如果你觉得密文不够隐蔽, 或许可以考虑使用rsa或者其他算法提前加密, 再用本编码器进行伪装. 玩的开心

# unicode disguise
A codec that can hide ciphertext under cover of disguise, so what you see may not be what you get.
The principle comes from [https://github.com/paulgb/emoji-encoder](https://github.com/paulgb/emoji-encoder)
This project implements its principle in Python, and adds interaction with the clipboard for ease of use.
# usage
Now you can copy any text to the clipboard and run
`python unicode_encoder.py -e`, the program will read the data in the clipboard, encode it, and write the result to the clipboard.
You can copy the encrypted text to the clipboard and then run
`python unicode_encoder.py -d`, the program will read the data in the clipboard, decode it, and write the result to the clipboard.
The default cover text (the text that is rendered after encoding for third parties to see) is '😀'. You can actually specify any cover text by using the -b parameter:
`python unicode_encoder.py -e -b abc`
You don't need to specify the cover text for decoding, the algorithm will automatically decode it
# environment
Platform: Windows
The pandas package is used to read and write the clipboard. If your Python environment does not have pandas, use pip install pandas to install it.
# more
If you think the ciphertext is not hidden enough, you may consider using RSA or other algorithms to encrypt in advance, and then use this encoder to disguise it. Have fun

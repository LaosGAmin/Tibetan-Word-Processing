
"""
30个辅音
"""
consonant_list = [0x0f40, 0x0f41, 0x0f42, 0x0f44, 0x0f45, 0x0f46, 0x0f47, 0x0f49, 0x0f4f, 0x0f50,
                  0x0f51, 0x0f53, 0x0f54, 0x0f55, 0x0f56, 0x0f58, 0x0f59, 0x0f5a, 0x0f5b, 0x0f5d,
                  0x0f5e, 0x0f5f, 0x0f60, 0x0f61, 0x0f62, 0x0f63, 0x0f64, 0x0f66, 0x0f67, 0x0f68]

"""
四个元音
"""
vowel = [0x0f72, 0x0f74, 0x0f7a, 0x0f7c]

"""
包含了30个辅音以及4个元音的原始字符
"""
const_list = [
        0x0f40, 0x0f41, 0x0f42, 0x0f44, 0x0f45, 0x0f46, 0x0f47, 0x0f49, 0x0f4f, 0x0f50,
        0x0f51, 0x0f53, 0x0f54, 0x0f55, 0x0f56, 0x0f58, 0x0f59, 0x0f5a, 0x0f5b, 0x0f5d,
        0x0f5e, 0x0f5f, 0x0f60, 0x0f61, 0x0f62, 0x0f63, 0x0f64, 0x0f66, 0x0f67, 0x0f68,
        0x0f72, 0x0f74, 0x0f7a, 0x0f7c]

"""
上加字的表，每一行的第一列是上加字本身，其余列为本行的上加字可以跟的基字
"""
up_table = [
        [0x0f62, 0x0f40, 0x0f42, 0x0f44, 0x0f47, 0x0f49, 0x0f4f, 0x0f51, 0x0f53, 0x0f56, 0x0f58, 0x0f59, 0x0f5b],
        [0x0f63, 0x0f40, 0x0f42, 0x0f44, 0x0f45, 0x0f47, 0x0f4f, 0x0f51, 0x0f54, 0x0f56, 0x0f67],
        [0x0f66, 0x0f40, 0x0f42, 0x0f44, 0x0f49, 0x0f4f, 0x0f51, 0x0f53, 0x0f54, 0x0f56, 0x0f58, 0x0f59],
    ]

"""
下加字的表，每一行的第一列是下加字本身，其余列为本行的上加字可以跟的基字
"""
down_table = [
        [0x0f61, 0x0f40, 0x0f41, 0x0f42, 0x0f54, 0x0f55, 0x0f56, 0x0f58],
        [0x0f62, 0x0f40, 0x0f41, 0x0f42, 0x0f45, 0x0f50, 0x0f51, 0x0f54, 0x0f55, 0x0f56, 0x0f66, 0x0f67],
        [0x0f63, 0x0f40, 0x0f41, 0x0f56, 0x0f5f, 0x0f62, 0x0f66],
    ]

"""
某一个具体下加字"ཝ"因为跟的字符可能是两个字符, (好像也没法加前加字), 故单独列出
down_table_special的后三行各表示一个字, 每一行的后两个要上下叠加起来，然后再添加下加字
down_table_special的第一行跟普通的table没什么不同
"""
down_table_special = [
    [0x0f5d, 0x0f40, 0x0f41, 0x0f42, 0x0f49, 0x0f51, 0x0f5a, 0x0f5e, 0x0f5f, 0x0f62, 0x0f63, 0x0f64, 0x0f67],
    [0x0f5d, 0x0f62, 0x0f59],
    [0x0f5d, 0x0f42, 0x0f62],
    [0x0f5d, 0x0f55, 0x0f61],
]

"""
三重叠加字符表，每一行的第一列为上加字，第二列为下加字，其余的各列为所在行的基字
"""
triple_word = [
        [0x0f62, 0x0f61, 0x0f40, 0x0f42, 0x0f58],
        [0x0f66, 0x0f61, 0x0f40, 0x0f42, 0x0f54, 0x0f56, 0x0f58],
        [0x0f66, 0x0f62, 0x0f40, 0x0f42, 0x0f53, 0x0f54, 0x0f56, 0x0f58],
    ]

"""
半前加字表，每一行的第一列是前加字本身，其余列为本行的前加字可以跟的基字，
值得注意的是这个表中之记录了基字为任意形态的情况，后面我会介绍用来创建基字存在上加字或下加字的完整表
"""
pre_table = [
        [0x0f42, 0x0f45, 0x0f49, 0x0f4f, 0x0f51, 0x0f53, 0x0f59, 0x0f5e, 0x0f5f, 0x0f61, 0x0f64, 0x0f66],
        [0x0f51, 0x0f40, 0x0f42, 0x0f44, 0x0f54, 0x0f56, 0x0f58],
        [0x0f56, 0x0f40, 0x0f42, 0x0f45, 0x0f4f, 0x0f51, 0x0f59, 0x0f5e, 0x0f5f, 0x0f64, 0x0f66],
        [0x0f58, 0x0f41, 0x0f42, 0x0f44, 0x0f46, 0x0f47, 0x0f49, 0x0f50, 0x0f51, 0x0f53, 0x0f5a, 0x0f5b],
        [0x0f60, 0x0f41, 0x0f42, 0x0f46, 0x0f47, 0x0f50, 0x0f51, 0x0f55, 0x0f56, 0x0f5a, 0x0f5b],
    ]

"""
全前加字表，主要用来生成'前加字+下加字+基字'以及'前加字+上加字+基字'的基础字
"""
pre_table_whole = [
        [0x0f42, 0x0f45, 0x0f49, 0x0f4f, 0x0f51, 0x0f53, 0x0f59, 0x0f5e, 0x0f5f, 0x0f61, 0x0f64, 0x0f66],
        [0x0f51, 0x0f40, 0x0f42, 0x0f44, 0x0f54, 0x0f56, 0x0f58],
        [0x0f56, 0x0f40, 0x0f42, 0x0f44, 0x0f45, 0x0f47, 0x0f49, 0x0f4f, 0x0f51, 0x0f53, 0x0f59, 0x0f5b, 0x0f5e, 0x0f5f,
         0x0f62, 0x0f64, 0x0f66],
        [0x0f58, 0x0f41, 0x0f42, 0x0f44, 0x0f46, 0x0f47, 0x0f49, 0x0f50, 0x0f51, 0x0f53, 0x0f5a, 0x0f5b],
        [0x0f60, 0x0f41, 0x0f42, 0x0f46, 0x0f47, 0x0f50, 0x0f51, 0x0f55, 0x0f56, 0x0f5a, 0x0f5b],
    ]

"""
可任意组合的9个后加字
"""
after_table = [0x0f42, 0x0f44, 0x0f51, 0x0f53, 0x0f56, 0x0f58, 0x0f62, 0x0f63, 0x0f66]

"""
再后加字表，每一行的第一列为再后加字，其余列为本行的后加字
"""
after_after_table = [
        [0x0f51, 0x0f53, 0x0f62, 0x0f63],
        [0x0f66, 0x0f42, 0x0f44, 0x0f56, 0x0f58],
    ]

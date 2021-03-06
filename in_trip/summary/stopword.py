# -*- coding: utf-8 -*-
stop_words = set([
u"、",
u"。",
u"“",
u"”",
u"《",
u"》",
u"！",
u"｜",
u"，",
u"：",
u"；",
u"？",
u"（",
u"）",
u"［",
u"］",
u"｛",
u"｝",
u"／",
u"＊",
u"＆",
u"……",
u"％",
u"＄",
u"＃",
u"＠",
u"～",
u"｀",
u"＜",
u"＞",
u"啊",
u"阿",
u"哎",
u"哎呀",
u"哎哟",
u"唉",
u"俺",
u"俺们",
u"按",
u"按照",
u"吧",
u"吧哒",
u"把",
u"罢了",
u"被",
u"本",
u"本着",
u"比",
u"比方",
u"比如",
u"鄙人",
u"彼",
u"彼此",
u"边",
u"别",
u"别的",
u"别说",
u"并",
u"并且",
u"不比",
u"不成",
u"不单",
u"不但",
u"不独",
u"不管",
u"不光",
u"不过",
u"不仅",
u"不拘",
u"不论",
u"不怕",
u"不然",
u"不如",
u"不特",
u"不惟",
u"不问",
u"不只",
u"朝",
u"朝着",
u"趁",
u"趁着",
u"乘",
u"冲",
u"除",
u"除此之外",
u"除非",
u"除了",
u"此",
u"此间",
u"此外",
u"从",
u"从而",
u"打",
u"待",
u"但",
u"但是",
u"当",
u"当着",
u"到",
u"得",
u"的",
u"的话",
u"等",
u"等等",
u"地",
u"第",
u"叮咚",
u"对",
u"对于",
u"多",
u"多少",
u"而",
u"而况",
u"而且",
u"而是",
u"而外",
u"而言",
u"而已",
u"尔后",
u"反过来",
u"反过来说",
u"反之",
u"非但",
u"非徒",
u"否则",
u"嘎",
u"嘎登",
u"该",
u"赶",
u"个",
u"各",
u"各个",
u"各位",
u"各种",
u"各自",
u"给",
u"根据",
u"跟",
u"故",
u"故此",
u"固然",
u"关于",
u"管",
u"归",
u"果然",
u"果真",
u"过",
u"哈",
u"哈哈",
# u"呵",
u"和",
u"何",
u"何处",
u"何况",
u"何时",
u"嘿",
u"哼",
u"哼唷",
u"呼哧",
u"乎",
u"哗",
u"还是",
u"还有",
u"换句话说",
u"换言之",
u"或",
u"或是",
u"或者",
u"极了",
u"及",
u"及其",
u"及至",
u"即",
u"即便",
u"即或",
u"即令",
u"即若",
u"即使",
u"几",
u"几时",
u"己",
u"既",
u"既然",
u"既是",
u"继而",
u"加之",
u"假如",
u"假若",
u"假使",
u"鉴于",
u"将",
u"较",
u"较之",
u"叫",
u"接着",
u"结果",
u"借",
u"紧接着",
u"进而",
u"尽",
u"尽管",
u"经",
u"经过",
u"就",
u"就是",
u"就是说",
u"据",
u"具体地说",
u"具体说来",
u"开始",
u"开外",
u"靠",
u"咳",
u"可",
u"可见",
u"可是",
u"可以",
u"况且",
u"啦",
u"来",
u"来着",
u"离",
u"例如",
u"哩",
u"连",
u"连同",
u"两者",
u"了",
u"临",
u"另",
u"另外",
u"另一方面",
u"论",
u"嘛",
u"吗",
u"慢说",
u"漫说",
u"冒",
u"么",
u"每",
u"每当",
u"们",
u"莫若",
u"某",
u"某个",
u"某些",
u"拿",
u"哪",
u"哪边",
u"哪儿",
u"哪个",
u"哪里",
u"哪年",
u"哪怕",
u"哪天",
u"哪些",
u"哪样",
u"那",
u"那边",
u"那儿",
u"那个",
u"那会儿",
u"那里",
u"那么",
u"那么些",
u"那么样",
u"那时",
u"那些",
u"那样",
u"乃",
u"乃至",
u"呢",
u"能",
u"你",
u"你们",
u"您",
u"宁",
u"宁可",
u"宁肯",
u"宁愿",
u"哦",
u"呕",
u"啪达",
u"旁人",
u"呸",
u"凭",
u"凭借",
u"其",
u"其次",
u"其二",
u"其他",
u"其它",
u"其一",
u"其余",
u"其中",
u"起",
u"起见",
u"起见",
u"岂但",
u"恰恰相反",
u"前后",
u"前者",
u"且",
u"然而",
u"然后",
u"然则",
u"让",
u"人家",
u"任",
u"任何",
u"任凭",
u"如",
u"如此",
u"如果",
u"如何",
u"如其",
u"如若",
u"如上所述",
u"若",
u"若非",
u"若是",
u"啥",
u"上下",
u"尚且",
u"设若",
u"设使",
u"甚而",
u"甚么",
u"甚至",
u"省得",
u"时候",
u"什么",
u"什么样",
u"使得",
u"是",
u"是的",
u"首先",
u"谁",
u"谁知",
u"顺",
u"顺着",
u"似的",
u"虽",
u"虽然",
u"虽说",
u"虽则",
u"随",
u"随着",
u"所",
u"所以",
u"他",
u"他们",
u"他人",
u"它",
u"它们",
u"她",
u"她们",
u"倘",
u"倘或",
u"倘然",
u"倘若",
u"倘使",
u"腾",
u"替",
u"通过",
u"同",
u"同时",
u"哇",
u"万一",
u"往",
u"望",
u"为",
u"为何",
u"为了",
u"为什么",
u"为着",
u"喂",
u"嗡嗡",
u"我",
u"我们",
u"呜",
u"呜呼",
u"乌乎",
u"无论",
u"无宁",
u"毋宁",
u"嘻",
u"吓",
u"相对而言",
u"像",
u"向",
u"向着",
u"嘘",
u"呀",
u"焉",
u"沿",
u"沿着",
u"要",
u"要不",
u"要不然",
u"要不是",
u"要么",
u"要是",
u"也",
u"也罢",
u"也好",
u"一",
u"一般",
u"一旦",
u"一方面",
u"一来",
u"一切",
u"一样",
u"一则",
u"依",
u"依照",
u"矣",
u"以",
u"以便",
u"以及",
u"以免",
u"以至",
u"以至于",
u"以致",
u"抑或",
u"因",
u"因此",
u"因而",
u"因为",
u"哟",
u"用",
u"由",
u"由此可见",
u"由于",
u"有",
u"有的",
u"有关",
u"有些",
u"又",
u"于",
u"于是",
u"于是乎",
u"与",
u"与此同时",
u"与否",
u"与其",
u"越是",
u"云云",
u"哉",
u"再说",
u"再者",
u"在",
u"在下",
u"咱",
u"咱们",
u"则",
u"怎",
u"怎么",
u"怎么办",
u"怎么样",
u"怎样",
u"咋",
u"照",
u"照着",
u"者",
u"这",
u"这边",
u"这儿",
u"这个",
u"这会儿",
u"这就是说",
u"这里",
u"这么",
u"这么点儿",
u"这么些",
u"这么样",
u"这时",
u"这些",
u"这样",
u"正如",
u"吱",
u"之",
u"之类",
u"之所以",
u"之一",
u"只是",
u"只限",
u"只要",
u"只有",
u"至",
u"至于",
u"诸位",
u"着",
u"着呢",
u"自",
u"自从",
u"自个儿",
u"自各儿",
u"自己",
u"自家",
u"自身",
u"综上所述",
u"总的来看",
u"总的来说",
u"总的说来",
u"总而言之",
u"总之",
u"纵",
u"纵令",
u"纵然",
u"纵使",
u"遵照",
u"作为",
u"兮",
u"呃",
u"呗",
u"咚",
u"咦",
u"喏",
u"啐",
u"喔唷",
u"嗬",
u"嗯",
# u"嗳",
])

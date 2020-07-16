from s_m import loop_m
import config


def news_1():
    loop_m('ТУРУРУ\nПоследние новости\nРано утром 7 июля недалеко от планеты в районе Молокова произошло самоубийство'
           ' молодой девушки. Предположительно, она была в состоянии алкогольного опьянения и решали принять ванну.'
           ' В последние заснула, тем самым утонула. Но местные жителе говорят, что не так давно у неё были стычки '
           'с людьми. Может ли это значить, что это было запланированное убийство, а не случайность? Мы можем только'
           ' догадываться. А пока дело на рассмотрение дали детективу Павлу',
           None, config.TOKEN_JOURNALIST)


def news_2():
    loop_m('ТУРУРУ\nНовости, срочные новости\nВ 11:30 местного времени, на улице Алексеева 33 был найден труп '
           'мужчины 40 лет. Смерть наступила от переизбытка свинца в его голове. Пуля вылетела с правой стороны виска. '
           'Неизвестно,что заставило его пойти на самоубийство, но накануне этого происшествия Никита Арсеньевич'
           ' был очень взволнован. Родственники утверждают ,что это было убийством. Юный детектив Алейников Павел'
           ' взялась за это дело, но граждане не верят в её успех.', None, config.TOKEN_JOURNALIST)


def news_3():
    loop_m('ТУРУРУ\nНовости, срочные новости\nРешив помыть окно,будьте аккуратным Этот совет пригодился бы Анне Эйснер.'
           ' Сегодня в 14:00 по местному времени бедная женщина выпала из окна,моя его. Она получила переломы '
           'несовместимые с жизнью. Очевидица предполагает,что это не было случайностью. Наш бравый,конечно же в '
           'кавычках, детектив Павел не упустил возможности взяться за это дело, ведь местные газеты уже '
           'называют его не состоявшимся детективом.', None, config.TOKEN_JOURNALIST)


def news_4():
    loop_m('ТУРУРУ\nНовости,срочные новости\nВоздух-это жизнь, с этим утверждением героиня сегодняшнего эпизода знакома'
           ' не понаслышке. В 17:30 по местному времени Была найдена мёртвая девушка, результатом её смерти стала'
           ' асфиксия,по сообщениям полиции у девушки были раны от инъекций, находящиеся прямо на венах, и пена вокруг'
           ' рта. Послужила ли передозировка для смерти девушки, это нам поможет узнать шутка ,ой извините наш '
           'много уважаемый детектив Алейников Павел. Его главный девиз по жизни: попытка не пытка.',
           None, config.TOKEN_JOURNALIST)


def news_5():
    loop_m('ТУРУРУ\nНовости,срочные новости\nВ 19:00 по местному времени,в результате передозировки инсулином '
           'скончался Морозин Владислав Дмитриевич. Что???? На место преступления приехал Алейников Павел. Многие'
           ' в городе называют его самым неудачным детективом за всё время существования этой уважаемой профессии. И он'
           ' смог подтвердить это своими расследованиями. Почти все родственники и друзья потерпевших обвиняют нашего'
           ' неудавшегося детектива, не слишком много ли взяла он на себя. Порой лучше сдаться и оставить дело '
           'настоящим профессионалам.', None, config.TOKEN_JOURNALIST)


def news_end1():
    loop_m('ТУРУРУ Новости,срочные новости. Убийца пойман. Полиция ликует,весь город рад триумфу нашего детектива.'
           ' Алеников Павел смога закрыть рты всем,кто сомневался в нём, и доказать что'
           ' он настоящий профессионал!!!', None, config.TOKEN_JOURNALIST)


def news_end2():
    loop_m('ТУРУРУ Новости,срочные новости. Комиссар был уволен из-за недостаточной раскрываемости дел. Убийца так и '
           'не был найден. Сегодня был найден труп всеми знакомого детектива-Алейникова Павла. ОН может и'
           ' был неплохим человеком, но как же он плохо расследовал дела.', None, config.TOKEN_JOURNALIST)
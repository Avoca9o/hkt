import base64
import utils.utils as utils
from utils.utils import get_base64_encoded_image
import logging
# пути к картинкам банков
TBANK_IMAGE = 'mock_images/tbank.jpg'
YA_PAY_IMAGE = 'mock_images/ya_pay.jpg'
ALPHA_IMAGE = 'mock_images/alpha_logo.jpg'
SBER_IMAGE = 'mock_images/sber_logo.png'
VTB_IMAGE = 'mock_images/vtb_logo.jpg'

# пути к картинкам конкретных кешбэков
ASHAN_IMAGE = 'mock_images/ashan.jpg'
BRISTOL_IMAGE = 'mock_images/bristol.jpg'
DETMIR_IMAGE = 'mock_images/detmir.png'
FARSH_IMAGE = 'mock_images/farsh.png'
KASHA_IMAGE = 'mock_images/kasha.png'
KB_IMAGE = 'mock_images/kb.jpg'
KHLEB_IMAGE = 'mock_images/khleb.png'
LENTA_IMAGE = 'mock_images/lenta.png'
LETUAL_IMAGE = 'mock_images/letual.png'
MAGNIT_IMAGE = 'mock_images/magnit.jpg'
MASLO_IMAGE = 'mock_images/maslo.png'
MOLOKO_IMAGE = 'mock_images/moloko.png'
OLIVKOVOE_MASLO_IMAGE = 'mock_images/olivkovoe_maslo.png'
PEREKRESTOK_IMAGE = 'mock_images/perekrestok.png'
PODRUZHKA_IMAGE = 'mock_images/podruzhka.png'
POMODORO_IMAGE = 'mock_images/pomodoro.png'
PYATEROCHKA_IMAGE = 'mock_images/pyaterochka.png'
RIV_GOSH_IMAGE = 'mock_images/riv_gosh.png'
SAHAR_IMAGE = 'mock_images/sahar.png'
SMETANA_IMAGE = 'mock_images/smetana.png'
SOCHEN_IMAGE = 'mock_images/sochen.png'
SPAR_IMAGE = 'mock_images/spar.jpg'
TVOROG_IMAGE = 'mock_images/tvorog.png'
VINLAB_IMAGE = 'mock_images/vinlab.png'
VKUSVILL_IMAGE = 'mock_images/vkusvill.jpg'
YAYICA_IMAGE = 'mock_images/yayica.png'
ZOLOTOYE_YABLOKO_IMAGE = 'mock_images/zolotoye_yabloko.png'
PIDZHAK_IMAGE = 'mock_images/pidzhak.jpg'
TUFLI_IMAGE = 'mock_images/tufli.jpg'
IPHONE_IMAGE = 'mock_images/iphone.jpeg'
PYLESOS_IMAGE = 'mock_images/pylesos.jpg'
ROSES_IMAGE = 'mock_images/roses.jpg'
TULIPS_IMAGE = 'mock_images/tulips.jpg'
AVIASALES_IMAGE = 'mock_images/aviasales.png'
AVITO_IMAGE = 'mock_images/avito.jpeg'

# банковские идентификаторы
TBANK_BIK = 00000000
YA_PAY_BIK = 11111111
ALPHA_BIK = 22222222
SBER_BIK = 33333333
VTB_BIK = 44444444


def mock_search():
    # картинки с банками
    base64_tbank_image = get_base64_encoded_image(TBANK_IMAGE)
    base64_ya_pay_image = get_base64_encoded_image(YA_PAY_IMAGE)
    base64_alpha_image = get_base64_encoded_image(ALPHA_IMAGE)
    base64_sber_image = get_base64_encoded_image(SBER_IMAGE)
    base64_vtb_image = get_base64_encoded_image(VTB_IMAGE)

    # картинки с конкретными предложениями
    base64_ashan_image = get_base64_encoded_image(ASHAN_IMAGE)
    base64_bristol_image = get_base64_encoded_image(BRISTOL_IMAGE)
    base64_detmir_image = get_base64_encoded_image(DETMIR_IMAGE)
    base64_farsh_image = get_base64_encoded_image(FARSH_IMAGE)
    base64_kasha_image = get_base64_encoded_image(KASHA_IMAGE)
    base64_kb_image = get_base64_encoded_image(KB_IMAGE)
    base64_khleb_image = get_base64_encoded_image(KHLEB_IMAGE)
    base64_lenta_image = get_base64_encoded_image(LENTA_IMAGE)
    base64_letual_image = get_base64_encoded_image(LETUAL_IMAGE)
    base64_magnit_image = get_base64_encoded_image(MAGNIT_IMAGE)
    base64_maslo_image = get_base64_encoded_image(MASLO_IMAGE)
    base64_moloko_image = get_base64_encoded_image(MOLOKO_IMAGE)
    base64_olivkovoye_maslo_image = get_base64_encoded_image(OLIVKOVOE_MASLO_IMAGE)
    base64_perekrestok_image = get_base64_encoded_image(PEREKRESTOK_IMAGE)
    base64_podruzhka_image = get_base64_encoded_image(PODRUZHKA_IMAGE)
    base64_pomodoro_image = get_base64_encoded_image(POMODORO_IMAGE)
    base64_pyaterochka_image = get_base64_encoded_image(PYATEROCHKA_IMAGE)
    base64_riv_gosh_image = get_base64_encoded_image(RIV_GOSH_IMAGE)
    base64_sahar_image = get_base64_encoded_image(SAHAR_IMAGE)
    base64_smetana_image = get_base64_encoded_image(SMETANA_IMAGE)
    base64_sochen_image = get_base64_encoded_image(SOCHEN_IMAGE)
    base64_spar_image = get_base64_encoded_image(SPAR_IMAGE)
    base64_tvorog_image = get_base64_encoded_image(TVOROG_IMAGE)
    base64_vinlab_image = get_base64_encoded_image(VINLAB_IMAGE)
    base64_vkusvill_image = get_base64_encoded_image(VKUSVILL_IMAGE)
    base64_yayica_image = get_base64_encoded_image(YAYICA_IMAGE)
    base64_zolotoye_yabloko_image = get_base64_encoded_image(ZOLOTOYE_YABLOKO_IMAGE)
    base64_pidzhak_image = get_base64_encoded_image(PIDZHAK_IMAGE)
    base64_tufli_image = get_base64_encoded_image(TUFLI_IMAGE)
    base64_iphone_image = get_base64_encoded_image(IPHONE_IMAGE)
    base64_pylesos_image = get_base64_encoded_image(PYLESOS_IMAGE)
    base64_roses_image = get_base64_encoded_image(ROSES_IMAGE)
    base64_tulips_image = get_base64_encoded_image(TULIPS_IMAGE)
    base64_aviasales_image = get_base64_encoded_image(AVIASALES_IMAGE)
    base64_avito_image = get_base64_encoded_image(AVITO_IMAGE)

    result = [
        {
            'header': '5% на супермаркеты зарплатным клиентам',
            'description': 'Кешбэк для всех новых пользователей до 23 октября',
            'category': 'Супермаркеты',
            'image': base64_ashan_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 300 рублей на красное вино',
            'description': 'Всем новым пользователям предоставляется скидка на первый заказ онлайн в сервисе Яндекс.Еда',
            'category': 'Супермаркеты',
            'image': base64_bristol_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 5% на настольные игры',
            'description': 'Получите кешбэк 5% на настольные игры! Покупайте любимые игры и возвращайте часть потраченных средств, чтобы обновить свою коллекцию',
            'category': 'Настольные игры',
            'image': base64_detmir_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 5000 рублей на покупку костюмов для вкладчиков',
            'description': 'Кешбэк 5000 рублей на пиджаки — это отличная возможность обновить свой гардероб! Кешбэк доступен всем клиентам ВТБ, у кого открыт вклад в размере от 50 тысяч рублей',
            'category': 'Одежда',
            'image': base64_pidzhak_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 5% на новый iphone',
            'description': 'Кешбэк 5% на новый iphone — это неплохая возможность сэкономить при покупке одного из самых популярных смартфонов на рынке',
            'category': 'Техника',
            'image': base64_iphone_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 20% на розы',
            'description': 'Кешбэк 20% на розы — это отличная возможность порадовать себя и своих близких, не выходя за рамки бюджета! При покупке роз вы можете вернуть 20% от суммы, что делает каждую покупку более выгодной',
            'category': 'Цветы',
            'image': base64_roses_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 4% на покупку авиабилетов',
            'description': 'Планируйте свои путешествия с удовольствием и получайте 4% кешбэка на покупку авиабилетов! Наслаждайтесь новыми открытиями и экономьте на своих поездках',
            'category': 'Путешествия',
            'image': base64_aviasales_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк до 100% на говяжий фарш',
            'description': 'Верните полную стоимость при покупке от двух пачек',
            'category': 'Продукты',
            'image': base64_farsh_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк до 3000 на iphone',
            'description': 'Кешбэк 5% на новый iphone, но до 3000 рублей только клиентам тинькофф банка в честь дня рождения',
            'category': 'Техника',
            'image': base64_iphone_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 15% на овсянку',
            'description': 'Получите кешбэк 15% на овсянку! Наслаждайтесь полезным завтраком и экономьте на покупках',
            'category': 'Продукты',
            'image': base64_kasha_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 300 рублей на доставку',
            'description': 'Получите кешбэк 300 рублей на доставку! Заказывайте любимую еду и возвращайте часть средств обратно',
            'category': 'Супермаркеты',
            'image': base64_kb_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 22% на батоны',
            'description': 'Кешбэк 22% на батоны! Покупайте свежие батоны и возвращайте часть средств обратно!',
            'category': 'Продукты',
            'image': base64_khleb_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 200 рублей на сникерсы',
            'description': 'Кешбэк 200 рублей на сникерсы (при покупке 20 штук)! Наслаждайтесь любимыми сладостями и получайте выгоду от покупок!',
            'category': 'Супермаркеты',
            'image': base64_lenta_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 2% на iphone в магазинах МВидео',
            'description': 'ВТБ совместно с МВидео запускают акцию в виде двухпроцентного кешбэка на продукцию смартфонов iphone для всех пользователей. Лимит покупок ограничен, условия уточняйте на сайте акции',
            'category': 'Техника',
            'image': base64_iphone_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 5% на красную помаду',
            'description': 'Кешбэк 5% на красную помаду! Придайте своим губам яркий оттенок и получайте выгоду от каждой покупки!',
            'category': 'Косметика',
            'image': base64_letual_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 7% на съём квартиры посуточно',
            'description': 'Снимайте квартиры посуточно и получайте 7% кешбэка на каждую бронирование! Наслаждайтесь комфортом домашней атмосферы во время ваших поездок и экономьте на проживании',
            'category': 'Путешествия',
            'image': base64_avito_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 100 рублей на туалетную бумагу',
            'description': 'Покупая туалетную бумагу, вы можете сэкономить! Получите кешбэк 100 рублей на эту необходимую продукцию и наслаждайтесь выгодными покупками!',
            'category': 'Супермаркеты',
            'image': base64_magnit_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 200 рублей на туфли',
            'description': 'Кешбэк 200 рублей на туфли — это хорошая возможность сэкономить при покупке новой пары обуви! Туфли могут быть как классическими, так и более современными, в зависимости от вашего стиля и предпочтений',
            'category': 'Одежда',
            'image': base64_tufli_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 7% на пылесос',
            'description': 'Кешбэк 7% на пылесос — это выгодное предложение, позволяющее сэкономить на покупке бытовой техники',
            'category': 'Техника',
            'image': base64_pylesos_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 10% на тюльпаны',
            'description': 'Покупая тюльпаны, вы не только наполняете свой дом яркими красками, но и получаете 10% кешбэка! Подарите себе и своим близким радость весны, сэкономив при этом',
            'category': 'Цветы',
            'image': base64_tulips_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 7% на подсолнечное масло Золотая Семечка',
            'description': 'Покупая подсолнечное масло Золотая Семечка, вы можете вернуть 7% от потраченной суммы. Сделайте свои покупки более выгодными и экономьте на каждом шагу',
            'category': 'Продукты',
            'image': base64_maslo_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 3% на пастеризованное молоко',
            'description': 'При покупке пастеризованного молока вы можете получить кешбэк в размере 3%. Это поможет вам сократить расходы на повседневные продукты',
            'category': 'Продукты',
            'image': base64_moloko_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 12% на оливковое масло',
            'description': 'При приобретении оливкового масла можно воспользоваться кешбэком в размере 12%. Это отличная возможность снизить затраты на покупку качественных продуктов',
            'category': 'Продукты',
            'image': base64_olivkovoye_maslo_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 4% на продукцию собственного производства',
            'description': 'При покупке продукции собственного производства вы можете получить кешбэк в размере 4%. Это может стать хорошим способом сэкономить на товарах, которые часто используются в повседневной жизни',
            'category': 'Супермаркеты',
            'image': base64_perekrestok_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 9% на тушь для ресниц',
            'description': 'Кешбэк в размере 9% доступен на тушь для ресниц. Это отличная возможность не только обновить свою косметичку, но и сэкономить на покупках',
            'category': 'Косметика',
            'image': base64_podruzhka_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 6% на помидоры',
            'description': 'Кешбэк в размере 6% предлагается на помидоры. Это замечательный способ поддержать здоровое питание и сэкономить на свежих овощах',
            'category': 'Продукты',
            'image': base64_pomodoro_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 8% на выпечку',
            'description': 'Кешбэк 8% на выпечку – отличный способ насладиться любимыми хлебобулочными изделиями и сэкономить на покупках',
            'category': 'Супермаркеты',
            'image': base64_pyaterochka_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 2% на крем для рук',
            'description': 'Кешбэк 2% на крем для рук – хорошая возможность ухаживать за кожей и получать небольшую выгоду от покупок',
            'category': 'Косметика',
            'image': base64_riv_gosh_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 60% на cахарный песок',
            'description': 'Кешбэк 60% на сахарный песок – отличная возможность сэкономить на покупке этого необходимого продукта',
            'category': 'Продукты',
            'image': base64_sahar_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 13% на сметану',
            'description': 'Кешбэк 13% на сметану – хороший способ сэкономить на покупке этого вкусного и полезного продукта',
            'category': 'Продукты',
            'image': base64_smetana_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 80% на сочни с творогом',
            'description': 'Кешбэк 80% на сочни с творогом – это замечательная возможность насладиться вкусной выпечкой и значительно сэкономить на покупке! Не упустите шанс побаловать себя и своих близких!',
            'category': 'Продукты',
            'image': base64_sochen_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 200 рублей на спаржу',
            'description': 'Кешбэк 200 рублей на спаржу – отличное предложение для любителей этого полезного овоща! Это не только возможность сэкономить, но и шанс добавить в свой рацион вкусное и питательное блюдо.',
            'category': 'Супермаркеты',
            'image': base64_spar_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        },
        {
            'header': 'Кешбэк 40% на творог',
            'description': 'Кешбэк 40% на творог – отличная возможность приобрести этот полезный продукт и сэкономить! Творог богат белком и кальцием, что делает его прекрасным выбором для здорового питания. Не упустите шанс воспользоваться этим предложением!',
            'category': 'Продукты',
            'image': base64_tvorog_image,
            'bank_image': base64_alpha_image,
            'bic': ALPHA_BIK
        },
        {
            'header': 'Кешбэк 350 рублей на водку',
            'description': 'Кешбэк 350 рублей на водку – это заманчивое предложение для тех, кто планирует покупку этого напитка. Однако всегда стоит помнить о разумном потреблении алкоголя',
            'category': 'Продукты',
            'image': base64_vinlab_image,
            'bank_image': base64_sber_image,
            'bic': SBER_BIK
        },
        {
            'header': 'Кешбэк 12% на фрукты',
            'description': 'Кешбэк 12% на фрукты – это отличная возможность сэкономить на покупке свежих и полезных продуктов! Фрукты богаты витаминами и минералами, и их стоит включать в свой рацион',
            'category': 'Супермаркеты',
            'image': base64_vkusvill_image,
            'bank_image': base64_vtb_image,
            'bic': VTB_BIK
        },
        {
            'header': 'Кешбэк 9% на яйца С0',
            'description': 'Кешбэк 9% на яйца — это хорошая возможность сэкономить на покупке этого полезного продукта. Яйца являются отличным источником белка и других питательных веществ',
            'category': 'Супермаркеты',
            'image': base64_yayica_image,
            'bank_image': base64_tbank_image,
            'bic': TBANK_BIK
        },
        {
            'header': 'Кешбэк 700 рублей на средства для ухода за волосами',
            'description': 'Кешбэк 700 рублей на средства для ухода за волосами — это отличная возможность сэкономить на продуктах, которые помогут поддерживать здоровье и красоту ваших волос. Вы можете использовать этот кешбэк для покупки шампуней, кондиционеров, масок или стайлинговых средств',
            'category': 'Косметика',
            'image': base64_zolotoye_yabloko_image,
            'bank_image': base64_ya_pay_image,
            'bic': YA_PAY_BIK
        }
    ]

    return result


def search(session: str, text):
    res = mock_search()

    if text is not None and len(text) > 0:
        res = utils.filter_response(text, res)

    return res


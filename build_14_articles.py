# -*- coding: utf-8 -*-
import re
import json

METADATA = [
    # Article 1
    {
        "slug": "pest-control-prices-apartments-villas",
        "category": "اسعار وباقات مكافحة الحشرات",
        "readTime": "9 دقائق",
        "date": "1 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80",
        "author": "م. فهد القحطاني",
        "authorRole": "استشاري التسعير والوقاية - حصن المملكة",
        "keywords": [
            "اسعار مكافحة الحشرات",
            "اسعار مكافحة الحشرات للشقق والفلل",
            "تكلفة مكافحة الحشرات بالرياض",
            "اسعار شركات رش المنازل",
            "اسعار مكافحة الحشرات ورش المبيدات بالرياض",
            "اسعار شركات مكافحة الحشرات بالدمام",
            "كم تكلفة واسعار مكافحة الحشرات في جدة",
            "اسعار مكافحة الصراصير والبق والنمل الابيض"
        ],
        "relatedServices": [
            {"title": "مكافحة الصراصير", "href": "/services/cockroaches"},
            {"title": "رش النمل الأبيض", "href": "/services/termites"},
            {"title": "إبادة بق الفراش", "href": "/services/bedbugs"},
            {"title": "باقات الأسعار والتكلفة", "href": "/#pricing"}
        ],
        "relatedPests": [
            {"title": "الصراصير الألمانية", "href": "/pests/cockroach-german"},
            {"title": "بق الفراش", "href": "/pests/bedbug"},
            {"title": "النمل الأبيض", "href": "/pests/termite"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "الدمام", "href": "/city/dammam"}
        ]
    },
    # Article 2
    {
        "slug": "best-pest-spray-types-flying-crawling",
        "category": "المبيدات الحشرية والأدوات",
        "readTime": "8 دقائق",
        "date": "2 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?auto=format&fit=crop&w=1200&q=80",
        "author": "م. عبدالله الشمري",
        "authorRole": "أخصائي مبيدات آفات الصحة العامة",
        "keywords": [
            "بخاخ الحشرات",
            "أفضل أنواع بخاخات الحشرات",
            "افضل بخاخ حشرات للمنازل بالرياض",
            "بخاخ طارد الحشرات الطائرة والزاحفة في مكة",
            "رشاش مبيد الحشرات",
            "بخاخ الصراصير",
            "بخاخ النمل",
            "بخاخ حشرات الفراش"
        ],
        "relatedServices": [
            {"title": "مكافحة الصراصير", "href": "/services/cockroaches"},
            {"title": "مكافحة الحشرات الطائرة", "href": "/services/gardens"},
            {"title": "إبادة بق الفراش", "href": "/services/bedbugs"}
        ],
        "relatedPests": [
            {"title": "الصراصير الألمانية", "href": "/pests/cockroach-german"},
            {"title": "بق الفراش", "href": "/pests/bedbug"},
            {"title": "النمل الأبيض", "href": "/pests/termite"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "مكة المكرمة", "href": "/city/makkah"},
            {"name": "جدة", "href": "/city/jeddah"}
        ]
    },
    # Article 3
    {
        "slug": "best-pest-control-company-homes-villas",
        "category": "إرشادات ومعايير الشركات",
        "readTime": "10 دقائق",
        "date": "3 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80",
        "author": "م. ياسر الغامدي",
        "authorRole": "كبير مهندسي المكافحة المتكاملة",
        "keywords": [
            "افضل شركة مكافحة حشرات",
            "افضل شركة رش مبيدات",
            "أفضل شركات مكافحة الحشرات",
            "أفضل شركة ابادة حشرات",
            "دليل افضل شركة مكافحة حشرات بالدمام والخبر",
            "ارقام افضل شركة مكافحة حشرات بمكة المكرمة مرخصة",
            "مكافحة الحشرات قبل الانتقال إلى منزل جديد"
        ],
        "relatedServices": [
            {"title": "مكافحة شاملة للفلل والمنازل", "href": "/#services"},
            {"title": "عقود المنشآت والمطاعم", "href": "/services/commercial"},
            {"title": "مكافحة النمل الأبيض", "href": "/services/termites"}
        ],
        "relatedPests": [
            {"title": "النمل الأبيض", "href": "/pests/termite"},
            {"title": "الصراصير", "href": "/pests/cockroach-german"},
            {"title": "بق الفراش", "href": "/pests/bedbug"}
        ],
        "relatedCities": [
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "مكة المكرمة", "href": "/city/makkah"},
            {"name": "الرياض", "href": "/city/riyadh"}
        ]
    },
    # Article 4
    {
        "slug": "booking-pest-control-service-riyadh",
        "category": "خدمات وحجوزات الرياض",
        "readTime": "8 دقائق",
        "date": "3 أكتوبر 2026",
        "region": "central",
        "city": "الرياض",
        "image": "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?auto=format&fit=crop&w=1200&q=80",
        "author": "م. فهد القحطاني",
        "authorRole": "مدير العمليات الميدانية - الرياض",
        "keywords": [
            "حجز خدمة مكافحة الحشرات بالرياض",
            "خدمة مكافحة الحشرات",
            "أفضل خدمة مكافحة الحشرات بجدة",
            "خدمة مكافحة حشرات الصرف الصحي والمطابخ بالدمام",
            "رقم خدمة مكافحة الحشرات المعتمدة في مكة",
            "خدمة رش ومكافحة الحشرات في الطائف والهدا",
            "تكلفة خدمة مكافحة الحشرات"
        ],
        "relatedServices": [
            {"title": "مكافحة الحشرات بالرياض", "href": "/city/riyadh"},
            {"title": "مكافحة الصراصير بالمطابخ", "href": "/services/cockroaches"},
            {"title": "رش النمل الأبيض", "href": "/services/termites"}
        ],
        "relatedPests": [
            {"title": "صراصير الصرف والمجاري", "href": "/pests/cockroach-german"},
            {"title": "بق الفراش", "href": "/pests/bedbug"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "الطائف", "href": "/city/taif"}
        ]
    },
    # Article 5
    {
        "slug": "pest-control-companies-residential-buildings",
        "category": "المباني والمجمعات السكنية",
        "readTime": "9 دقائق",
        "date": "4 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1200&q=80",
        "author": "م. عبدالعزيز المطيري",
        "authorRole": "مستشار الوقاية الإنشائية للمباني السكنية",
        "keywords": [
            "شركات مكافحة الحشرات للمباني السكنية",
            "مكافحة الحشرات للشقق المشتركة",
            "شركات مبيدات الحشرات",
            "ارقام شركات رش الحشرات",
            "افضل شركات مكافحة الحشرات الدمام",
            "شركات مكافحة الحشرات في الاحساء والهفوف",
            "عروض شركات مكافحة الحشرات للمباني"
        ],
        "relatedServices": [
            {"title": "مكافحة شاملة للمباني", "href": "/#services"},
            {"title": "عقود المنشآت والمجمعات", "href": "/services/commercial"},
            {"title": "مكافحة حشرات الصرف", "href": "/services/cockroaches"}
        ],
        "relatedPests": [
            {"title": "الصراصير الألمانية", "href": "/pests/cockroach-german"},
            {"title": "بق الفراش", "href": "/pests/bedbug"},
            {"title": "الفئران والقوارض", "href": "/pests/rodents-rats"}
        ],
        "relatedCities": [
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "الأحساء", "href": "/city/ahsa"},
            {"name": "الرياض", "href": "/city/riyadh"}
        ]
    },
    # Article 6
    {
        "slug": "pest-cleanup-sanitization-after-infestation",
        "category": "التنظيف والتعقيم بعد المكافحة",
        "readTime": "9 دقائق",
        "date": "4 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80",
        "author": "م. خالد الزهراني",
        "authorRole": "أخصائي التعقيم البيئي والصحة العامة",
        "keywords": [
            "شركة تنظيف حشرات المنازل",
            "تنظيف حشرات",
            "شركة تنظيف حشرات وتعقيم المنازل بالرياض",
            "شركة تنظيف ورش مبيدات",
            "تنظيف وتعقيم المطبخ من الصراصير في جدة",
            "تنظيف وتعقيم اسطح ونوافذ المنازل من فضلات الحمام بمكة",
            "تنظيف اثار الحشرات من الاثاث والمفروشات"
        ],
        "relatedServices": [
            {"title": "مكافحة الصراصير", "href": "/services/cockroaches"},
            {"title": "مكافحة الحمام والطيور", "href": "/services/birds"},
            {"title": "إبادة بق الفراش", "href": "/services/bedbugs"}
        ],
        "relatedPests": [
            {"title": "الصراصير", "href": "/pests/cockroach-german"},
            {"title": "الحمام والطيور", "href": "/pests/pigeons"},
            {"title": "بق الفراش", "href": "/pests/bedbug"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "مكة المكرمة", "href": "/city/makkah"}
        ]
    },
    # Article 7
    {
        "slug": "home-pest-control-spray-by-infestation-type",
        "category": "المبيدات الحشرية والأدوات",
        "readTime": "10 دقائق",
        "date": "5 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80",
        "author": "م. عبدالله الشمري",
        "authorRole": "استشاري سموم وبيئة الآفات",
        "keywords": [
            "شركة رش مبيدات الحشرات المنزلية",
            "مبيدات الحشرات المنزلية",
            "مبيدات حشرية منزلية",
            "أفضل مبيدات حشرية منزلية آمنة في الرياض",
            "مبيد حشري بدون رائحة للمنازل في الدمام",
            "أسعار مبيدات الحشرات المنزلية مكة",
            "الفرق بين شراء المبيد وطلب خدمة المكافحة"
        ],
        "relatedServices": [
            {"title": "رش الصراصير بالجل", "href": "/services/cockroaches"},
            {"title": "مكافحة النمل الأبيض", "href": "/services/termites"},
            {"title": "إبادة بق الفراش", "href": "/services/bedbugs"}
        ],
        "relatedPests": [
            {"title": "الصراصير الألمانية", "href": "/pests/cockroach-german"},
            {"title": "بق الفراش", "href": "/pests/bedbug"},
            {"title": "النمل الأبيض", "href": "/pests/termite"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "مكة المكرمة", "href": "/city/makkah"}
        ]
    },
    # Article 8
    {
        "slug": "gecko-lizard-control-prevent-entry",
        "category": "مكافحة الزواحف والآفات",
        "readTime": "9 دقائق",
        "date": "5 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1504450758481-7338eba7524a?auto=format&fit=crop&w=1200&q=80",
        "author": "م. طارق العتيبي",
        "authorRole": "أخصائي مكافحة الزواحف والآفات المنزلية",
        "keywords": [
            "مكافحة الابراص",
            "مكافحة الوزغ",
            "شركة مكافحة الوزغ والأبراص بالرياض",
            "أفضل طريقة للتخلص من البرص في جدة",
            "مبيد للابراص",
            "مكافحة الأبراص والزواحف في المدينة المنورة",
            "حماية الابواب والنوافذ من دخول الابراص"
        ],
        "relatedServices": [
            {"title": "مكافحة الزواحف والعقارب", "href": "/services/scorpions-snakes"},
            {"title": "مكافحة الحشرات الطائرة", "href": "/services/gardens"},
            {"title": "رش شامل للمنازل", "href": "/#services"}
        ],
        "relatedPests": [
            {"title": "العقارب والثعابين", "href": "/pests/scorpions"},
            {"title": "الصراصير", "href": "/pests/cockroach-german"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "المدينة المنورة", "href": "/city/madinah"}
        ]
    },
    # Article 9
    {
        "slug": "mosquito-control-gardens-rest-houses",
        "category": "مكافحة الحشرات الطائرة",
        "readTime": "9 دقائق",
        "date": "6 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1558904541-efa8c4a08931?auto=format&fit=crop&w=1200&q=80",
        "author": "م. سلطان الحربي",
        "authorRole": "خبير رش الحدائق ومكافحة نواقل الأمراض",
        "keywords": [
            "شركة مكافحة البعوض",
            "مكافحة الناموس",
            "مبيد الناموس",
            "شركة رش الناموس والبعوض بجدة للحدائق والمسابح",
            "رش البعوض في الرياض بجهاز الضباب الحراري",
            "أفضل شركة مكافحة البعوض والحشرات الطائرة بالدمام",
            "رش مبيدات الناموس في جازان وصبيا",
            "أسعار شركات رش الناموس للمزارع بالقصيم"
        ],
        "relatedServices": [
            {"title": "مكافحة حشرات الحدائق والمسابح", "href": "/services/gardens"},
            {"title": "رش الحشرات بالضباب الحراري", "href": "/#services"},
            {"title": "عقود المزارع والاستراحات", "href": "/services/commercial"}
        ],
        "relatedPests": [
            {"title": "البعوض ونواقل الأمراض", "href": "/pests/rodents-rats"},
            {"title": "الذباب", "href": "/pests/cockroach-german"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "جازان", "href": "/city/jazan-najran"},
            {"name": "بريدة والقصيم", "href": "/city/qassim"}
        ]
    },
    # Article 10
    {
        "slug": "pigeon-control-window-ac-protection",
        "category": "مكافحة الطيور والحمام",
        "readTime": "10 دقائق",
        "date": "6 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=1200&q=80",
        "author": "م. حسام الدوسري",
        "authorRole": "مهندس حماية الواجهات وطرد الطيور",
        "keywords": [
            "شركة مكافحة الحمام",
            "طارد الحمام",
            "شركة تركيب طوارد الحمام بالرياض",
            "أفضل شركة مكافحة الحمام والطيور بجدة",
            "مبيد حشرات الحمام والتعامل مع الفاش",
            "تركيب شبك حمام للمكيفات في مكة المكرمة",
            "فني تركيب أشواك طرد الحمام بالدمام ستانلس ستيل",
            "شركة طرد الحمام من النوافذ في الخرج والدلم"
        ],
        "relatedServices": [
            {"title": "تركيب طارد الحمام وشبك النوافذ", "href": "/services/birds"},
            {"title": "تنظيف وتعقيم واجهات المباني", "href": "/#services"},
            {"title": "مكافحة حشرات الفاش والعتة", "href": "/services/bedbugs"}
        ],
        "relatedPests": [
            {"title": "الحمام والطيور البرية", "href": "/pests/pigeons"},
            {"title": "حشرات الفاش والبراغيث", "href": "/pests/bedbug"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "مكة المكرمة", "href": "/city/makkah"},
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "الخرج", "href": "/city/kharj"}
        ]
    },
    # Article 11
    {
        "slug": "fly-control-homes-kitchens-commercial",
        "category": "مكافحة الحشرات الطائرة",
        "readTime": "9 دقائق",
        "date": "7 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=1200&q=80",
        "author": "م. ياسر الغامدي",
        "authorRole": "استشاري مكافحة آفات المطاعم والمنشآت الغذائية",
        "keywords": [
            "شركة مكافحة الذباب",
            "مكافحة الذباب",
            "شركة رش ومكافحة الذباب في الرياض",
            "أفضل طرق مكافحة الذباب المنزلي في جدة",
            "طارد الذباب",
            "شركة القضاء على الذباب في الأحساء",
            "مبيد للذباب بدون رائحه",
            "تركيب صواعق ومصائد الذباب للمطاعم"
        ],
        "relatedServices": [
            {"title": "مكافحة الحشرات بالمطاعم والمنشآت", "href": "/services/commercial"},
            {"title": "مكافحة الحشرات الطائرة والحدائق", "href": "/services/gardens"},
            {"title": "رش المطابخ والصرف", "href": "/services/cockroaches"}
        ],
        "relatedPests": [
            {"title": "الذباب المنزلي", "href": "/pests/cockroach-german"},
            {"title": "البعوض", "href": "/pests/rodents-rats"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "الأحساء", "href": "/city/ahsa"}
        ]
    },
    # Article 12
    {
        "slug": "mice-rat-control-inside-homes-prevention",
        "category": "مكافحة القوارض والفئران",
        "readTime": "10 دقائق",
        "date": "7 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1425082661705-1834bfd09dca?auto=format&fit=crop&w=1200&q=80",
        "author": "م. عادل الشهري",
        "authorRole": "خبير إبادة القوارض والتحصين الميكانيكي",
        "keywords": [
            "شركة مكافحة الفئران داخل المنازل",
            "مكافحة الفئران",
            "شركة مكافحة الفئران بالرياض",
            "رقم شركة صيد الفئران والقوارض بجدة",
            "أفضل شركة إبادة جرذان وفئران في الدمام والخبر",
            "مكافحة الفئران في الخرج للمنازل",
            "سد فتحات دخول الفئران",
            "أسعار مكافحة القوارض وسد الفتحات بالمدينة المنورة"
        ],
        "relatedServices": [
            {"title": "إبادة الفئران والقوارض ومحطات الطعوم", "href": "/services/rodents"},
            {"title": "سد الفتحات والتحصين الميكانيكي", "href": "/#services"},
            {"title": "مكافحة حشرات المستودعات والمخازن", "href": "/services/commercial"}
        ],
        "relatedPests": [
            {"title": "الفئران والجرذان", "href": "/pests/rodents-rats"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "الخرج", "href": "/city/kharj"},
            {"name": "المدينة المنورة", "href": "/city/madinah"}
        ]
    },
    # Article 13
    {
        "slug": "methods-pest-rodent-control-inside-homes",
        "category": "مكافحة الحشرات والآفات",
        "readTime": "9 دقائق",
        "date": "8 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80",
        "author": "م. فهد القحطاني",
        "authorRole": "كبير استشاريي المكافحة المتكاملة",
        "keywords": [
            "طرق مكافحة الحشرات والقوارض داخل المنازل",
            "مكافحة الحشرات والقوارض",
            "شركة مكافحة الحشرات والقوارض بالرياض",
            "أفضل شركة إبادة حشرات وقوارض في جدة",
            "أسعار مكافحة الحشرات والقوارض في الدمام والظهران",
            "شركة مكافحة الحشرات والقوارض في الخرج",
            "رش الحشرات ومكافحة القوارض بالقصيم"
        ],
        "relatedServices": [
            {"title": "مكافحة القوارض", "href": "/services/rodents"},
            {"title": "مكافحة الصراصير", "href": "/services/cockroaches"},
            {"title": "إبادة بق الفراش", "href": "/services/bedbugs"}
        ],
        "relatedPests": [
            {"title": "القوارض والفئران", "href": "/pests/rodents-rats"},
            {"title": "الصراصير", "href": "/pests/cockroach-german"},
            {"title": "بق الفراش", "href": "/pests/bedbug"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "القصيم", "href": "/city/qassim"},
            {"name": "الخرج", "href": "/city/kharj"}
        ]
    },
    # Article 14
    {
        "slug": "public-health-pest-control-homes-facilities",
        "category": "آفات الصحة العامة والمنشآت",
        "readTime": "10 دقائق",
        "date": "8 أكتوبر 2026",
        "region": "general",
        "image": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80",
        "author": "م. سامي السبيعي",
        "authorRole": "استشاري مكافحة آفات الصحة العامة والامتثال الصحي",
        "keywords": [
            "مكافحة افات الصحة العامة",
            "المكافحة المتكاملة للآفات",
            "شركة مكافحة آفات بالرياض معتمدة",
            "أفضل شركات مكافحة الآفات الزراعية والمنزلية بجدة",
            "مكافحة آفات الصحة العامة بالدمام والخبر",
            "شركة مكافحة الآفات والقوارض بمكة المكرمة",
            "بروتوكول مكافحة الآفات للمطاعم والمنشآت بالمدينة المنورة",
            "أسعار مكافحة الآفات"
        ],
        "relatedServices": [
            {"title": "عقود المطاعم والمنشآت المعتمدة", "href": "/services/commercial"},
            {"title": "مكافحة حشرات الصحة العامة", "href": "/#services"},
            {"title": "مكافحة القوارض", "href": "/services/rodents"}
        ],
        "relatedPests": [
            {"title": "الصراصير الألمانية والأمريكية", "href": "/pests/cockroach-german"},
            {"title": "فئران المجاري", "href": "/pests/rodents-rats"},
            {"title": "بق الفراش", "href": "/pests/bedbug"}
        ],
        "relatedCities": [
            {"name": "الرياض", "href": "/city/riyadh"},
            {"name": "جدة", "href": "/city/jeddah"},
            {"name": "الدمام", "href": "/city/dammam"},
            {"name": "مكة المكرمة", "href": "/city/makkah"},
            {"name": "المدينة المنورة", "href": "/city/madinah"}
        ]
    }
]

def split_raw_articles(raw_text):
    # Splits by top-level markdown heading: # **...**
    pattern = r'(?=(?:^|\n)# \*\*[^\n]+\*\*)|(?=(?:^|\n)# [^\n]+)'
    articles_raw = re.split(pattern, raw_text.strip())
    articles_clean = [a.strip() for a in articles_raw if a.strip()]
    return articles_clean

with open('data/raw_articles_part1.md', 'r', encoding='utf-8') as f:
    part1_text = f.read()

with open('data/raw_articles_part2.md', 'r', encoding='utf-8') as f:
    part2_text = f.read()

articles_part1 = split_raw_articles(part1_text)
articles_part2 = split_raw_articles(part2_text)
all_raw_articles = articles_part1 + articles_part2

print(f"Total extracted articles: {len(all_raw_articles)}")
assert len(all_raw_articles) == 14, f"Expected 14 articles, got {len(all_raw_articles)}"

processed_posts = []

for idx, (raw_art, meta) in enumerate(zip(all_raw_articles, METADATA)):
    lines = raw_art.split('\n')
    # First line is title
    title_line = lines[0].strip()
    title_match = re.search(r'# \*\*([^*]+)\*\*', title_line)
    if not title_match:
        title_match = re.search(r'# (.*)', title_line)
    title = title_match.group(1).strip() if title_match else title_line.replace('#', '').strip()

    # Find paragraphs before first '##' to build excerpt
    body_lines = lines[1:]
    intro_paras = []
    current_para = []
    for line in body_lines:
        if line.strip().startswith('##'):
            break
        if line.strip():
            current_para.append(line.strip())
        else:
            if current_para:
                intro_paras.append(' '.join(current_para))
                current_para = []
    if current_para:
        intro_paras.append(' '.join(current_para))

    # Excerpt
    full_intro = ' '.join(intro_paras)
    # clean markdown links in excerpt
    clean_excerpt = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', full_intro)
    clean_excerpt = clean_excerpt.replace('**', '').replace('*', '').strip()
    # take up to ~250 chars
    if len(clean_excerpt) > 280:
        clean_excerpt = clean_excerpt[:277] + '...'

    # Parse FAQs
    # Look for '## الأسئلة الشائعة' section
    faq_list = []
    faq_match = re.search(r'## \*\*?الأسئلة الشائعة\*\*?.*?\n(.*)', raw_art, re.DOTALL)
    if faq_match:
        faq_text = faq_match.group(1)
        faq_blocks = re.findall(r'### \*\*?([^\n*?]+)\*?\*?\s*\n+([^#]+)', faq_text)
        for q, a in faq_blocks:
            q_clean = q.replace('**', '').replace('*', '').strip()
            a_clean = a.strip()
            # Clean trailing whitespace/newlines
            faq_list.append({"q": q_clean, "a": a_clean})

    # Table of contents: Extract ## and ### headings (excluding TOC itself)
    toc_items = []
    heading_idx = 1
    for line in lines:
        h2_m = re.match(r'^## \*\*?([^*#]+)\*?\*?', line)
        if h2_m:
            h_title = h2_m.group(1).strip()
            if 'فهرس المحتويات' not in h_title and 'Table of Contents' not in h_title:
                h_id = f"heading-{heading_idx}"
                heading_idx += 1
                toc_items.append({
                    "id": h_id,
                    "title": h_title,
                    "level": 2
                })
        else:
            h3_m = re.match(r'^### \*\*?([^*#]+)\*?\*?', line)
            if h3_m:
                h_title = h3_m.group(1).strip()
                # Don't include FAQ subquestions in main TOC to avoid bloating
                if 'الأسئلة الشائعة' not in raw_art[:raw_art.find(line)]:
                    h_id = f"heading-{heading_idx}"
                    heading_idx += 1
                    toc_items.append({
                        "id": h_id,
                        "title": h_title,
                        "level": 3
                    })

    # Content: We keep markdown body starting after title
    # Remove TOC block from content if present, or keep clean
    content = '\n'.join(body_lines).strip()

    post_data = {
        "id": f"post-new-14-{idx+1}",
        "slug": meta["slug"],
        "title": title,
        "excerpt": clean_excerpt,
        "readTime": meta["readTime"],
        "date": meta["date"],
        "category": meta["category"],
        "region": meta["region"],
        "city": meta.get("city", "عام لكافة مناطق المملكة"),
        "pestType": "مكافحة الآفات والحشرات",
        "image": meta["image"],
        "author": meta["author"],
        "authorRole": meta["authorRole"],
        "keywords": meta["keywords"],
        "tableOfContents": toc_items,
        "content": content,
        "faqList": faq_list,
        "relatedServices": meta["relatedServices"],
        "relatedPests": meta["relatedPests"],
        "relatedCities": meta["relatedCities"]
    }
    processed_posts.append(post_data)

print("Writing data/added_articles.ts ...")
with open('data/added_articles.ts', 'w', encoding='utf-8') as out_f:
    out_f.write("import type { BlogPost } from './blog';\n\n")
    out_f.write("export const ADDED_ARTICLES: BlogPost[] = ")
    json.dump(processed_posts, out_f, ensure_ascii=False, indent=2)
    out_f.write(";\n")

print("Successfully generated data/added_articles.ts with 14 articles!")

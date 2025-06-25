from dotenv import load_dotenv

from amocrm.models import Lead


json = {
  "id": 39060590,
  "name": "4.05 в 11.00 могут пораньше только 165 школа",
  "price": 0,
  "responsible_user_id": 10727737,
  "group_id": 495437,
  "status_id": 61095973,
  "pipeline_id": 7341297,
  "loss_reason_id": None,
  "created_by": 11060341,
  "updated_by": 0,
  "created_at": 1746183082,
  "updated_at": 1746421930,
  "closed_at": None,
  "closest_task_at": 1777482000,
  "is_deleted": False,
  "custom_fields_values": [
    {
      "field_id": 691118,
      "field_name": "Отделение",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "РО",
          "enum_id": 1132548,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 680015,
      "field_name": "Цель обращения",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "Поступление",
          "enum_id": 1122363,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 693664,
      "field_name": "Время встречи",
      "field_code": None,
      "field_type": "date_time",
      "values": [
        {
          "value": 1746338400
        }
      ]
    },
    {
      "field_id": 691102,
      "field_name": "Фамилия ученика",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "Алишев"
        }
      ]
    },
    {
      "field_id": 691104,
      "field_name": "Имя ученика",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "Мансур"
        }
      ]
    },
    {
      "field_id": 799670,
      "field_name": "Время напоминание о встрече",
      "field_code": None,
      "field_type": "date_time",
      "values": [
        {
          "value": 1746282600
        }
      ]
    },
    {
      "field_id": 798802,
      "field_name": "Доп. инфо. об уч.",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "Рано пошел в школу, стеснительный и закрытый, в садик не ходил и адаптация в школу было тяжелаЯ, хотят в ниш, занимается шахматами, любит естествознание, география,  НАДО РАСКРЫТЬ ЕГО, ПРОБЛЕМЫ С КАЗ, ЯЗ. интенсив в апреле акцент на бил а не рфмш"
        }
      ]
    },
    {
      "field_id": 798854,
      "field_name": "Откуда узнали про нас?",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "Рекомендация",
          "enum_id": 1151740,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691010,
      "field_name": "ФИО родителя",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "АЛИШЕВ АБАЙ"
        }
      ]
    },
    
    {
      "field_id": 798158,
      "field_name": "Теги проставлены",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "Да",
          "enum_id": 1150774,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691106,
      "field_name": "Дата рождения ученика",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1401818400
        }
      ]
    },
    {
      "field_id": 691108,
      "field_name": "Номер телефона родителя",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "+7 701 788 4453"
        }
      ]
    },
    {
      "field_id": 691110,
      "field_name": "Номер Whatsapp родителя",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "+7 701 788 4453"
        }
      ]
    },
    {
      "field_id": 691124,
      "field_name": "В школе учится",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "После обеда",
          "enum_id": 1132574,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691126,
      "field_name": "Вид занятий",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "Групповое",
          "enum_id": 1132576,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691128,
      "field_name": "Предметы",
      "field_code": None,
      "field_type": "multiselect",
      "values": [
        {
          "value": "Математика",
          "enum_id": 1132582,
          "enum_code": None
        },
        {
          "value": "Английский язык",
          "enum_id": 1132586,
          "enum_code": None
        },
        {
          "value": "Русский язык",
          "enum_id": 1132588,
          "enum_code": None
        },
        {
          "value": "Казахский язык",
          "enum_id": 1132590,
          "enum_code": None
        },
        {
          "value": "Логика",
          "enum_id": 1132592,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691132,
      "field_name": "Дни обучения",
      "field_code": None,
      "field_type": "multiselect",
      "values": [
        {
          "value": "Вт",
          "enum_id": 1132610,
          "enum_code": None
        },
        {
          "value": "Чт",
          "enum_id": 1132614,
          "enum_code": None
        },
        {
          "value": "Сб",
          "enum_id": 1132618,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691134,
      "field_name": "Филиал",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "г. Алматы, Тимирязева 42к 10А (4 этаж)",
          "enum_id": 1132622,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691136,
      "field_name": "Время обучения",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "9:00 - 12:05",
          "enum_id": 1132628,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691138,
      "field_name": "Цель обучения",
      "field_code": None,
      "field_type": "multiselect",
      "values": [
        {
          "value": "Подготовка к НИШ",
          "enum_id": 1132634,
          "enum_code": None
        },
        {
          "value": "Подготовка к БИЛ (КТЛ)",
          "enum_id": 1132638,
          "enum_code": None
        },
        {
          "value": "Подготовка к 165 Лицею",
          "enum_id": 1132640,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 790262,
      "field_name": "Номер УДВ родителя",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "038239079"
        }
      ]
    },
    {
      "field_id": 790264,
      "field_name": "ИИН родителя",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "790826300569"
        }
      ]
    },
    {
      "field_id": 691142,
      "field_name": "Выдано кем?",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "МВД РК",
          "enum_id": 1132654,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691144,
      "field_name": "Дата выдачи УДВ",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1437674400
        }
      ]
    },
    {
      "field_id": 691148,
      "field_name": "Срок обуч (мес)",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "12"
        }
      ]
    },
    {
      "field_id": 800320,
      "field_name": "Баз-й курс (мес)",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "9"
        }
      ]
    },
    {
      "field_id": 800322,
      "field_name": "Инт-й курс (мес)",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "3"
        }
      ]
    },
    {
      "field_id": 691152,
      "field_name": "Дата начала учебы по договору",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1754506800
        }
      ]
    },
    {
      "field_id": 691176,
      "field_name": "Дата конца учебы",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1778094000
        }
      ]
    },
    {
      "field_id": 691164,
      "field_name": "Сумма со скидкой",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "550000"
        }
      ]
    },
    {
      "field_id": 798554,
      "field_name": "Летний лагерь",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "0 мес",
          "enum_id": 1151366,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 801172,
      "field_name": "транш",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "1",
          "enum_id": 1154454,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 691166,
      "field_name": "Дата 1 транша",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1746298800
        }
      ]
    },
    {
      "field_id": 691170,
      "field_name": "Сумма 1 транша",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "550000"
        }
      ]
    },
    {
      "field_id": 775908,
      "field_name": "Включен ИНТЕНСИВ?",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "3 мес",
          "enum_id": 1156556,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 787528,
      "field_name": "Результаты тестов",
      "field_code": None,
      "field_type": "textarea",
      "values": [
        {
          "value": "МАТ 5 КАЗАХСКИЙ 1 РУССКИЙ 9  АНГЛИЙСКИЙ 3-4"
        }
      ]
    },
    {
      "field_id": 799668,
      "field_name": "Дата заключения договора",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1746298800
        }
      ]
    },
    {
      "field_id": 799680,
      "field_name": "Метод Оплаты",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "freedom",
          "enum_id": 1159698,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 799952,
      "field_name": "Новый ученик",
      "field_code": None,
      "field_type": "checkbox",
      "values": [
        {
          "value": True
        }
      ]
    },
    {
      "field_id": 800342,
      "field_name": "Банк",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "Kaspi Bank",
          "enum_id": 1153208,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 802044,
      "field_name": "Коммент ОП",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "РАСКРЫТЬ  РЕБЕНКА"
        }
      ]
    },
    {
      "field_id": 802046,
      "field_name": "Статус Ученика",
      "field_code": None,
      "field_type": "multiselect",
      "values": [
        {
          "value": "Новый",
          "enum_id": 1157424,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 802428,
      "field_name": "Город клиента",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "АЛМАТЫ"
        }
      ]
    },
    {
      "field_id": 802474,
      "field_name": "Программирование и список",
      "field_code": None,
      "field_type": "select",
      "values": [
        {
          "value": "Нет",
          "enum_id": 1158486,
          "enum_code": None
        }
      ]
    },
    {
      "field_id": 801632,
      "field_name": "количество попыток анкета",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "8"
        }
      ]
    },
    {
      "field_id": 799422,
      "field_name": "Анкета для договора",
      "field_code": None,
      "field_type": "url",
      "values": [
        {
          "value": "https://forms.amocrm.ru/rvrvdlw?dp=Q1zaSQHqO-hHArUG1UMtpUoLDbi1z2ygdS8XlnzZDFDUShegbSJSLtxJ8s4L1zdP"
        }
      ]
    },
    {
      "field_id": 801554,
      "field_name": "Document_link",
      "field_code": None,
      "field_type": "text",
      "values": [
        {
          "value": "https://drive.google.com/uc?id=1qgsB0sdKgAMWo2OulEsPaSf75trx_IIz&export=download"
        }
      ]
    },
    {
      "field_id": 799494,
      "field_name": "customer_id",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "30294"
        }
      ]
    },
    {
      "field_id": 799528,
      "field_name": "tariff_id",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "42201"
        }
      ]
    },
    {
      "field_id": 799692,
      "field_name": "Количество дней заморозок",
      "field_code": None,
      "field_type": "numeric",
      "values": [
        {
          "value": "54"
        }
      ]
    },
    {
      "field_id": 799946,
      "field_name": "Дата начало интенсив",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1769886000
        }
      ]
    },
    {
      "field_id": 799948,
      "field_name": "Дата конец интенсив",
      "field_code": None,
      "field_type": "date",
      "values": [
        {
          "value": 1777489200
        }
      ]
    },
    {
      "field_id": 799672,
      "field_name": "Время продления",
      "field_code": None,
      "field_type": "date_time",
      "values": [
        {
          "value": 1777485600
        }
      ]
    }
  ],
  "score": None,
  "account_id": 23221876,
  "labor_cost": None,
  "_links": {
    "self": {
      "href": "https://teslakz.amocrm.ru/api/v4/leads/39060590?page=1&limit=250"
    }
  },
  "_embedded": {
    "tags": [
      {
        "id": 530830,
        "name": "FB/SS/ребенок опередит сверстников/eln/24.04/alm",
        "color": None
      }
    ],
    "companies": []
  }
}

lead = Lead.from_json(json)
print(lead.payment.parent.name)
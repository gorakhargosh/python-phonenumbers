"""Auto-generated file, do not edit by hand. RU metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_RU = PhoneMetadata(id='RU', country_code=7, international_prefix='8~10',
    general_desc=PhoneNumberDesc(national_number_pattern='[3489]\\d{9}', possible_number_pattern='\\d{10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:3(?:0[12]|4[1-35-79]|5[1-3]|8[1-58]|9[0145])|4(?:01|1[1356]|2[13467]|7[1-5]|8[1-7]|9[1-689])|8(?:1[1-8]|2[01]|3[13-6]|4[0-8]|5[15]|6[1-35-7]|7[1-37-9]))\\d{7}', possible_number_pattern='\\d{10}', example_number='3011234567'),
    mobile=PhoneNumberDesc(national_number_pattern='9\\d{9}', possible_number_pattern='\\d{10}', example_number='9123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='80[04]\\d{7}', possible_number_pattern='\\d{10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='80[39]\\d{7}', possible_number_pattern='\\d{10}', example_number='8091234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix=u'8',
    national_prefix_for_parsing=u'8',
    number_format=[NumberFormat(pattern='([3489]\\d{2})(\\d{3})(\\d{2})(\\d{2})', format=u'\\1 \\2-\\3-\\4', leading_digits_pattern=['[34689]'], national_prefix_formatting_rule=u'8 (\\1)'),
        NumberFormat(pattern='(7\\d{2})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3', leading_digits_pattern=['7'], national_prefix_formatting_rule=u'8 (\\1)')],
    main_country_for_code=True)

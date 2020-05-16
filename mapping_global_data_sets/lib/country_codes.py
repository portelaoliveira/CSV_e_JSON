from pygal_maps_world import i18n

def get_country_code(country_name): # Passa o nome do país e armazena no parâmetro country_name.
    ''' Devolve o código de duas letras do pygal para um país, dado o seu nome. '''
    for code, name in i18n.COUNTRIES.items(): # Percorre os pares de código-nome do país em COUNTRIES.
        if name == country_name: # Se o nome for encontrado, o código desse país é retornado.
            return code
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Zimbabwe':
            return 'zw'
        elif country_name == 'Zambia':
            return 'zm'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Virgin Islands (U.S.)':
            return 'do'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vanuatu':
            return 'pg'
        elif country_name == 'Uzbekistan':
            return 'uz'
        elif country_name == 'Uruguay':
            return 'uy'
        elif country_name == 'United States':
            return 'us'
        elif country_name == 'United Kingdom':
            return 'gb'
        elif country_name == 'United Arab Emirates':
            return 'ae'
        elif country_name == 'Ukraine':
            return 'ua'
        elif country_name == 'Uganda':
            return 'ug'
        elif country_name == 'Turkmenistan':
            return 'tm'
        elif country_name == 'Turkey':
            return 'tr'
        elif country_name == 'Tunisia':
            return 'tn'
        elif country_name == 'Togo':
            return 'tg'
        elif country_name == 'Timor-Leste':
            return 'tl'
        elif country_name == 'Thailand':
            return 'th'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Tajikistan':
            return 'tj'
        elif country_name == 'Syrian Arab Republic':
            return 'sy'
        elif country_name == 'Swaziland':
            return 'sz'
        elif country_name == 'Suriname':
            return 'sr'
        elif country_name == 'Sweden':
            return 'se'
        elif country_name == 'Sudan':
            return 'sd'
        elif country_name == 'Spain':
            return 'es'
        elif country_name == 'South Africa':
            return 'za'
        elif country_name == 'Somalia':
            return 'so'
        elif country_name == 'Slovenia':
            return 'si'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == '-Singapore':
            return 'sg'
        elif country_name == 'Sri Lanka':
            return 'lk'
        elif country_name == 'Sierra Leone':
            return 'sl'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Brazil':
            return 'br'
        elif country_name == 'Chile':
            return 'cl'
        elif country_name == 'China':
            return 'cn'
        elif country_name == 'Colombia':
            return 'co'
        elif country_name == 'Costa Rica':
            return 'cr'
        elif country_name == 'Cuba':
            return 'cu'
        elif country_name == 'Cyprus':
            return 'cy'
        elif country_name == 'Czech Republic':
            return 'cz'
        elif country_name == 'Denmark':
            return 'dk'
        elif country_name == '-Djibouti':
            return 'dj'
        elif country_name == 'Madagascar':
            return 'mg'
        elif country_name == 'India':
            return 'in'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Kyrgyz Republic':
            return 'kd'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
 
        # Se o país não foi encontrado, devolve None
        return None


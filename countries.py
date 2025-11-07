import pycountry


from geonamescache import GeonamesCache

import requests

import json


def CountryName_All_V1():
    for country in pycountry.countries:
        print(country.name, country.alpha_2)


def CountryName_All_V2():
    gc = GeonamesCache()
    cities = gc.get_cities()
    for city_id, city_data in cities.items():
        print(city_data["name"], city_data["countrycode"])


def CountryName_All_V3():
    url = "http://api.geonames.org/searchJSON"
    params = {
        "country": "IR",
        "featureClass": "P",
        "maxRows": 1000,
        "username": "your_username",
    }

    response = requests.get(url, params=params)
    data = response.json()

    for city in data["geonames"]:
        print(city["name"], "-", city["adminName1"])


def CountryName_All_V4(a):
    with open("countriesToCities.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    def get_cities(country_name):
        return data.get(country_name, [])

    cities = get_cities(a)
    print(cities)


# افغانستان
def Afghanistan():
    print(
        """
----Afghanistan
|
--> Kabul
|
--> Herat
|
--> Kandahar
|
--> Mazar-i-Sharif
|
--> Jalalabad
|
--> Kunduz
|
--> Ghazni
|
--> Bamyan
|
--> Khost
|
--> Farah
|
--> Baghlan
|
--> Pul-e Khumri
|
--> Lashkar Gah
|
--> Taloqan
|
--> Sheberghan
|
--> Zaranj
|
--> Fayzabad
|
--> Gardez
|
--> Charikar
"""
    )


# آلبانی
def Albania():
    print(
        """
----Albania
|
--> Tirana
|
--> Durrës
|
--> Vlorë
|
--> Shkodër
|
--> Elbasan
|
--> Fier
|
--> Berat
|
--> Korçë
|
--> Gjirokastër
|
--> Kukës
"""
    )


# الجزایر
def Algeria():
    print(
        """
----Algeria
|
--> Algiers
|
--> Oran
|
--> Constantine
|
--> Annaba
|
--> Blida
|
--> Batna
|
--> Sétif
|
--> Djelfa
|
--> Tébessa
|
--> Skikda
"""
    )


# آندورا
def Andorra():
    print(
        """
----Andorra
|
--> Andorra la Vella
|
--> Escaldes-Engordany
|
--> Encamp
|
--> La Massana
|
--> Ordino
|
--> Canillo
|
--> Sant Julià de Lòria
"""
    )


# آنگولا
def Angola():
    print(
        """
----Angola
|
--> Luanda
|
--> Huambo
|
--> Lobito
|
--> Benguela
|
--> Kuito
|
--> Lubango
|
--> Malanje
|
--> Namibe
|
--> Saurimo
|
--> Uíge
"""
    )


# آنتیگوا و باربودا
def Antigua_and_Barbuda():
    print(
        """
----Antigua and Barbuda
|
--> St. John's
|
--> All Saints
|
--> Liberta
|
--> Potter's Village
|
--> Bolans
|
--> Swetes
|
--> Seaview Farm
|
--> Pigotts
|
--> Parham
|
--> Clare Hall
"""
    )


# آرژانتین
def Argentina():
    print(
        """
----Argentina
|
--> Buenos Aires
|
--> Córdoba
|
--> Rosario
|
--> Mendoza
|
--> La Plata
|
--> San Miguel de Tucumán
|
--> Mar del Plata
|
--> Salta
|
--> Santa Fe
|
--> San Juan
"""
    )


# ارمنستان
def Armenia():
    print(
        """
----Armenia
|
--> Yerevan
|
--> Gyumri
|
--> Vanadzor
|
--> Vagharshapat
|
--> Hrazdan
|
--> Abovyan
|
--> Kapan
|
--> Ararat
|
--> Armavir
|
--> Gavar
"""
    )


# استرالیا
def Australia():
    print(
        """
----Australia
|
--> Sydney
|
--> Melbourne
|
--> Brisbane
|
--> Perth
|
--> Adelaide
|
--> Canberra
|
--> Hobart
|
--> Darwin
|
--> Gold Coast
|
--> Newcastle
"""
    )


# اتریش
def Austria():
    print(
        """
----Austria
|
--> Vienna
|
--> Graz
|
--> Linz
|
--> Salzburg
|
--> Innsbruck
|
--> Klagenfurt
|
--> Villach
|
--> Wels
|
--> Sankt Pölten
|
--> Dornbirn
"""
    )


# آذربایجان
def Azerbaijan():
    print(
        """
----Azerbaijan
|
--> Baku
|
--> Ganja
|
--> Sumqayit
|
--> Mingachevir
|
--> Lankaran
|
--> Nakhchivan
|
--> Sheki
|
--> Shirvan
|
--> Khirdalan
|
--> Shamakhi
"""
    )


# باهاما
def Bahamas():
    print(
        """
----Bahamas
|
--> Nassau
|
--> Freeport
|
--> Marsh Harbour
|
--> Coopers Town
|
--> West End
|
--> Lucaya
|
--> Alice Town
|
--> Andros Town
|
--> Clarence Town
|
--> Dunmore Town
"""
    )


# بحرین
def Bahrain():
    print(
        """
----Bahrain
|
--> Manama
|
--> Riffa
|
--> Muharraq
|
--> Hamad Town
|
--> A'ali
|
--> Sitra
|
--> Isa Town
|
--> Budaiya
|
--> Jidhafs
|
--> Diraz
"""
    )


# بنگلادش
def Bangladesh():
    print(
        """
----Bangladesh
|
--> Dhaka
|
--> Chittagong
|
--> Khulna
|
--> Rajshahi
|
--> Sylhet
|
--> Barisal
|
--> Mymensingh
|
--> Comilla
|
--> Rangpur
|
--> Bogra
"""
    )


# باربادوس
def Barbados():
    print(
        """
----Barbados
|
--> Bridgetown
|
--> Speightstown
|
--> Oistins
|
--> Holetown
|
--> Bathsheba
|
--> Saint James
|
--> Saint Michael
|
--> Saint George
|
--> Saint Philip
|
--> Saint Thomas
"""
    )


# بلاروس
def Belarus():
    print(
        """
----Belarus
|
--> Minsk
|
--> Gomel
|
--> Vitebsk
|
--> Brest
|
--> Mogilev
|
--> Grodno
|
--> Babruysk
|
--> Baranovichi
|
--> Barysaw
|
--> Pinsk
"""
    )


# بلژیک
def Belgium():
    print(
        """
----Belgium
|
--> Brussels
|
--> Antwerp
|
--> Ghent
|
--> Charleroi
|
--> Liège
|
--> Bruges
|
--> Namur
|
--> Leuven
|
--> Mons
|
--> Mechelen
"""
    )


# بلیز
def Belize():
    print(
        """
----Belize
|
--> Belize City
|
--> Belmopan
|
--> San Ignacio
|
--> Orange Walk Town
|
--> Dangriga
|
--> Corozal Town
|
--> Punta Gorda
|
--> San Pedro
|
--> Benque Viejo del Carmen
|
--> Ladyville
"""
    )


# بنین
def Benin():
    print(
        """
----Benin
|
--> Cotonou
|
--> Porto-Novo
|
--> Parakou
|
--> Djougou
|
--> Abomey
|
--> Bohicon
|
--> Kandi
|
--> Natitingou
|
--> Ouidah
|
--> Lokossa
"""
    )


# بوتان
def Bhutan():
    print(
        """
----Bhutan
|
--> Thimphu
|
--> Phuntsholing
|
--> Paro
|
--> Gelephu
|
--> Samdrup Jongkhar
|
--> Wangdue Phodrang
|
--> Punakha
|
--> Jakar
|
--> Nganglam
|
--> Samtse
"""
    )


# بولیوی
def Bolivia():
    print(
        """
----Bolivia
|
--> Santa Cruz de la Sierra
|
--> El Alto
|
--> La Paz
|
--> Cochabamba
|
--> Oruro
|
--> Sucre
|
--> Tarija
|
--> Potosí
|
--> Sacaba
|
--> Quillacollo
"""
    )


# بوسنی و هرزگوین
def Bosnia_and_Herzegovina():
    print(
        """
----Bosnia and Herzegovina
|
--> Sarajevo
|
--> Banja Luka
|
--> Tuzla
|
--> Zenica
|
--> Mostar
|
--> Bijeljina
|
--> Prijedor
|
--> Doboj
|
--> Cazin
|
--> Trebinje
"""
    )


# بوتسوانا
def Botswana():
    print(
        """
----Botswana
|
--> Gaborone
|
--> Francistown
|
--> Molepolole
|
--> Selebi-Phikwe
|
--> Maun
|
--> Serowe
|
--> Kanye
|
--> Mahalapye
|
--> Mochudi
|
--> Lobatse
"""
    )


# برزیل
def Brazil():
    print(
        """
----Brazil
|
--> São Paulo
|
--> Rio de Janeiro
|
--> Brasília
|
--> Salvador
|
--> Fortaleza
|
--> Belo Horizonte
|
--> Manaus
|
--> Curitiba
|
--> Recife
|
--> Porto Alegre
"""
    )


# برونئی
def Brunei():
    print(
        """
----Brunei
|
--> Bandar Seri Begawan
|
--> Kuala Belait
|
--> Seria
|
--> Tutong
"""
    )


# بلغارستان
def Bulgaria():
    print(
        """
----Bulgaria
|
--> Sofia
|
--> Plovdiv
|
--> Varna
|
--> Burgas
|
--> Ruse
|
--> Stara Zagora
|
--> Pleven
|
--> Sliven
|
--> Dobrich
|
--> Shumen
"""
    )


# بورکینافاسو
def Burkina_Faso():
    print(
        """
----Burkina Faso
|
--> Ouagadougou
|
--> Bobo-Dioulasso
|
--> Koudougou
|
--> Ouahigouya
|
--> Banfora
|
--> Dédougou
|
--> Kaya
|
--> Dori
|
--> Tenkodogo
|
--> Fada N'gourma
"""
    )


# بوروندی
def Burundi():
    print(
        """
----Burundi
|
--> Bujumbura
|
--> Gitega
|
--> Muyinga
|
--> Ngozi
|
--> Ruyigi
|
--> Kayanza
|
--> Bururi
|
--> Muramvya
|
--> Makamba
|
--> Rumonge
"""
    )


# کیپ ورد
def Cabo_Verde():
    print(
        """
----Cabo Verde
|
--> Praia
|
--> Mindelo
|
--> Santa Maria
|
--> Espargos
|
--> Assomada
|
--> São Filipe
|
--> Tarrafal
|
--> Pedra Badejo
|
--> Porto Novo
|
--> Sal Rei
"""
    )


# کامبوج
def Cambodia():
    print(
        """
----Cambodia
|
--> Phnom Penh
|
--> Siem Reap
|
--> Battambang
|
--> Sihanoukville
|
--> Kampong Cham
|
--> Kampot
|
--> Takeo
|
--> Pursat
|
--> Kampong Thom
|
--> Svay Rieng
"""
    )


# کامرون
def Cameroon():
    print(
        """
----Cameroon
|
--> Yaoundé
|
--> Douala
|
--> Bamenda
|
--> Bafoussam
|
--> Garoua
|
--> Maroua
|
--> Ngaoundéré
|
--> Bertoua
|
--> Kumba
|
--> Limbe
"""
    )


# کانادا
def Canada():
    print(
        """
----Canada
|
--> Toronto
|
--> Montreal
|
--> Vancouver
|
--> Calgary
|
--> Edmonton
|
--> Ottawa
|
--> Winnipeg
|
--> Quebec City
|
--> Hamilton
|
--> Halifax
"""
    )


# جمهوری آفریقای مرکزی
def Central_African_Republic():
    print(
        """
----Central African Republic
|
--> Bangui
|
--> Bimbo
|
--> Berbérati
|
--> Carnot
|
--> Bambari
|
--> Bouar
|
--> Bossangoa
|
--> Bria
|
--> Bangassou
|
--> Mbaïki
"""
    )


# چاد
def Chad():
    print(
        """
----Chad
|
--> N'Djamena
|
--> Moundou
|
--> Sarh
|
--> Abéché
|
--> Kélo
|
--> Koumra
|
--> Pala
|
--> Bongor
|
--> Mongo
|
--> Doba
"""
    )


# شیلی
def Chile():
    print(
        """
----Chile
|
--> Santiago
|
--> Puente Alto
|
--> Antofagasta
|
--> Viña del Mar
|
--> Valparaíso
|
--> Talcahuano
|
--> Temuco
|
--> Iquique
|
--> Concepción
|
--> Rancagua
"""
    )


# چین
def China():
    print(
        """
----China
|
--> Beijing
|
--> Shanghai
|
--> Guangzhou
|
--> Shenzhen
|
--> Chengdu
|
--> Chongqing
|
--> Tianjin
|
--> Wuhan
|
--> Hangzhou
|
--> Xi'an
"""
    )


# کلمبیا
def Colombia():
    print(
        """
----Colombia
|
--> Bogotá
|
--> Medellín
|
--> Cali
|
--> Barranquilla
|
--> Cartagena
|
--> Cúcuta
|
--> Bucaramanga
|
--> Pereira
|
--> Santa Marta
|
--> Ibagué
"""
    )


# کومور
def Comoros():
    print(
        """
----Comoros
|
--> Moroni
|
--> Mutsamudu
|
--> Fomboni
|
--> Domoni
|
--> Ouani
|
--> Mitsamiouli
|
--> Tsimbeo
|
--> Sima
|
--> Moya
|
--> Bandrele
"""
    )


# کنگو (برازاویل)
def Congo_Brazzaville():
    print(
        """
----Congo (Brazzaville)
|
--> Brazzaville
|
--> Pointe-Noire
|
--> Dolisie
|
--> Nkayi
|
--> Owando
|
--> Ouesso
|
--> Madingou
|
--> Gamboma
|
--> Sibiti
|
--> Kinkala
"""
    )


# کنگو (کینشاسا)
def Congo_Kinshasa():
    print(
        """
----Congo (Kinshasa)
|
--> Kinshasa
|
--> Lubumbashi
|
--> Mbuji-Mayi
|
--> Kisangani
|
--> Kananga
|
--> Bukavu
|
--> Goma
|
--> Kolwezi
|
--> Matadi
|
--> Beni
"""
    )


# کاستاریکا
def Costa_Rica():
    print(
        """
----Costa Rica
|
--> San José
|
--> Alajuela
|
--> Cartago
|
--> Heredia
|
--> Puntarenas
|
--> Limón
|
--> Liberia
|
--> San Isidro
|
--> Curridabat
|
--> Nicoya
"""
    )


# کرواسی
def Croatia():
    print(
        """
----Croatia
|
--> Zagreb
|
--> Split
|
--> Rijeka
|
--> Osijek
|
--> Zadar
|
--> Pula
|
--> Slavonski Brod
|
--> Karlovac
|
--> Varaždin
|
--> Šibenik
"""
    )


# کوبا
def Cuba():
    print(
        """
----Cuba
|
--> Havana
|
--> Santiago de Cuba
|
--> Camagüey
|
--> Holguín
|
--> Santa Clara
|
--> Guantánamo
|
--> Bayamo
|
--> Cienfuegos
|
--> Matanzas
|
--> Pinar del Río
"""
    )


# قبرس
def Cyprus():
    print(
        """
----Cyprus
|
--> Nicosia
|
--> Limassol
|
--> Larnaca
|
--> Famagusta
|
--> Paphos
|
--> Kyrenia
|
--> Strovolos
|
--> Ayia Napa
|
--> Aradippou
|
--> Paralimni
"""
    )


# جمهوری چک
def Czech_Republic():
    print(
        """
----Czech Republic
|
--> Prague
|
--> Brno
|
--> Ostrava
|
--> Plzeň
|
--> Liberec
|
--> Olomouc
|
--> České Budějovice
|
--> Hradec Králové
|
--> Pardubice
|
--> Zlín
"""
    )


# دانمارک
def Denmark():
    print(
        """
----Denmark
|
--> Copenhagen
|
--> Aarhus
|
--> Odense
|
--> Aalborg
|
--> Esbjerg
|
--> Randers
|
--> Kolding
|
--> Horsens
|
--> Vejle
|
--> Roskilde
"""
    )


# جیبوتی
def Djibouti():
    print(
        """
----Djibouti
|
--> Djibouti
|
--> Ali Sabieh
|
--> Tadjourah
|
--> Dikhil
|
--> Obock
|
--> Arta
|
--> Holhol
|
--> Balho
|
--> Yoboki
|
--> Dorra
"""
    )


# دومینیکا
def Dominica():
    print(
        """
----Dominica
|
--> Roseau
|
--> Portsmouth
|
--> Marigot
|
--> Canefield
|
--> Mahaut
|
--> Grand Bay
|
--> Castle Bruce
|
--> Wesley
|
--> La Plaine
|
--> Saint Joseph
"""
    )


# جمهوری دومینیکن
def Dominican_Republic():
    print(
        """
----Dominican Republic
|
--> Santo Domingo
|
--> Santiago
|
--> La Romana
|
--> San Pedro de Macorís
|
--> San Cristóbal
|
--> Higüey
|
--> Puerto Plata
|
--> Moca
|
--> La Vega
|
--> San Francisco de Macorís
"""
    )


# اکوادور
def Ecuador():
    print(
        """
----Ecuador
|
--> Quito
|
--> Guayaquil
|
--> Cuenca
|
--> Santo Domingo
|
--> Machala
|
--> Manta
|
--> Portoviejo
|
--> Ambato
|
--> Loja
|
--> Esmeraldas
"""
    )


# مصر
def Egypt():
    print(
        """
----Egypt
|
--> Cairo
|
--> Alexandria
|
--> Giza
|
--> Shubra El Kheima
|
--> Port Said
|
--> Suez
|
--> Mansoura
|
--> Tanta
|
--> Asyut
|
--> Ismailia
"""
    )


# السالوادور
def El_Salvador():
    print(
        """
----El Salvador
|
--> San Salvador
|
--> Santa Ana
|
--> San Miguel
|
--> Soyapango
|
--> Mejicanos
|
--> Apopa
|
--> Santa Tecla
|
--> Delgado
|
--> Sonsonate
|
--> Ahuachapán
"""
    )


# گینه استوایی
def Equatorial_Guinea():
    print(
        """
----Equatorial Guinea
|
--> Malabo
|
--> Bata
|
--> Ebebiyín
|
--> Aconibe
|
--> Añisoc
|
--> Luba
|
--> Evinayong
|
--> Mongomo
|
--> Rebola
|
--> Cogo
"""
    )


# اریتره
def Eritrea():
    print(
        """
----Eritrea
|
--> Asmara
|
--> Keren
|
--> Massawa
|
--> Assab
|
--> Mendefera
|
--> Barentu
|
--> Adi Keyh
|
--> Dekemhare
|
--> Senafe
|
--> Ghinda
"""
    )


# استونی
def Estonia():
    print(
        """
----Estonia
|
--> Tallinn
|
--> Tartu
|
--> Narva
|
--> Pärnu
|
--> Kohtla-Järve
|
--> Viljandi
|
--> Rakvere
|
--> Maardu
|
--> Sillamäe
|
--> Kuressaare
"""
    )


# اسواتینی
def Eswatini():
    print(
        """
----Eswatini
|
--> Mbabane
|
--> Manzini
|
--> Big Bend
|
--> Malkerns
|
--> Nhlangano
|
--> Mhlume
|
--> Simunye
|
--> Siteki
|
--> Piggs Peak
|
--> Lobamba
"""
    )


# اتیوپی
def Ethiopia():
    print(
        """
----Ethiopia
|
--> Addis Ababa
|
--> Mekelle
|
--> Gondar
|
--> Adama
|
--> Hawassa
|
--> Bahir Dar
|
--> Dire Dawa
|
--> Jimma
|
--> Dessie
|
--> Jijiga
"""
    )


# فیجی
def Fiji():
    print(
        """
----Fiji
|
--> Suva
|
--> Lautoka
|
--> Nadi
|
--> Labasa
|
--> Ba
|
--> Nasinu
|
--> Nausori
|
--> Sigatoka
|
--> Lami
|
--> Tavua
"""
    )


# فنلاند
def Finland():
    print(
        """
----Finland
|
--> Helsinki
|
--> Espoo
|
--> Tampere
|
--> Vantaa
|
--> Oulu
|
--> Turku
|
--> Jyväskylä
|
--> Lahti
|
--> Kuopio
|
--> Pori
"""
    )


# فرانسه
def France():
    print(
        """
----France
|
--> Paris
|
--> Marseille
|
--> Lyon
|
--> Toulouse
|
--> Nice
|
--> Nantes
|
--> Strasbourg
|
--> Montpellier
|
--> Bordeaux
|
--> Lille
"""
    )


# گابن
def Gabon():
    print(
        """
----Gabon
|
--> Libreville
|
--> Port-Gentil
|
--> Franceville
|
--> Oyem
|
--> Moanda
|
--> Lambaréné
|
--> Mouila
|
--> Tchibanga
|
--> Makokou
|
--> Bitam
"""
    )


# گامبیا
def Gambia():
    print(
        """
----Gambia
|
--> Banjul
|
--> Serekunda
|
--> Brikama
|
--> Bakau
|
--> Farafenni
|
--> Lamin
|
--> Sukuta
|
--> Basse Santa Su
|
--> Gunjur
|
--> Soma
"""
    )


# گرجستان
def Georgia():
    print(
        """
----Georgia
|
--> Tbilisi
|
--> Batumi
|
--> Kutaisi
|
--> Rustavi
|
--> Zugdidi
|
--> Gori
|
--> Poti
|
--> Telavi
|
--> Akhaltsikhe
|
--> Ozurgeti
"""
    )


# آلمان
def Germany():
    print(
        """
----Germany
|
--> Berlin
|
--> Hamburg
|
--> Munich
|
--> Cologne
|
--> Frankfurt
"""
    )


# گرنادا
def Grenada():
    print(
        """
----Grenada
|
--> St. George's
|
--> Gouyave
|
--> Grenville
|
--> Victoria
|
--> Sauteurs
|
--> Hillsborough
|
--> Grand Roy
|
--> St. David's
|
--> St. Andrew's
|
--> St. Mark's
"""
    )


# گواتمالا
def Guatemala():
    print(
        """
----Guatemala
|
--> Guatemala City
|
--> Mixco
|
--> Villa Nueva
|
--> Quetzaltenango
|
--> Escuintla
|
--> Cobán
|
--> Huehuetenango
|
--> Chiquimula
|
--> Puerto Barrios
|
--> Jalapa
"""
    )


# گینه
def Guinea():
    print(
        """
----Guinea
|
--> Conakry
|
--> Kankan
|
--> Labé
|
--> Kindia
|
--> Mamou
|
--> Boké
|
--> Nzérékoré
|
--> Siguiri
|
--> Faranah
|
--> Télimélé
"""
    )


# گینه بیسائو
def Guinea_Bissau():
    print(
        """
----Guinea-Bissau
|
--> Bissau
|
--> Bafatá
|
--> Gabú
|
--> Cacheu
|
--> Bolama
|
--> Buba
|
--> Quinhamel
|
--> Mansôa
|
--> Catió
|
--> Farim
"""
    )


# گویان
def Guyana():
    print(
        """
----Guyana
|
--> Georgetown
|
--> Linden
|
--> New Amsterdam
|
--> Bartica
|
--> Lethem
|
--> Skeldon
|
--> Anna Regina
|
--> Corriverton
|
--> Rose Hall
|
--> Mahdia
"""
    )


# هائیتی
def Haiti():
    print(
        """
----Haiti
|
--> Port-au-Prince
|
--> Cap-Haïtien
|
--> Gonaïves
|
--> Les Cayes
|
--> Jacmel
|
--> Jérémie
|
--> Hinche
|
--> Saint-Marc
|
--> Croix-des-Bouquets
|
--> Petit-Goâve
"""
    )


# هندوراس
def Honduras():
    print(
        """
----Honduras
|
--> Tegucigalpa
|
--> San Pedro Sula
|
--> La Ceiba
|
--> Choloma
|
--> Comayagua
|
--> El Progreso
|
--> Danlí
|
--> Juticalpa
|
--> Puerto Cortés
|
--> Santa Rosa de Copán
"""
    )


# مجارستان
def Hungary():
    print(
        """
----Hungary
|
--> Budapest
|
--> Debrecen
|
--> Szeged
|
--> Miskolc
|
--> Pécs
|
--> Győr
|
--> Nyíregyháza
|
--> Kecskemét
|
--> Székesfehérvár
|
--> Szombathely
"""
    )


# ایسلند
def Iceland():
    print(
        """
----Iceland
|
--> Reykjavik
|
--> Kópavogur
|
--> Hafnarfjörður
|
--> Akureyri
|
--> Reykjanesbær
|
--> Garðabær
|
--> Mosfellsbær
|
--> Akranes
|
--> Selfoss
|
--> Egilsstaðir
"""
    )


# هند
def India():
    print(
        """
----India
|
--> Delhi
|
--> Mumbai
|
--> Bengaluru
|
--> Chennai
|
--> Hyderabad
|
--> Kolkata
|
--> Ahmedabad
|
--> Pune
|
--> Jaipur
|
--> Lucknow
"""
    )


# اندونزی
def Indonesia():
    print(
        """
----Indonesia
|
--> Jakarta
|
--> Surabaya
|
--> Bandung
|
--> Medan
|
--> Bekasi
|
--> Depok
|
--> Semarang
|
--> Palembang
|
--> Tangerang
|
--> Makassar
"""
    )  # Sources:


# ایران
def Iran():
    print(
        """
----Iran
|
--> Tehran
|
--> Mashhad
|
--> Isfahan
|
--> Karaj
|
--> Shiraz
|
--> Tabriz
|
--> Qom
|
--> Ahvaz
|
--> Kermanshah
|
--> Rasht
"""
    )  # Sources:


# عراق
def Iraq():
    print(
        """
----Iraq
|
--> Baghdad
|
--> Mosul
|
--> Basra
|
--> Erbil
|
--> Kirkuk
|
--> Najaf
|
--> Karbala
|
--> Sulaymaniyah
|
--> Nasiriyah
|
--> Amarah
"""
    )  # Sources:


# ایرلند
def Ireland():
    print(
        """
----Ireland
|
--> Dublin
|
--> Cork
|
--> Limerick
|
--> Galway
|
--> Waterford
|
--> Drogheda
|
--> Dundalk
|
--> Bray
|
--> Swords
|
--> Kilkenny
"""
    )  # Sources:


# ایتالیا
def Italy():
    print(
        """
----Italy
|
--> Rome
|
--> Milan
|
--> Naples
|
--> Turin
|
--> Palermo
|
--> Genoa
|
--> Bologna
|
--> Florence
|
--> Bari
|
--> Catania
"""
    )  # Sources:


# جامائیکا
def Jamaica():
    print(
        """
----Jamaica
|
--> Kingston
|
--> Portmore
|
--> Spanish Town
|
--> Montego Bay
|
--> Mandeville
|
--> May Pen
|
--> Old Harbour
|
--> Linstead
|
--> Savanna-la-Mar
|
--> Port Antonio
"""
    )  # Sources:


# ژاپن
def Japan():
    print(
        """
----Japan
|
--> Tokyo
|
--> Yokohama
|
--> Osaka
|
--> Nagoya
|
--> Sapporo
|
--> Fukuoka
|
--> Kobe
|
--> Kyoto
|
--> Kawasaki
|
--> Hiroshima
"""
    )  # Sources:


# اردن
def Jordan():
    print(
        """
----Jordan
|
--> Amman
|
--> Zarqa
|
--> Irbid
|
--> Russeifa
|
--> Aqaba
|
--> Madaba
|
--> Mafraq
|
--> Salt
|
--> Karak
|
--> Tafilah
"""
    )  # Sources:


# قزاقستان
def Kazakhstan():
    print(
        """
----Kazakhstan
|
--> Almaty
|
--> Astana
|
--> Shymkent
|
--> Karagandy
|
--> Taraz
|
--> Pavlodar
|
--> Aktobe
|
--> Semey
|
--> Kostanay
|
--> Ust-Kamenogorsk
"""
    )  # Sources:


# کنیا
def Kenya():
    print(
        """
----Kenya
|
--> Nairobi
|
--> Mombasa
|
--> Kisumu
|
--> Nakuru
|
--> Eldoret
|
--> Thika
|
--> Ruiru
|
--> Kikuyu
|
--> Machakos
|
--> Garissa
"""
    )  # Sources:


# کیریباتی
def Kiribati():
    print(
        """
----Kiribati
|
--> Tarawa
|
--> Betio
|
--> Bikenibeu
|
--> Teaoraereke
|
--> Bairiki
|
--> Bonriki
|
--> Eita
|
--> Tanaea
|
--> Buariki
|
--> Abatao
"""
    )  # Sources:


# کره شمالی
def North_Korea():
    print(
        """
----North Korea
|
--> Pyongyang
|
--> Hamhung
|
--> Chongjin
|
--> Nampo
|
--> Wonsan
|
--> Sinuiju
|
--> Tanchon
|
--> Kaesong
|
--> Haeju
|
--> Rason
"""
    )


# کره جنوبی
def South_Korea():
    print(
        """
----South Korea
|
--> Seoul
|
--> Busan
|
--> Incheon
|
--> Daegu
|
--> Daejeon
|
--> Gwangju
|
--> Suwon
|
--> Ulsan
|
--> Changwon
|
--> Seongnam
"""
    )


# کویت
def Kuwait():
    print(
        """
----Kuwait
|
--> Kuwait City
|
--> Al Ahmadi
|
--> Hawalli
|
--> Salmiya
|
--> Farwaniya
|
--> Jahra
|
--> Fahaheel
|
--> Mangaf
|
--> Sabah Al Salem
|
--> Mahboula
"""
    )


# قرقیزستان
def Kyrgyzstan():
    print(
        """
----Kyrgyzstan
|
--> Bishkek
|
--> Osh
|
--> Jalal-Abad
|
--> Karakol
|
--> Tokmok
|
--> Naryn
|
--> Talas
|
--> Balykchy
|
--> Kant
|
--> Kara-Balta
"""
    )


# لائوس
def Laos():
    print(
        """
----Laos
|
--> Vientiane
|
--> Pakse
|
--> Savannakhet
|
--> Luang Prabang
|
--> Thakhek
|
--> Muang Xay
|
--> Phonsavan
|
--> Sam Neua
|
--> Paksan
|
--> Attapeu
"""
    )


# لتونی
def Latvia():
    print(
        """
----Latvia
|
--> Riga
|
--> Daugavpils
|
--> Liepāja
|
--> Jelgava
|
--> Jūrmala
|
--> Ventspils
|
--> Rēzekne
|
--> Valmiera
|
--> Ogre
|
--> Jēkabpils
"""
    )


# لبنان
def Lebanon():
    print(
        """
----Lebanon
|
--> Beirut
|
--> Tripoli
|
--> Sidon
|
--> Tyre
|
--> Zahle
|
--> Baalbek
|
--> Jounieh
|
--> Nabatieh
|
--> Aley
|
--> Byblos
"""
    )


# لسوتو
def Lesotho():
    print(
        """
----Lesotho
|
--> Maseru
|
--> Teyateyaneng
|
--> Mafeteng
|
--> Hlotse
|
--> Mohale's Hoek
|
--> Quthing
|
--> Butha-Buthe
|
--> Qacha's Nek
|
--> Mokhotlong
|
--> Thaba-Tseka
"""
    )


# لیبریا
def Liberia():
    print(
        """
----Liberia
|
--> Monrovia
|
--> Gbarnga
|
--> Buchanan
|
--> Kakata
|
--> Zwedru
|
--> Harper
|
--> Voinjama
|
--> Robertsport
|
--> Sanniquellie
|
--> Greenville
"""
    )


# لیبی
def Libya():
    print(
        """
----Libya
|
--> Tripoli
|
--> Benghazi
|
--> Misrata
|
--> Bayda
|
--> Zawiya
|
--> Ajdabiya
|
--> Sabha
|
--> Derna
|
--> Tobruk
|
--> Zliten
"""
    )


# لیختن‌اشتاین
def Liechtenstein():
    print(
        """
----Liechtenstein
|
--> Vaduz
|
--> Schaan
|
--> Balzers
|
--> Triesen
|
--> Eschen
|
--> Mauren
|
--> Triesenberg
|
--> Ruggell
|
--> Gamprin
|
--> Schellenberg
"""
    )


# لیتوانی
def Lithuania():
    print(
        """
----Lithuania
|
--> Vilnius
|
--> Kaunas
|
--> Klaipėda
|
--> Šiauliai
|
--> Panevėžys
|
--> Alytus
|
--> Marijampolė
|
--> Mažeikiai
|
--> Jonava
|
--> Utena
"""
    )


# لوکزامبورگ
def Luxembourg():
    print(
        """
----Luxembourg
|
--> Luxembourg City
|
--> Esch-sur-Alzette
|
--> Differdange
|
--> Dudelange
|
--> Ettelbruck
|
--> Diekirch
|
--> Strassen
|
--> Bertrange
|
--> Bettembourg
|
--> Grevenmacher
"""
    )


# ماداگاسکار
def Madagascar():
    print(
        """
----Madagascar
|
--> Antananarivo
|
--> Toamasina
|
--> Fianarantsoa
|
--> Mahajanga
|
--> Toliara
|
--> Antsiranana
|
--> Ambatondrazaka
|
--> Antsirabe
|
--> Manakara
|
--> Morondava
"""
    )


# مالاوی
def Malawi():
    print(
        """
----Malawi
|
--> Lilongwe
|
--> Blantyre
|
--> Mzuzu
|
--> Zomba
|
--> Kasungu
|
--> Mangochi
|
--> Karonga
|
--> Salima
|
--> Nkhotakota
|
--> Dedza
"""
    )


# مالزی
def Malaysia():
    print(
        """
----Malaysia
|
--> Kuala Lumpur
|
--> George Town
|
--> Johor Bahru
|
--> Ipoh
|
--> Shah Alam
|
--> Kota Kinabalu
|
--> Kuching
|
--> Malacca
|
--> Alor Setar
|
--> Miri
"""
    )


# مالدیو
def Maldives():
    print(
        """
----Maldives
|
--> Malé
|
--> Addu City
|
--> Fuvahmulah
|
--> Kulhudhuffushi
|
--> Thinadhoo
|
--> Naifaru
|
--> Hithadhoo
|
--> Dhidhdhoo
|
--> Eydhafushi
|
--> Villingili
"""
    )


# مالی
def Mali():
    print(
        """
----Mali
|
--> Bamako
|
--> Sikasso
|
--> Mopti
|
--> Koutiala
|
--> Ségou
|
--> Kayes
|
--> Gao
|
--> Tombouctou
|
--> Niono
|
--> Koulikoro
"""
    )


# مالت
def Malta():
    print(
        """
----Malta
|
--> Valletta
|
--> Birkirkara
|
--> Qormi
|
--> Mosta
|
--> Sliema
|
--> Żabbar
|
--> San Ġwann
|
--> Fgura
|
--> Żebbuġ
|
--> Marsaskala
"""
    )


# جزایر مارشال
def Marshall_Islands():
    print(
        """
----Marshall Islands
|
--> Majuro
|
--> Ebeye
|
--> Laura
|
--> Arno
|
--> Delap
|
--> Ajeltake
|
--> Rairok
|
--> Woja
|
--> Uliga
|
--> Jabor
"""
    )


# موریتانی
def Mauritania():
    print(
        """
----Mauritania
|
--> Nouakchott
|
--> Nouadhibou
|
--> Rosso
|
--> Kaédi
|
--> Zouerate
|
--> Kiffa
|
--> Atar
|
--> Akjoujt
|
--> Néma
|
--> Sélibaby
"""
    )


# موریس
def Mauritius():
    print(
        """
----Mauritius
|
--> Port Louis
|
--> Beau Bassin-Rose Hill
|
--> Vacoas-Phoenix
|
--> Curepipe
|
--> Quatre Bornes
|
--> Flic en Flac
|
--> Mahébourg
|
--> Grand Baie
|
--> Goodlands
|
--> Triolet
"""
    )


# مکزیک
def Mexico():
    print(
        """
----Mexico
|
--> Mexico City
|
--> Guadalajara
|
--> Monterrey
|
--> Puebla
|
--> Tijuana
|
--> León
|
--> Ciudad Juárez
|
--> Torreón
|
--> Querétaro
|
--> Mérida
"""
    )


# میکرونزی
def Micronesia():
    print(
        """
----Micronesia
|
--> Palikir
|
--> Kolonia
|
--> Weno
|
--> Tofol
|
--> Tafunsak
|
--> Lelu
|
--> Utwe
|
--> Malem
|
--> Pingelap
|
--> Moen
"""
    )


# مولداوی
def Moldova():
    print(
        """
----Moldova
|
--> Chișinău
|
--> Bălți
|
--> Tiraspol
|
--> Bender
|
--> Cahul
|
--> Ungheni
|
--> Soroca
|
--> Orhei
|
--> Comrat
|
--> Edineț
"""
    )


# موناکو
def Monaco():
    print(
        """
----Monaco
|
--> Monaco-Ville
|
--> Monte Carlo
|
--> La Condamine
|
--> Fontvieille
|
--> Moneghetti
|
--> Les Révoires
|
--> Jardin Exotique
|
--> Larvotto
|
--> Saint Michel
|
--> Saint Roman
"""
    )


# مغولستان
def Mongolia():
    print(
        """
----Mongolia
|
--> Ulaanbaatar
|
--> Erdenet
|
--> Darkhan
|
--> Choibalsan
|
--> Mörön
|
--> Nalaikh
|
--> Baganuur
|
--> Arvaikheer
|
--> Bayankhongor
|
--> Mandalgovi
"""
    )


# مونته‌نگرو
def Montenegro():
    print(
        """
----Montenegro
|
--> Podgorica
|
--> Nikšić
|
--> Herceg Novi
|
--> Pljevlja
|
--> Bijelo Polje
|
--> Cetinje
|
--> Bar
|
--> Berane
|
--> Kotor
|
--> Tivat
"""
    )


# مراکش
def Morocco():
    print(
        """
----Morocco
|
--> Casablanca
|
--> Rabat
|
--> Fes
|
--> Marrakesh
|
--> Tangier
|
--> Agadir
|
--> Meknes
|
--> Oujda
|
--> Kenitra
|
--> Tetouan
"""
    )


# موزامبیک
def Mozambique():
    print(
        """
----Mozambique
|
--> Maputo
|
--> Matola
|
--> Beira
|
--> Nampula
|
--> Quelimane
|
--> Tete
|
--> Chimoio
|
--> Pemba
|
--> Xai-Xai
|
--> Inhambane
"""
    )


# میانمار
def Myanmar():
    print(
        """
----Myanmar
|
--> Yangon
|
--> Mandalay
|
--> Naypyidaw
|
--> Bago
|
--> Mawlamyine
|
--> Taunggyi
|
--> Monywa
|
--> Pathein
|
--> Sittwe
|
--> Meiktila
"""
    )


# نامیبیا
def Namibia():
    print(
        """
----Namibia
|
--> Windhoek
|
--> Walvis Bay
|
--> Swakopmund
|
--> Rundu
|
--> Oshakati
|
--> Katima Mulilo
|
--> Grootfontein
|
--> Otjiwarongo
|
--> Tsumeb
|
--> Rehoboth
"""
    )


# نائورو
def Nauru():
    print(
        """
----Nauru
|
--> Yaren
|
--> Boe
|
--> Aiwo
|
--> Anetan
|
--> Anabar
|
--> Baiti
|
--> Buada
|
--> Denigomodu
|
--> Ewa
|
--> Meneng
"""
    )


# نپال
def Nepal():
    print(
        """
----Nepal
|
--> Kathmandu
|
--> Pokhara
|
--> Lalitpur
|
--> Biratnagar
|
--> Bharatpur
|
--> Birgunj
|
--> Dharan
|
--> Janakpur
|
--> Hetauda
|
--> Bhaktapur
"""
    )


# هلند
def Netherlands():
    print(
        """
----Netherlands
|
--> Amsterdam
|
--> Rotterdam
|
--> The Hague
|
--> Utrecht
|
--> Eindhoven
|
--> Tilburg
|
--> Groningen
|
--> Almere
|
--> Breda
|
--> Nijmegen
"""
    )


# نیوزیلند
def New_Zealand():
    print(
        """
----New Zealand
|
--> Auckland
|
--> Wellington
|
--> Christchurch
|
--> Hamilton
|
--> Tauranga
|
--> Napier-Hastings
|
--> Dunedin
|
--> Palmerston North
|
--> Nelson
|
--> Rotorua
"""
    )


# نیکاراگوئه
def Nicaragua():
    print(
        """
----Nicaragua
|
--> Managua
|
--> León
|
--> Masaya
|
--> Tipitapa
|
--> Chinandega
|
--> Matagalpa
|
--> Estelí
|
--> Granada
|
--> Jinotega
|
--> Bluefields
"""
    )


# نیجر
def Niger():
    print(
        """
----Niger
|
--> Niamey
|
--> Zinder
|
--> Maradi
|
--> Agadez
|
--> Tahoua
|
--> Dosso
|
--> Diffa
|
--> Tillabéri
|
--> Arlit
|
--> Birni-N'Konni
"""
    )


# نیجریه
def Nigeria():
    print(
        """
----Nigeria
|
--> Lagos
|
--> Abuja
|
--> Kano
|
--> Ibadan
|
--> Port Harcourt
|
--> Benin City
|
--> Maiduguri
|
--> Zaria
|
--> Aba
|
--> Jos
"""
    )


# مقدونیه شمالی
def North_Macedonia():
    print(
        """
----North Macedonia
|
--> Skopje
|
--> Bitola
|
--> Kumanovo
|
--> Prilep
|
--> Tetovo
|
--> Veles
|
--> Ohrid
|
--> Gostivar
|
--> Štip
|
--> Strumica
"""
    )


# نروژ
def Norway():
    print(
        """
----Norway
|
--> Oslo
|
--> Bergen
|
--> Trondheim
|
--> Stavanger
|
--> Drammen
|
--> Fredrikstad
|
--> Kristiansand
|
--> Tromsø
|
--> Sandnes
|
--> Skien
"""
    )


# عمان
def Oman():
    print(
        """
----Oman
|
--> Muscat
|
--> Salalah
|
--> Sohar
|
--> Nizwa
|
--> Sur
|
--> Ibri
|
--> Buraimi
|
--> Rustaq
|
--> Bahla
|
--> Khasab
"""
    )


# پاکستان
def Pakistan():
    print(
        """
----Pakistan
|
--> Karachi
|
--> Lahore
|
--> Islamabad
|
--> Rawalpindi
|
--> Faisalabad
|
--> Multan
|
--> Peshawar
|
--> Quetta
|
--> Sialkot
|
--> Gujranwala
"""
    )


# پالائو
def Palau():
    print(
        """
----Palau
|
--> Ngerulmud
|
--> Koror
|
--> Airai
|
--> Melekeok
|
--> Ngaraard
|
--> Ngchesar
|
--> Ngatpang
|
--> Aimeliik
|
--> Ngiwal
|
--> Angaur
"""
    )


# پاناما
def Panama():
    print(
        """
----Panama
|
--> Panama City
|
--> San Miguelito
|
--> Colón
|
--> David
|
--> La Chorrera
|
--> Santiago
|
--> Chitré
|
--> Penonomé
|
--> Arraiján
|
--> Aguadulce
"""
    )


# پاپوآ گینه نو
def Papua_New_Guinea():
    print(
        """
----Papua New Guinea
|
--> Port Moresby
|
--> Lae
|
--> Mount Hagen
|
--> Madang
|
--> Wewak
|
--> Goroka
|
--> Kokopo
|
--> Arawa
|
--> Kimbe
|
--> Alotau
"""
    )


# پاراگوئه
def Paraguay():
    print(
        """
----Paraguay
|
--> Asunción
|
--> Ciudad del Este
|
--> San Lorenzo
|
--> Luque
|
--> Capiatá
|
--> Lambaré
|
--> Fernando de la Mora
|
--> Encarnación
|
--> Ñemby
|
--> Pedro Juan Caballero
"""
    )


# پرو
def Peru():
    print(
        """
----Peru
|
--> Lima
|
--> Arequipa
|
--> Trujillo
|
--> Chiclayo
|
--> Piura
|
--> Cusco
|
--> Iquitos
|
--> Huancayo
|
--> Puno
|
--> Tacna
"""
    )


# فیلیپین
def Philippines():
    print(
        """
----Philippines
|
--> Manila
|
--> Quezon City
|
--> Davao City
|
--> Cebu City
|
--> Zamboanga City
|
--> Antipolo
|
--> Pasig
|
--> Taguig
|
--> Cagayan de Oro
|
--> Bacolod
"""
    )


# لهستان
def Poland():
    print(
        """
----Poland
|
--> Warsaw
|
--> Kraków
|
--> Łódź
|
--> Wrocław
|
--> Poznań
|
--> Gdańsk
|
--> Szczecin
|
--> Bydgoszcz
|
--> Lublin
|
--> Katowice
"""
    )


# پرتغال
def Portugal():
    print(
        """
----Portugal
|
--> Lisbon
|
--> Porto
|
--> Vila Nova de Gaia
|
--> Amadora
|
--> Braga
|
--> Coimbra
|
--> Funchal
|
--> Setúbal
|
--> Almada
|
--> Leiria
"""
    )


# قطر
def Qatar():
    print(
        """
----Qatar
|
--> Doha
|
--> Al Rayyan
|
--> Al Wakrah
|
--> Al Khor
|
--> Umm Salal
|
--> Al Daayen
|
--> Madinat ash Shamal
|
--> Dukhan
|
--> Mesaieed
|
--> Lusail
"""
    )


# رومانی
def Romania():
    print(
        """
----Romania
|
--> Bucharest
|
--> Cluj-Napoca
|
--> Timișoara
|
--> Iași
|
--> Constanța
|
--> Craiova
|
--> Brașov
|
--> Galați
|
--> Ploiești
|
--> Oradea
"""
    )


# روسیه
def Russia():
    print(
        """
----Russia
|
--> Moscow
|
--> Saint Petersburg
|
--> Novosibirsk
|
--> Yekaterinburg
|
--> Nizhny Novgorod
|
--> Kazan
|
--> Chelyabinsk
|
--> Omsk
|
--> Samara
|
--> Rostov-on-Don
"""
    )


# رواندا
def Rwanda():
    print(
        """
----Rwanda
|
--> Kigali
|
--> Butare
|
--> Gitarama
|
--> Ruhengeri
|
--> Gisenyi
|
--> Byumba
|
--> Cyangugu
|
--> Rwamagana
|
--> Nyagatare
|
--> Kibuye
"""
    )


# سنت کیتس و نویس
def Saint_Kitts_and_Nevis():
    print(
        """
----Saint Kitts and Nevis
|
--> Basseterre
|
--> Charlestown
|
--> Sandy Point Town
|
--> Fig Tree
|
--> Monkey Hill
|
--> Cayon
|
--> Dieppe Bay Town
|
--> Newcastle
|
--> Gingerland
|
--> Mansion
"""
    )


# سنت لوسیا
def Saint_Lucia():
    print(
        """
----Saint Lucia
|
--> Castries
|
--> Soufrière
|
--> Vieux Fort
|
--> Gros Islet
|
--> Micoud
|
--> Dennery
|
--> Laborie
|
--> Anse La Raye
|
--> Canaries
|
--> Babonneau
"""
    )


# سنت وینسنت و گرنادین‌ها
def Saint_Vincent_and_the_Grenadines():
    print(
        """
----Saint Vincent and the Grenadines
|
--> Kingstown
|
--> Georgetown
|
--> Barrouallie
|
--> Chateaubelair
|
--> Calliaqua
|
--> Bequia
|
--> Layou
|
--> Port Elizabeth
|
--> Union Island
|
--> Mesopotamia
"""
    )


# ساموآ
def Samoa():
    print(
        """
----Samoa
|
--> Apia
|
--> Vaitele
|
--> Faleasiu
|
--> Siusega
|
--> Malie
|
--> Fasito'o-uta
|
--> Leulumoega
|
--> Safotu
|
--> Saleimoa
|
--> Afega
"""
    )


# سان مارینو
def San_Marino():
    print(
        """
----San Marino
|
--> San Marino
|
--> Serravalle
|
--> Borgo Maggiore
|
--> Domagnano
|
--> Fiorentino
|
--> Acquaviva
|
--> Faetano
|
--> Chiesanuova
"""
    )


# سائوتومه و پرنسیپ
def Sao_Tome_and_Principe():
    print(
        """
----Sao Tome and Principe
|
--> São Tomé
|
--> Santo Amaro
|
--> Neves
|
--> Trindade
|
--> Santana
|
--> São João dos Angolares
|
--> Guadalupe
|
--> Pantufo
|
--> Santa Cruz
|
--> Ribeira Afonso
"""
    )


# عربستان سعودی
def Saudi_Arabia():
    print(
        """
----Saudi Arabia
|
--> Riyadh
|
--> Jeddah
|
--> Mecca
|
--> Medina
|
--> Dammam
|
--> Khobar
|
--> Tabuk
|
--> Abha
|
--> Buraidah
|
--> Najran
"""
    )


# سنگال
def Senegal():
    print(
        """
----Senegal
|
--> Dakar
|
--> Touba
|
--> Thiès
|
--> Rufisque
|
--> Saint-Louis
|
--> Kaolack
|
--> Ziguinchor
|
--> Mbour
|
--> Diourbel
|
--> Louga
"""
    )


# صربستان
def Serbia():
    print(
        """
----Serbia
|
--> Belgrade
|
--> Novi Sad
|
--> Niš
|
--> Kragujevac
|
--> Subotica
|
--> Zrenjanin
|
--> Pančevo
|
--> Čačak
|
--> Smederevo
|
--> Leskovac
"""
    )


# سیشل
def Seychelles():
    print(
        """
----Seychelles
|
--> Victoria
|
--> Anse Boileau
|
--> Beau Vallon
|
--> Bel Ombre
|
--> Cascade
|
--> Glacis
|
--> Grand Anse
|
--> Takamaka
|
--> Baie Lazare
|
--> Mont Fleuri
"""
    )


# سیرالئون
def Sierra_Leone():
    print(
        """
----Sierra Leone
|
--> Freetown
|
--> Bo
|
--> Kenema
|
--> Makeni
|
--> Koidu
|
--> Lunsar
|
--> Port Loko
|
--> Kabala
|
--> Magburaka
|
--> Waterloo
"""
    )


# سنگاپور
def Singapore():
    print(
        """
----Singapore
|
--> Singapore
|
--> Jurong East
|
--> Woodlands
|
--> Tampines
|
--> Yishun
|
--> Bukit Batok
|
--> Hougang
|
--> Sengkang
|
--> Choa Chu Kang
|
--> Pasir Ris
"""
    )


# اسلواکی
def Slovakia():
    print(
        """
----Slovakia
|
--> Bratislava
|
--> Košice
|
--> Prešov
|
--> Žilina
|
--> Nitra
|
--> Banská Bystrica
|
--> Trnava
|
--> Trenčín
|
--> Martin
|
--> Poprad
"""
    )


# اسلوونی
def Slovenia():
    print(
        """
----Slovenia
|
--> Ljubljana
|
--> Maribor
|
--> Celje
|
--> Kranj
|
--> Velenje
|
--> Novo Mesto
|
--> Ptuj
|
--> Trbovlje
|
--> Kamnik
|
--> Jesenice
"""
    )


# جزایر سلیمان
def Solomon_Islands():
    print(
        """
----Solomon Islands
|
--> Honiara
|
--> Gizo
|
--> Auki
|
--> Noro
|
--> Tulagi
|
--> Buala
|
--> Kirakira
|
--> Taro Island
|
--> Lata
|
--> Munda
"""
    )


# سومالی
def Somalia():
    print(
        """
----Somalia
|
--> Mogadishu
|
--> Hargeisa
|
--> Bosaso
|
--> Kismayo
|
--> Baidoa
|
--> Beledweyne
|
--> Galkayo
|
--> Garowe
|
--> Marka
|
--> Jowhar
"""
    )


# آفریقای جنوبی
def South_Africa():
    print(
        """
----South Africa
|
--> Johannesburg
|
--> Cape Town
|
--> Durban
|
--> Pretoria
|
--> Port Elizabeth
|
--> Bloemfontein
|
--> East London
|
--> Polokwane
|
--> Kimberley
|
--> Nelspruit
"""
    )


# سودان جنوبی
def South_Sudan():
    print(
        """
----South Sudan
|
--> Juba
|
--> Wau
|
--> Malakal
|
--> Bor
|
--> Yambio
|
--> Rumbek
|
--> Aweil
|
--> Torit
|
--> Bentiu
|
--> Kuajok
"""
    )


# اسپانیا
def Spain():
    print(
        """
----Spain
|
--> Madrid
|
--> Barcelona
|
--> Valencia
|
--> Seville
|
--> Zaragoza
|
--> Málaga
|
--> Murcia
|
--> Palma
|
--> Bilbao
|
--> Alicante
"""
    )


# سری‌لانکا
def Sri_Lanka():
    print(
        """
----Sri Lanka
|
--> Colombo
|
--> Kandy
|
--> Galle
|
--> Jaffna
|
--> Negombo
|
--> Trincomalee
|
--> Batticaloa
|
--> Anuradhapura
|
--> Ratnapura
|
--> Matara
"""
    )


# سودان
def Sudan():
    print(
        """
----Sudan
|
--> Khartoum
|
--> Omdurman
|
--> Port Sudan
|
--> Kassala
|
--> El Obeid
|
--> Nyala
|
--> Wad Madani
|
--> Atbara
|
--> El Fasher
|
--> Kosti
"""
    )


# سورینام
def Suriname():
    print(
        """
----Suriname
|
--> Paramaribo
|
--> Lelydorp
|
--> Nieuw Nickerie
|
--> Moengo
|
--> Albina
|
--> Totness
|
--> Wageningen
|
--> Brokopondo
|
--> Groningen
|
--> Brownsweg
"""
    )


# سوئد
def Sweden():
    print(
        """
----Sweden
|
--> Stockholm
|
--> Gothenburg
|
--> Malmö
|
--> Uppsala
|
--> Västerås
|
--> Örebro
|
--> Linköping
|
--> Helsingborg
|
--> Jönköping
|
--> Norrköping
"""
    )


# سوئیس
def Switzerland():
    print(
        """
----Switzerland
|
--> Zurich
|
--> Geneva
|
--> Basel
|
--> Bern
|
--> Lausanne
|
--> Lucerne
|
--> St. Gallen
|
--> Lugano
|
--> Biel/Bienne
|
--> Thun
"""
    )


# سوریه
def Syria():
    print(
        """
----Syria
|
--> Damascus
|
--> Aleppo
|
--> Homs
|
--> Latakia
|
--> Hama
|
--> Deir ez-Zor
|
--> Raqqa
|
--> Daraa
|
--> Tartus
|
--> Al-Hasakah
"""
    )


# تایوان
def Taiwan():
    print(
        """
----Taiwan
|
--> Taipei
|
--> Kaohsiung
|
--> Taichung
|
--> Tainan
|
--> Hsinchu
|
--> Keelung
|
--> Chiayi
|
--> Pingtung
|
--> Miaoli
|
--> Yilan
"""
    )


# تاجیکستان
def Tajikistan():
    print(
        """
----Tajikistan
|
--> Dushanbe
|
--> Khujand
|
--> Kulob
|
--> Qurghonteppa
|
--> Istaravshan
|
--> Panjakent
|
--> Tursunzoda
|
--> Khorugh
|
--> Vahdat
|
--> Isfara
"""
    )


# تانزانیا
def Tanzania():
    print(
        """
----Tanzania
|
--> Dar es Salaam
|
--> Dodoma
|
--> Mwanza
|
--> Arusha
|
--> Mbeya
|
--> Morogoro
|
--> Tanga
|
--> Zanzibar City
|
--> Kigoma
|
--> Tabora
"""
    )


# تایلند
def Thailand():
    print(
        """
----Thailand
|
--> Bangkok
|
--> Chiang Mai
|
--> Nakhon Ratchasima
|
--> Udon Thani
|
--> Pattaya
|
--> Khon Kaen
|
--> Hat Yai
|
--> Surat Thani
|
--> Nakhon Si Thammarat
|
--> Phuket
"""
    )


# تیمور شرقی
def Timor_Leste():
    print(
        """
----Timor-Leste
|
--> Dili
|
--> Baucau
|
--> Maliana
|
--> Suai
|
--> Lospalos
|
--> Aileu
|
--> Ainaro
|
--> Ermera
|
--> Manatuto
|
--> Viqueque
"""
    )


# توگو
def Togo():
    print(
        """
----Togo
|
--> Lomé
|
--> Sokodé
|
--> Kara
|
--> Kpalimé
|
--> Atakpamé
|
--> Tsévié
|
--> Aného
|
--> Dapaong
|
--> Mango
|
--> Notsé
"""
    )


# تونگا
def Tonga():
    print(
        """
----Tonga
|
--> Nukuʻalofa
|
--> Neiafu
|
--> Pangai
|
--> ʻOhonua
|
--> Haveluloto
|
--> Vaini
|
--> Hihifo
|
--> Lapaha
|
--> Kolonga
|
--> Fuaʻamotu
"""
    )


# ترینیداد
def Trinidad():
    print(
        """
----Trinidad
|
--> Port of Spain
|
--> San Fernando
|
--> Chaguanas
|
--> Arima
|
--> Point Fortin
|
--> Couva
|
--> Princes Town
|
--> Diego Martin
|
--> Siparia
|
--> Sangre Grande
"""
    )


# توباگو
def Tobago():
    print(
        """
----Tobago
|
--> Scarborough
|
--> Roxborough
|
--> Charlotteville
|
--> Plymouth
|
--> Speyside
|
--> Goodwood
|
--> Mason Hall
|
--> Bethel
|
--> Lambeau
|
--> Lowlands
"""
    )


# تونس
def Tunisia():
    print(
        """
----Tunisia
|
--> Tunis
|
--> Sfax
|
--> Sousse
|
--> Kairouan
|
--> Bizerte
|
--> Gabès
|
--> Ariana
|
--> Gafsa
|
--> Monastir
|
--> Nabeul
"""
    )


# ترکیه
def Turkey():
    print(
        """
----Turkey
|
--> Istanbul
|
--> Ankara
|
--> Izmir
|
--> Bursa
|
--> Adana
|
--> Gaziantep
|
--> Konya
|
--> Antalya
|
--> Kayseri
|
--> Mersin
"""
    )


# ترکمنستان
def Turkmenistan():
    print(
        """
----Turkmenistan
|
--> Ashgabat
|
--> Türkmenabat
|
--> Dashoguz
|
--> Mary
|
--> Balkanabat
|
--> Tejen
|
--> Bayramaly
|
--> Abadan
|
--> Serdar
|
--> Gazanjyk
"""
    )


def all():
    print(
        """

🌍 All countries :

Afghanistan
Albania
Algeria
Andorra
Angola
Antigua
Barbuda
Argentina
Armenia
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina Faso
Burundi
Cabo Verde
Cambodia
Cameroon
Canada
Central African Republic
Chad
Chile
China
Colombia
Comoros
Congo (Brazzaville)
Congo (Kinshasa)
Costa Rica
Croatia
Cuba
Cyprus
Czech Republic
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Eswatini
Ethiopia
Fiji
Finland
France
Gabon
Gambia
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea-Bissau
Guyana
Haiti
Honduras
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Korea, North
Korea, South
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
North Macedonia
Norway
Oman
Pakistan
Palau
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Qatar
Romania
Russia
Rwanda
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tonga
Trinidad
Tobago
Tunisia
Turkey
Turkmenistan
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
Uruguay
Uzbekistan
Vanuatu
Vatican City
Venezuela
Vietnam
Yemen
Zambia
Zimbabwe
 """
    )


def city():
    print(
        """

----Afghanistan
|
--> Kabul
|
--> Herat
|
--> Kandahar
|
--> Mazar-i-Sharif
|
--> Jalalabad
|
--> Kunduz
|
--> Ghazni
|
--> Bamyan
|
--> Khost
|
--> Farah
|
--> Baghlan
|
--> Pul-e Khumri
|
--> Lashkar Gah
|
--> Taloqan
|
--> Sheberghan
|
--> Zaranj
|
--> Fayzabad
|
--> Gardez
|
--> Charikar

----Albania
|
--> Tirana
|
--> Durrës
|
--> Vlorë
|
--> Shkodër
|
--> Elbasan
|
--> Fier
|
--> Berat
|
--> Korçë
|
--> Gjirokastër
|
--> Kukës

----Algeria
|
--> Algiers
|
--> Oran
|
--> Constantine
|
--> Annaba
|
--> Blida
|
--> Batna
|
--> Sétif
|
--> Djelfa
|
--> Tébessa
|
--> Skikda

----Andorra
|
--> Andorra la Vella
|
--> Escaldes-Engordany
|
--> Encamp
|
--> La Massana
|
--> Ordino
|
--> Canillo
|
--> Sant Julià de Lòria

----Angola
|
--> Luanda
|
--> Huambo
|
--> Lobito
|
--> Benguela
|
--> Kuito
|
--> Lubango
|
--> Malanje
|
--> Namibe
|
--> Saurimo
|
--> Uíge

----Antigua and Barbuda
|
--> St. John's
|
--> All Saints
|
--> Liberta
|
--> Potter's Village
|
--> Bolans
|
--> Swetes
|
--> Seaview Farm
|
--> Pigotts
|
--> Parham
|
--> Clare Hall

----Argentina
|
--> Buenos Aires
|
--> Córdoba
|
--> Rosario
|
--> Mendoza
|
--> La Plata
|
--> San Miguel de Tucumán
|
--> Mar del Plata
|
--> Salta
|
--> Santa Fe
|
--> San Juan

----Armenia
|
--> Yerevan
|
--> Gyumri
|
--> Vanadzor
|
--> Vagharshapat
|
--> Hrazdan
|
--> Abovyan
|
--> Kapan
|
--> Ararat
|
--> Armavir
|
--> Gavar

----Australia
|
--> Sydney
|
--> Melbourne
|
--> Brisbane
|
--> Perth
|
--> Adelaide
|
--> Canberra
|
--> Hobart
|
--> Darwin
|
--> Gold Coast
|
--> Newcastle

----Austria
|
--> Vienna
|
--> Graz
|
--> Linz
|
--> Salzburg
|
--> Innsbruck
|
--> Klagenfurt
|
--> Villach
|
--> Wels
|
--> Sankt Pölten
|
--> Dornbirn

----Azerbaijan
|
--> Baku
|
--> Ganja
|
--> Sumqayit
|
--> Mingachevir
|
--> Lankaran
|
--> Nakhchivan
|
--> Sheki
|
--> Shirvan
|
--> Khirdalan
|
--> Shamakhi

----Bahamas
|
--> Nassau
|
--> Freeport
|
--> Marsh Harbour
|
--> Coopers Town
|
--> West End
|
--> Lucaya
|
--> Alice Town
|
--> Andros Town
|
--> Clarence Town
|
--> Dunmore Town

----Bahrain
|
--> Manama
|
--> Riffa
|
--> Muharraq
|
--> Hamad Town
|
--> A'ali
|
--> Sitra
|
--> Isa Town
|
--> Budaiya
|
--> Jidhafs
|
--> Diraz

----Bangladesh
|
--> Dhaka
|
--> Chittagong
|
--> Khulna
|
--> Rajshahi
|
--> Sylhet
|
--> Barisal
|
--> Mymensingh
|
--> Comilla
|
--> Rangpur
|
--> Bogra

----Barbados
|
--> Bridgetown
|
--> Speightstown
|
--> Oistins
|
--> Holetown
|
--> Bathsheba
|
--> Saint James
|
--> Saint Michael
|
--> Saint George
|
--> Saint Philip
|
--> Saint Thomas

----Belarus
|
--> Minsk
|
--> Gomel
|
--> Vitebsk
|
--> Brest
|
--> Mogilev
|
--> Grodno
|
--> Babruysk
|
--> Baranovichi
|
--> Barysaw
|
--> Pinsk

----Belgium
|
--> Brussels
|
--> Antwerp
|
--> Ghent
|
--> Charleroi
|
--> Liège
|
--> Bruges
|
--> Namur
|
--> Leuven
|
--> Mons
|
--> Mechelen

----Belize
|
--> Belize City
|
--> Belmopan
|
--> San Ignacio
|
--> Orange Walk Town
|
--> Dangriga
|
--> Corozal Town
|
--> Punta Gorda
|
--> San Pedro
|
--> Benque Viejo del Carmen
|
--> Ladyville

----Benin
|
--> Cotonou
|
--> Porto-Novo
|
--> Parakou
|
--> Djougou
|
--> Abomey
|
--> Bohicon
|
--> Kandi
|
--> Natitingou
|
--> Ouidah
|
--> Lokossa

----Bhutan
|
--> Thimphu
|
--> Phuntsholing
|
--> Paro
|
--> Gelephu
|
--> Samdrup Jongkhar
|
--> Wangdue Phodrang
|
--> Punakha
|
--> Jakar
|
--> Nganglam
|
--> Samtse

----Bolivia
|
--> Santa Cruz de la Sierra
|
--> El Alto
|
--> La Paz
|
--> Cochabamba
|
--> Oruro
|
--> Sucre
|
--> Tarija
|
--> Potosí
|
--> Sacaba
|
--> Quillacollo

----Bosnia and Herzegovina
|
--> Sarajevo
|
--> Banja Luka
|
--> Tuzla
|
--> Zenica
|
--> Mostar
|
--> Bijeljina
|
--> Prijedor
|
--> Doboj
|
--> Cazin
|
--> Trebinje

----Botswana
|
--> Gaborone
|
--> Francistown
|
--> Molepolole
|
--> Selebi-Phikwe
|
--> Maun
|
--> Serowe
|
--> Kanye
|
--> Mahalapye
|
--> Mochudi
|
--> Lobatse

----Brazil
|
--> São Paulo
|
--> Rio de Janeiro
|
--> Brasília
|
--> Salvador
|
--> Fortaleza
|
--> Belo Horizonte
|
--> Manaus
|
--> Curitiba
|
--> Recife
|
--> Porto Alegre

----Brunei
|
--> Bandar Seri Begawan
|
--> Kuala Belait
|
--> Seria
|
--> Tutong

----Bulgaria
|
--> Sofia
|
--> Plovdiv
|
--> Varna
|
--> Burgas
|
--> Ruse
|
--> Stara Zagora
|
--> Pleven
|
--> Sliven
|
--> Dobrich
|
--> Shumen

----Burkina Faso
|
--> Ouagadougou
|
--> Bobo-Dioulasso
|
--> Koudougou
|
--> Ouahigouya
|
--> Banfora
|
--> Dédougou
|
--> Kaya
|
--> Dori
|
--> Tenkodogo
|
--> Fada N'gourma

----Burundi
|
--> Bujumbura
|
--> Gitega
|
--> Muyinga
|
--> Ngozi
|
--> Ruyigi
|
--> Kayanza
|
--> Bururi
|
--> Muramvya
|
--> Makamba
|
--> Rumonge

----Cabo Verde
|
--> Praia
|
--> Mindelo
|
--> Santa Maria
|
--> Espargos
|
--> Assomada
|
--> São Filipe
|
--> Tarrafal
|
--> Pedra Badejo
|
--> Porto Novo
|
--> Sal Rei

----Cambodia
|
--> Phnom Penh
|
--> Siem Reap
|
--> Battambang
|
--> Sihanoukville
|
--> Kampong Cham
|
--> Kampot
|
--> Takeo
|
--> Pursat
|
--> Kampong Thom
|
--> Svay Rieng

----Cameroon
|
--> Yaoundé
|
--> Douala
|
--> Bamenda
|
--> Bafoussam
|
--> Garoua
|
--> Maroua
|
--> Ngaoundéré
|
--> Bertoua
|
--> Kumba
|
--> Limbe

----Canada
|
--> Toronto
|
--> Montreal
|
--> Vancouver
|
--> Calgary
|
--> Edmonton
|
--> Ottawa
|
--> Winnipeg
|
--> Quebec City
|
--> Hamilton
|
--> Halifax

----Central African Republic
|
--> Bangui
|
--> Bimbo
|
--> Berbérati
|
--> Carnot
|
--> Bambari
|
--> Bouar
|
--> Bossangoa
|
--> Bria
|
--> Bangassou
|
--> Mbaïki

----Chad
|
--> N'Djamena
|
--> Moundou
|
--> Sarh
|
--> Abéché
|
--> Kélo
|
--> Koumra
|
--> Pala
|
--> Bongor
|
--> Mongo
|
--> Doba

----Chile
|
--> Santiago
|
--> Puente Alto
|
--> Antofagasta
|
--> Viña del Mar
|
--> Valparaíso
|
--> Talcahuano
|
--> Temuco
|
--> Iquique
|
--> Concepción
|
--> Rancagua

----China
|
--> Beijing
|
--> Shanghai
|
--> Guangzhou
|
--> Shenzhen
|
--> Chengdu
|
--> Chongqing
|
--> Tianjin
|
--> Wuhan
|
--> Hangzhou
|
--> Xi'an

----Colombia
|
--> Bogotá
|
--> Medellín
|
--> Cali
|
--> Barranquilla
|
--> Cartagena
|
--> Cúcuta
|
--> Bucaramanga
|
--> Pereira
|
--> Santa Marta
|
--> Ibagué

----Comoros
|
--> Moroni
|
--> Mutsamudu
|
--> Fomboni
|
--> Domoni
|
--> Ouani
|
--> Mitsamiouli
|
--> Tsimbeo
|
--> Sima
|
--> Moya
|
--> Bandrele

----Congo (Brazzaville)
|
--> Brazzaville
|
--> Pointe-Noire
|
--> Dolisie
|
--> Nkayi
|
--> Owando
|
--> Ouesso
|
--> Madingou
|
--> Gamboma
|
--> Sibiti
|
--> Kinkala

----Congo (Kinshasa)
|
--> Kinshasa
|
--> Lubumbashi
|
--> Mbuji-Mayi
|
--> Kisangani
|
--> Kananga
|
--> Bukavu
|
--> Goma
|
--> Kolwezi
|
--> Matadi
|
--> Beni

----Costa Rica
|
--> San José
|
--> Alajuela
|
--> Cartago
|
--> Heredia
|
--> Puntarenas
|
--> Limón
|
--> Liberia
|
--> San Isidro
|
--> Curridabat
|
--> Nicoya

----Croatia
|
--> Zagreb
|
--> Split
|
--> Rijeka
|
--> Osijek
|
--> Zadar
|
--> Pula
|
--> Slavonski Brod
|
--> Karlovac
|
--> Varaždin
|
--> Šibenik

----Cuba
|
--> Havana
|
--> Santiago de Cuba
|
--> Camagüey
|
--> Holguín
|
--> Santa Clara
|
--> Guantánamo
|
--> Bayamo
|
--> Cienfuegos
|
--> Matanzas
|
--> Pinar del Río

----Cyprus
|
--> Nicosia
|
--> Limassol
|
--> Larnaca
|
--> Famagusta
|
--> Paphos
|
--> Kyrenia
|
--> Strovolos
|
--> Ayia Napa
|
--> Aradippou
|
--> Paralimni

----Czech Republic
|
--> Prague
|
--> Brno
|
--> Ostrava
|
--> Plzeň
|
--> Liberec
|
--> Olomouc
|
--> České Budějovice
|
--> Hradec Králové
|
--> Pardubice
|
--> Zlín

----Denmark
|
--> Copenhagen
|
--> Aarhus
|
--> Odense
|
--> Aalborg
|
--> Esbjerg
|
--> Randers
|
--> Kolding
|
--> Horsens
|
--> Vejle
|
--> Roskilde

----Djibouti
|
--> Djibouti
|
--> Ali Sabieh
|
--> Tadjourah
|
--> Dikhil
|
--> Obock
|
--> Arta
|
--> Holhol
|
--> Balho
|
--> Yoboki
|
--> Dorra

----Dominica
|
--> Roseau
|
--> Portsmouth
|
--> Marigot
|
--> Canefield
|
--> Mahaut
|
--> Grand Bay
|
--> Castle Bruce
|
--> Wesley
|
--> La Plaine
|
--> Saint Joseph

----Dominican Republic
|
--> Santo Domingo
|
--> Santiago
|
--> La Romana
|
--> San Pedro de Macorís
|
--> San Cristóbal
|
--> Higüey
|
--> Puerto Plata
|
--> Moca
|
--> La Vega
|
--> San Francisco de Macorís

----Ecuador
|
--> Quito
|
--> Guayaquil
|
--> Cuenca
|
--> Santo Domingo
|
--> Machala
|
--> Manta
|
--> Portoviejo
|
--> Ambato
|
--> Loja
|
--> Esmeraldas

----Egypt
|
--> Cairo
|
--> Alexandria
|
--> Giza
|
--> Shubra El Kheima
|
--> Port Said
|
--> Suez
|
--> Mansoura
|
--> Tanta
|
--> Asyut
|
--> Ismailia

----El Salvador
|
--> San Salvador
|
--> Santa Ana
|
--> San Miguel
|
--> Soyapango
|
--> Mejicanos
|
--> Apopa
|
--> Santa Tecla
|
--> Delgado
|
--> Sonsonate
|
--> Ahuachapán

----Equatorial Guinea
|
--> Malabo
|
--> Bata
|
--> Ebebiyín
|
--> Aconibe
|
--> Añisoc
|
--> Luba
|
--> Evinayong
|
--> Mongomo
|
--> Rebola
|
--> Cogo

----Eritrea
|
--> Asmara
|
--> Keren
|
--> Massawa
|
--> Assab
|
--> Mendefera
|
--> Barentu
|
--> Adi Keyh
|
--> Dekemhare
|
--> Senafe
|
--> Ghinda

----Estonia
|
--> Tallinn
|
--> Tartu
|
--> Narva
|
--> Pärnu
|
--> Kohtla-Järve
|
--> Viljandi
|
--> Rakvere
|
--> Maardu
|
--> Sillamäe
|
--> Kuressaare

----Eswatini
|
--> Mbabane
|
--> Manzini
|
--> Big Bend
|
--> Malkerns
|
--> Nhlangano
|
--> Mhlume
|
--> Simunye
|
--> Siteki
|
--> Piggs Peak
|
--> Lobamba

----Ethiopia
|
--> Addis Ababa
|
--> Mekelle
|
--> Gondar
|
--> Adama
|
--> Hawassa
|
--> Bahir Dar
|
--> Dire Dawa
|
--> Jimma
|
--> Dessie
|
--> Jijiga

----Fiji
|
--> Suva
|
--> Lautoka
|
--> Nadi
|
--> Labasa
|
--> Ba
|
--> Nasinu
|
--> Nausori
|
--> Sigatoka
|
--> Lami
|
--> Tavua

----Finland
|
--> Helsinki
|
--> Espoo
|
--> Tampere
|
--> Vantaa
|
--> Oulu
|
--> Turku
|
--> Jyväskylä
|
--> Lahti
|
--> Kuopio
|
--> Pori

----France
|
--> Paris
|
--> Marseille
|
--> Lyon
|
--> Toulouse
|
--> Nice
|
--> Nantes
|
--> Strasbourg
|
--> Montpellier
|
--> Bordeaux
|
--> Lille

----Gabon
|
--> Libreville
|
--> Port-Gentil
|
--> Franceville
|
--> Oyem
|
--> Moanda
|
--> Lambaréné
|
--> Mouila
|
--> Tchibanga
|
--> Makokou
|
--> Bitam

----Gambia
|
--> Banjul
|
--> Serekunda
|
--> Brikama
|
--> Bakau
|
--> Farafenni
|
--> Lamin
|
--> Sukuta
|
--> Basse Santa Su
|
--> Gunjur
|
--> Soma

----Georgia
|
--> Tbilisi
|
--> Batumi
|
--> Kutaisi
|
--> Rustavi
|
--> Zugdidi
|
--> Gori
|
--> Poti
|
--> Telavi
|
--> Akhaltsikhe
|
--> Ozurgeti

----Germany
|
--> Berlin
|
--> Hamburg
|
--> Munich
|
--> Cologne
|
--> Frankfurt

----Grenada
|
--> St. George's
|
--> Gouyave
|
--> Grenville
|
--> Victoria
|
--> Sauteurs
|
--> Hillsborough
|
--> Grand Roy
|
--> St. David's
|
--> St. Andrew's
|
--> St. Mark's

----Guatemala
|
--> Guatemala City
|
--> Mixco
|
--> Villa Nueva
|
--> Quetzaltenango
|
--> Escuintla
|
--> Cobán
|
--> Huehuetenango
|
--> Chiquimula
|
--> Puerto Barrios
|
--> Jalapa

----Guinea
|
--> Conakry
|
--> Kankan
|
--> Labé
|
--> Kindia
|
--> Mamou
|
--> Boké
|
--> Nzérékoré
|
--> Siguiri
|
--> Faranah
|
--> Télimélé

----Guinea-Bissau
|
--> Bissau
|
--> Bafatá
|
--> Gabú
|
--> Cacheu
|
--> Bolama
|
--> Buba
|
--> Quinhamel
|
--> Mansôa
|
--> Catió
|
--> Farim

----Guyana
|
--> Georgetown
|
--> Linden
|
--> New Amsterdam
|
--> Bartica
|
--> Lethem
|
--> Skeldon
|
--> Anna Regina
|
--> Corriverton
|
--> Rose Hall
|
--> Mahdia

----Haiti
|
--> Port-au-Prince
|
--> Cap-Haïtien
|
--> Gonaïves
|
--> Les Cayes
|
--> Jacmel
|
--> Jérémie
|
--> Hinche
|
--> Saint-Marc
|
--> Croix-des-Bouquets
|
--> Petit-Goâve

----Honduras
|
--> Tegucigalpa
|
--> San Pedro Sula
|
--> La Ceiba
|
--> Choloma
|
--> Comayagua
|
--> El Progreso
|
--> Danlí
|
--> Juticalpa
|
--> Puerto Cortés
|
--> Santa Rosa de Copán

----Hungary
|
--> Budapest
|
--> Debrecen
|
--> Szeged
|
--> Miskolc
|
--> Pécs
|
--> Győr
|
--> Nyíregyháza
|
--> Kecskemét
|
--> Székesfehérvár
|
--> Szombathely

----Iceland
|
--> Reykjavik
|
--> Kópavogur
|
--> Hafnarfjörður
|
--> Akureyri
|
--> Reykjanesbær
|
--> Garðabær
|
--> Mosfellsbær
|
--> Akranes
|
--> Selfoss
|
--> Egilsstaðir

----India
|
--> Delhi
|
--> Mumbai
|
--> Bengaluru
|
--> Chennai
|
--> Hyderabad
|
--> Kolkata
|
--> Ahmedabad
|
--> Pune
|
--> Jaipur
|
--> Lucknow

----Indonesia
|
--> Jakarta
|
--> Surabaya
|
--> Bandung
|
--> Medan
|
--> Bekasi
|
--> Depok
|
--> Semarang
|
--> Palembang
|
--> Tangerang
|
--> Makassar

----Iran
|
--> Tehran
|
--> Mashhad
|
--> Isfahan
|
--> Karaj
|
--> Shiraz
|
--> Tabriz
|
--> Qom
|
--> Ahvaz
|
--> Kermanshah
|
--> Rasht

----Iraq
|
--> Baghdad
|
--> Mosul
|
--> Basra
|
--> Erbil
|
--> Kirkuk
|
--> Najaf
|
--> Karbala
|
--> Sulaymaniyah
|
--> Nasiriyah
|
--> Amarah

----Ireland
|
--> Dublin
|
--> Cork
|
--> Limerick
|
--> Galway
|
--> Waterford
|
--> Drogheda
|
--> Dundalk
|
--> Bray
|
--> Swords
|
--> Kilkenny

----Italy
|
--> Rome
|
--> Milan
|
--> Naples
|
--> Turin
|
--> Palermo
|
--> Genoa
|
--> Bologna
|
--> Florence
|
--> Bari
|
--> Catania

----Jamaica
|
--> Kingston
|
--> Portmore
|
--> Spanish Town
|
--> Montego Bay
|
--> Mandeville
|
--> May Pen
|
--> Old Harbour
|
--> Linstead
|
--> Savanna-la-Mar
|
--> Port Antonio

----Japan
|
--> Tokyo
|
--> Yokohama
|
--> Osaka
|
--> Nagoya
|
--> Sapporo
|
--> Fukuoka
|
--> Kobe
|
--> Kyoto
|
--> Kawasaki
|
--> Hiroshima

----Jordan
|
--> Amman
|
--> Zarqa
|
--> Irbid
|
--> Russeifa
|
--> Aqaba
|
--> Madaba
|
--> Mafraq
|
--> Salt
|
--> Karak
|
--> Tafilah

----Kazakhstan
|
--> Almaty
|
--> Astana
|
--> Shymkent
|
--> Karagandy
|
--> Taraz
|
--> Pavlodar
|
--> Aktobe
|
--> Semey
|
--> Kostanay
|
--> Ust-Kamenogorsk

----Kenya
|
--> Nairobi
|
--> Mombasa
|
--> Kisumu
|
--> Nakuru
|
--> Eldoret
|
--> Thika
|
--> Ruiru
|
--> Kikuyu
|
--> Machakos
|
--> Garissa

----Kiribati
|
--> Tarawa
|
--> Betio
|
--> Bikenibeu
|
--> Teaoraereke
|
--> Bairiki
|
--> Bonriki
|
--> Eita
|
--> Tanaea
|
--> Buariki
|
--> Abatao

----North Korea
|
--> Pyongyang
|
--> Hamhung
|
--> Chongjin
|
--> Nampo
|
--> Wonsan
|
--> Sinuiju
|
--> Tanchon
|
--> Kaesong
|
--> Haeju
|
--> Rason

----South Korea
|
--> Seoul
|
--> Busan
|
--> Incheon
|
--> Daegu
|
--> Daejeon
|
--> Gwangju
|
--> Suwon
|
--> Ulsan
|
--> Changwon
|
--> Seongnam

----Kuwait
|
--> Kuwait City
|
--> Al Ahmadi
|
--> Hawalli
|
--> Salmiya
|
--> Farwaniya
|
--> Jahra
|
--> Fahaheel
|
--> Mangaf
|
--> Sabah Al Salem
|
--> Mahboula

----Kyrgyzstan
|
--> Bishkek
|
--> Osh
|
--> Jalal-Abad
|
--> Karakol
|
--> Tokmok
|
--> Naryn
|
--> Talas
|
--> Balykchy
|
--> Kant
|
--> Kara-Balta

----Laos
|
--> Vientiane
|
--> Pakse
|
--> Savannakhet
|
--> Luang Prabang
|
--> Thakhek
|
--> Muang Xay
|
--> Phonsavan
|
--> Sam Neua
|
--> Paksan
|
--> Attapeu

----Latvia
|
--> Riga
|
--> Daugavpils
|
--> Liepāja
|
--> Jelgava
|
--> Jūrmala
|
--> Ventspils
|
--> Rēzekne
|
--> Valmiera
|
--> Ogre
|
--> Jēkabpils

----Lebanon
|
--> Beirut
|
--> Tripoli
|
--> Sidon
|
--> Tyre
|
--> Zahle
|
--> Baalbek
|
--> Jounieh
|
--> Nabatieh
|
--> Aley
|
--> Byblos

----Lesotho
|
--> Maseru
|
--> Teyateyaneng
|
--> Mafeteng
|
--> Hlotse
|
--> Mohale's Hoek
|
--> Quthing
|
--> Butha-Buthe
|
--> Qacha's Nek
|
--> Mokhotlong
|
--> Thaba-Tseka

----Liberia
|
--> Monrovia
|
--> Gbarnga
|
--> Buchanan
|
--> Kakata
|
--> Zwedru
|
--> Harper
|
--> Voinjama
|
--> Robertsport
|
--> Sanniquellie
|
--> Greenville

----Libya
|
--> Tripoli
|
--> Benghazi
|
--> Misrata
|
--> Bayda
|
--> Zawiya
|
--> Ajdabiya
|
--> Sabha
|
--> Derna
|
--> Tobruk
|
--> Zliten

----Liechtenstein
|
--> Vaduz
|
--> Schaan
|
--> Balzers
|
--> Triesen
|
--> Eschen
|
--> Mauren
|
--> Triesenberg
|
--> Ruggell
|
--> Gamprin
|
--> Schellenberg

----Lithuania
|
--> Vilnius
|
--> Kaunas
|
--> Klaipėda
|
--> Šiauliai
|
--> Panevėžys
|
--> Alytus
|
--> Marijampolė
|
--> Mažeikiai
|
--> Jonava
|
--> Utena

----Luxembourg
|
--> Luxembourg City
|
--> Esch-sur-Alzette
|
--> Differdange
|
--> Dudelange
|
--> Ettelbruck
|
--> Diekirch
|
--> Strassen
|
--> Bertrange
|
--> Bettembourg
|
--> Grevenmacher

----Madagascar
|
--> Antananarivo
|
--> Toamasina
|
--> Fianarantsoa
|
--> Mahajanga
|
--> Toliara
|
--> Antsiranana
|
--> Ambatondrazaka
|
--> Antsirabe
|
--> Manakara
|
--> Morondava

----Malawi
|
--> Lilongwe
|
--> Blantyre
|
--> Mzuzu
|
--> Zomba
|
--> Kasungu
|
--> Mangochi
|
--> Karonga
|
--> Salima
|
--> Nkhotakota
|
--> Dedza

----Malaysia
|
--> Kuala Lumpur
|
--> George Town
|
--> Johor Bahru
|
--> Ipoh
|
--> Shah Alam
|
--> Kota Kinabalu
|
--> Kuching
|
--> Malacca
|
--> Alor Setar
|
--> Miri

----Maldives
|
--> Malé
|
--> Addu City
|
--> Fuvahmulah
|
--> Kulhudhuffushi
|
--> Thinadhoo
|
--> Naifaru
|
--> Hithadhoo
|
--> Dhidhdhoo
|
--> Eydhafushi
|
--> Villingili

----Mali
|
--> Bamako
|
--> Sikasso
|
--> Mopti
|
--> Koutiala
|
--> Ségou
|
--> Kayes
|
--> Gao
|
--> Tombouctou
|
--> Niono
|
--> Koulikoro

----Malta
|
--> Valletta
|
--> Birkirkara
|
--> Qormi
|
--> Mosta
|
--> Sliema
|
--> Żabbar
|
--> San Ġwann
|
--> Fgura
|
--> Żebbuġ
|
--> Marsaskala

----Marshall Islands
|
--> Majuro
|
--> Ebeye
|
--> Laura
|
--> Arno
|
--> Delap
|
--> Ajeltake
|
--> Rairok
|
--> Woja
|
--> Uliga
|
--> Jabor

----Mauritania
|
--> Nouakchott
|
--> Nouadhibou
|
--> Rosso
|
--> Kaédi
|
--> Zouerate
|
--> Kiffa
|
--> Atar
|
--> Akjoujt
|
--> Néma
|
--> Sélibaby

----Mauritius
|
--> Port Louis
|
--> Beau Bassin-Rose Hill
|
--> Vacoas-Phoenix
|
--> Curepipe
|
--> Quatre Bornes
|
--> Flic en Flac
|
--> Mahébourg
|
--> Grand Baie
|
--> Goodlands
|
--> Triolet

----Mexico
|
--> Mexico City
|
--> Guadalajara
|
--> Monterrey
|
--> Puebla
|
--> Tijuana
|
--> León
|
--> Ciudad Juárez
|
--> Torreón
|
--> Querétaro
|
--> Mérida

----Micronesia
|
--> Palikir
|
--> Kolonia
|
--> Weno
|
--> Tofol
|
--> Tafunsak
|
--> Lelu
|
--> Utwe
|
--> Malem
|
--> Pingelap
|
--> Moen

----Moldova
|
--> Chișinău
|
--> Bălți
|
--> Tiraspol
|
--> Bender
|
--> Cahul
|
--> Ungheni
|
--> Soroca
|
--> Orhei
|
--> Comrat
|
--> Edineț

----Monaco
|
--> Monaco-Ville
|
--> Monte Carlo
|
--> La Condamine
|
--> Fontvieille
|
--> Moneghetti
|
--> Les Révoires
|
--> Jardin Exotique
|
--> Larvotto
|
--> Saint Michel
|
--> Saint Roman

----Mongolia
|
--> Ulaanbaatar
|
--> Erdenet
|
--> Darkhan
|
--> Choibalsan
|
--> Mörön
|
--> Nalaikh
|
--> Baganuur
|
--> Arvaikheer
|
--> Bayankhongor
|
--> Mandalgovi

----Montenegro
|
--> Podgorica
|
--> Nikšić
|
--> Herceg Novi
|
--> Pljevlja
|
--> Bijelo Polje
|
--> Cetinje
|
--> Bar
|
--> Berane
|
--> Kotor
|
--> Tivat

----Morocco
|
--> Casablanca
|
--> Rabat
|
--> Fes
|
--> Marrakesh
|
--> Tangier
|
--> Agadir
|
--> Meknes
|
--> Oujda
|
--> Kenitra
|
--> Tetouan

----Mozambique
|
--> Maputo
|
--> Matola
|
--> Beira
|
--> Nampula
|
--> Quelimane
|
--> Tete
|
--> Chimoio
|
--> Pemba
|
--> Xai-Xai
|
--> Inhambane

----Myanmar
|
--> Yangon
|
--> Mandalay
|
--> Naypyidaw
|
--> Bago
|
--> Mawlamyine
|
--> Taunggyi
|
--> Monywa
|
--> Pathein
|
--> Sittwe
|
--> Meiktila

----Namibia
|
--> Windhoek
|
--> Walvis Bay
|
--> Swakopmund
|
--> Rundu
|
--> Oshakati
|
--> Katima Mulilo
|
--> Grootfontein
|
--> Otjiwarongo
|
--> Tsumeb
|
--> Rehoboth

----Nauru
|
--> Yaren
|
--> Boe
|
--> Aiwo
|
--> Anetan
|
--> Anabar
|
--> Baiti
|
--> Buada
|
--> Denigomodu
|
--> Ewa
|
--> Meneng

----Nepal
|
--> Kathmandu
|
--> Pokhara
|
--> Lalitpur
|
--> Biratnagar
|
--> Bharatpur
|
--> Birgunj
|
--> Dharan
|
--> Janakpur
|
--> Hetauda
|
--> Bhaktapur

----Netherlands
|
--> Amsterdam
|
--> Rotterdam
|
--> The Hague
|
--> Utrecht
|
--> Eindhoven
|
--> Tilburg
|
--> Groningen
|
--> Almere
|
--> Breda
|
--> Nijmegen

----New Zealand
|
--> Auckland
|
--> Wellington
|
--> Christchurch
|
--> Hamilton
|
--> Tauranga
|
--> Napier-Hastings
|
--> Dunedin
|
--> Palmerston North
|
--> Nelson
|
--> Rotorua

----Nicaragua
|
--> Managua
|
--> León
|
--> Masaya
|
--> Tipitapa
|
--> Chinandega
|
--> Matagalpa
|
--> Estelí
|
--> Granada
|
--> Jinotega
|
--> Bluefields

----Niger
|
--> Niamey
|
--> Zinder
|
--> Maradi
|
--> Agadez
|
--> Tahoua
|
--> Dosso
|
--> Diffa
|
--> Tillabéri
|
--> Arlit
|
--> Birni-N'Konni

----Nigeria
|
--> Lagos
|
--> Abuja
|
--> Kano
|
--> Ibadan
|
--> Port Harcourt
|
--> Benin City
|
--> Maiduguri
|
--> Zaria
|
--> Aba
|
--> Jos

----North Macedonia
|
--> Skopje
|
--> Bitola
|
--> Kumanovo
|
--> Prilep
|
--> Tetovo
|
--> Veles
|
--> Ohrid
|
--> Gostivar
|
--> Štip
|
--> Strumica

----Norway
|
--> Oslo
|
--> Bergen
|
--> Trondheim
|
--> Stavanger
|
--> Drammen
|
--> Fredrikstad
|
--> Kristiansand
|
--> Tromsø
|
--> Sandnes
|
--> Skien

----Oman
|
--> Muscat
|
--> Salalah
|
--> Sohar
|
--> Nizwa
|
--> Sur
|
--> Ibri
|
--> Buraimi
|
--> Rustaq
|
--> Bahla
|
--> Khasab

----Pakistan
|
--> Karachi
|
--> Lahore
|
--> Islamabad
|
--> Rawalpindi
|
--> Faisalabad
|
--> Multan
|
--> Peshawar
|
--> Quetta
|
--> Sialkot
|
--> Gujranwala

----Palau
|
--> Ngerulmud
|
--> Koror
|
--> Airai
|
--> Melekeok
|
--> Ngaraard
|
--> Ngchesar
|
--> Ngatpang
|
--> Aimeliik
|
--> Ngiwal
|
--> Angaur

----Panama
|
--> Panama City
|
--> San Miguelito
|
--> Colón
|
--> David
|
--> La Chorrera
|
--> Santiago
|
--> Chitré
|
--> Penonomé
|
--> Arraiján
|
--> Aguadulce

----Papua New Guinea
|
--> Port Moresby
|
--> Lae
|
--> Mount Hagen
|
--> Madang
|
--> Wewak
|
--> Goroka
|
--> Kokopo
|
--> Arawa
|
--> Kimbe
|
--> Alotau

----Paraguay
|
--> Asunción
|
--> Ciudad del Este
|
--> San Lorenzo
|
--> Luque
|
--> Capiatá
|
--> Lambaré
|
--> Fernando de la Mora
|
--> Encarnación
|
--> Ñemby
|
--> Pedro Juan Caballero

----Peru
|
--> Lima
|
--> Arequipa
|
--> Trujillo
|
--> Chiclayo
|
--> Piura
|
--> Cusco
|
--> Iquitos
|
--> Huancayo
|
--> Puno
|
--> Tacna

----Philippines
|
--> Manila
|
--> Quezon City
|
--> Davao City
|
--> Cebu City
|
--> Zamboanga City
|
--> Antipolo
|
--> Pasig
|
--> Taguig
|
--> Cagayan de Oro
|
--> Bacolod

----Poland
|
--> Warsaw
|
--> Kraków
|
--> Łódź
|
--> Wrocław
|
--> Poznań
|
--> Gdańsk
|
--> Szczecin
|
--> Bydgoszcz
|
--> Lublin
|
--> Katowice

----Portugal
|
--> Lisbon
|
--> Porto
|
--> Vila Nova de Gaia
|
--> Amadora
|
--> Braga
|
--> Coimbra
|
--> Funchal
|
--> Setúbal
|
--> Almada
|
--> Leiria

----Qatar
|
--> Doha
|
--> Al Rayyan
|
--> Al Wakrah
|
--> Al Khor
|
--> Umm Salal
|
--> Al Daayen
|
--> Madinat ash Shamal
|
--> Dukhan
|
--> Mesaieed
|
--> Lusail

----Romania
|
--> Bucharest
|
--> Cluj-Napoca
|
--> Timișoara
|
--> Iași
|
--> Constanța
|
--> Craiova
|
--> Brașov
|
--> Galați
|
--> Ploiești
|
--> Oradea

----Russia
|
--> Moscow
|
--> Saint Petersburg
|
--> Novosibirsk
|
--> Yekaterinburg
|
--> Nizhny Novgorod
|
--> Kazan
|
--> Chelyabinsk
|
--> Omsk
|
--> Samara
|
--> Rostov-on-Don

----Rwanda
|
--> Kigali
|
--> Butare
|
--> Gitarama
|
--> Ruhengeri
|
--> Gisenyi
|
--> Byumba
|
--> Cyangugu
|
--> Rwamagana
|
--> Nyagatare
|
--> Kibuye

----Saint Kitts and Nevis
|
--> Basseterre
|
--> Charlestown
|
--> Sandy Point Town
|
--> Fig Tree
|
--> Monkey Hill
|
--> Cayon
|
--> Dieppe Bay Town
|
--> Newcastle
|
--> Gingerland
|
--> Mansion

----Saint Lucia
|
--> Castries
|
--> Soufrière
|
--> Vieux Fort
|
--> Gros Islet
|
--> Micoud
|
--> Dennery
|
--> Laborie
|
--> Anse La Raye
|
--> Canaries
|
--> Babonneau

----Saint Vincent and the Grenadines
|
--> Kingstown
|
--> Georgetown
|
--> Barrouallie
|
--> Chateaubelair
|
--> Calliaqua
|
--> Bequia
|
--> Layou
|
--> Port Elizabeth
|
--> Union Island
|
--> Mesopotamia

----Samoa
|
--> Apia
|
--> Vaitele
|
--> Faleasiu
|
--> Siusega
|
--> Malie
|
--> Fasito'o-uta
|
--> Leulumoega
|
--> Safotu
|
--> Saleimoa
|
--> Afega

----San Marino
|
--> San Marino
|
--> Serravalle
|
--> Borgo Maggiore
|
--> Domagnano
|
--> Fiorentino
|
--> Acquaviva
|
--> Faetano
|
--> Chiesanuova

----Sao Tome and Principe
|
--> São Tomé
|
--> Santo Amaro
|
--> Neves
|
--> Trindade
|
--> Santana
|
--> São João dos Angolares
|
--> Guadalupe
|
--> Pantufo
|
--> Santa Cruz
|
--> Ribeira Afonso

----Saudi Arabia
|
--> Riyadh
|
--> Jeddah
|
--> Mecca
|
--> Medina
|
--> Dammam
|
--> Khobar
|
--> Tabuk
|
--> Abha
|
--> Buraidah
|
--> Najran

----Senegal
|
--> Dakar
|
--> Touba
|
--> Thiès
|
--> Rufisque
|
--> Saint-Louis
|
--> Kaolack
|
--> Ziguinchor
|
--> Mbour
|
--> Diourbel
|
--> Louga

----Serbia
|
--> Belgrade
|
--> Novi Sad
|
--> Niš
|
--> Kragujevac
|
--> Subotica
|
--> Zrenjanin
|
--> Pančevo
|
--> Čačak
|
--> Smederevo
|
--> Leskovac

----Seychelles
|
--> Victoria
|
--> Anse Boileau
|
--> Beau Vallon
|
--> Bel Ombre
|
--> Cascade
|
--> Glacis
|
--> Grand Anse
|
--> Takamaka
|
--> Baie Lazare
|
--> Mont Fleuri

----Sierra Leone
|
--> Freetown
|
--> Bo
|
--> Kenema
|
--> Makeni
|
--> Koidu
|
--> Lunsar
|
--> Port Loko
|
--> Kabala
|
--> Magburaka
|
--> Waterloo

----Singapore
|
--> Singapore
|
--> Jurong East
|
--> Woodlands
|
--> Tampines
|
--> Yishun
|
--> Bukit Batok
|
--> Hougang
|
--> Sengkang
|
--> Choa Chu Kang
|
--> Pasir Ris

----Slovakia
|
--> Bratislava
|
--> Košice
|
--> Prešov
|
--> Žilina
|
--> Nitra
|
--> Banská Bystrica
|
--> Trnava
|
--> Trenčín
|
--> Martin
|
--> Poprad

----Slovenia
|
--> Ljubljana
|
--> Maribor
|
--> Celje
|
--> Kranj
|
--> Velenje
|
--> Novo Mesto
|
--> Ptuj
|
--> Trbovlje
|
--> Kamnik
|
--> Jesenice

----Solomon Islands
|
--> Honiara
|
--> Gizo
|
--> Auki
|
--> Noro
|
--> Tulagi
|
--> Buala
|
--> Kirakira
|
--> Taro Island
|
--> Lata
|
--> Munda

----Somalia
|
--> Mogadishu
|
--> Hargeisa
|
--> Bosaso
|
--> Kismayo
|
--> Baidoa
|
--> Beledweyne
|
--> Galkayo
|
--> Garowe
|
--> Marka
|
--> Jowhar

----South Africa
|
--> Johannesburg
|
--> Cape Town
|
--> Durban
|
--> Pretoria
|
--> Port Elizabeth
|
--> Bloemfontein
|
--> East London
|
--> Polokwane
|
--> Kimberley
|
--> Nelspruit

----South Sudan
|
--> Juba
|
--> Wau
|
--> Malakal
|
--> Bor
|
--> Yambio
|
--> Rumbek
|
--> Aweil
|
--> Torit
|
--> Bentiu
|
--> Kuajok

----Spain
|
--> Madrid
|
--> Barcelona
|
--> Valencia
|
--> Seville
|
--> Zaragoza
|
--> Málaga
|
--> Murcia
|
--> Palma
|
--> Bilbao
|
--> Alicante

----Sri Lanka
|
--> Colombo
|
--> Kandy
|
--> Galle
|
--> Jaffna
|
--> Negombo
|
--> Trincomalee
|
--> Batticaloa
|
--> Anuradhapura
|
--> Ratnapura
|
--> Matara

----Sudan
|
--> Khartoum
|
--> Omdurman
|
--> Port Sudan
|
--> Kassala
|
--> El Obeid
|
--> Nyala
|
--> Wad Madani
|
--> Atbara
|
--> El Fasher
|
--> Kosti

----Suriname
|
--> Paramaribo
|
--> Lelydorp
|
--> Nieuw Nickerie
|
--> Moengo
|
--> Albina
|
--> Totness
|
--> Wageningen
|
--> Brokopondo
|
--> Groningen
|
--> Brownsweg

----Sweden
|
--> Stockholm
|
--> Gothenburg
|
--> Malmö
|
--> Uppsala
|
--> Västerås
|
--> Örebro
|
--> Linköping
|
--> Helsingborg
|
--> Jönköping
|
--> Norrköping

----Switzerland
|
--> Zurich
|
--> Geneva
|
--> Basel
|
--> Bern
|
--> Lausanne
|
--> Lucerne
|
--> St. Gallen
|
--> Lugano
|
--> Biel/Bienne
|
--> Thun

----Syria
|
--> Damascus
|
--> Aleppo
|
--> Homs
|
--> Latakia
|
--> Hama
|
--> Deir ez-Zor
|
--> Raqqa
|
--> Daraa
|
--> Tartus
|
--> Al-Hasakah

----Taiwan
|
--> Taipei
|
--> Kaohsiung
|
--> Taichung
|
--> Tainan
|
--> Hsinchu
|
--> Keelung
|
--> Chiayi
|
--> Pingtung
|
--> Miaoli
|
--> Yilan

----Tajikistan
|
--> Dushanbe
|
--> Khujand
|
--> Kulob
|
--> Qurghonteppa
|
--> Istaravshan
|
--> Panjakent
|
--> Tursunzoda
|
--> Khorugh
|
--> Vahdat
|
--> Isfara

----Tanzania
|
--> Dar es Salaam
|
--> Dodoma
|
--> Mwanza
|
--> Arusha
|
--> Mbeya
|
--> Morogoro
|
--> Tanga
|
--> Zanzibar City
|
--> Kigoma
|
--> Tabora

----Thailand
|
--> Bangkok
|
--> Chiang Mai
|
--> Nakhon Ratchasima
|
--> Udon Thani
|
--> Pattaya
|
--> Khon Kaen
|
--> Hat Yai
|
--> Surat Thani
|
--> Nakhon Si Thammarat
|
--> Phuket

----Timor-Leste
|
--> Dili
|
--> Baucau
|
--> Maliana
|
--> Suai
|
--> Lospalos
|
--> Aileu
|
--> Ainaro
|
--> Ermera
|
--> Manatuto
|
--> Viqueque

----Togo
|
--> Lomé
|
--> Sokodé
|
--> Kara
|
--> Kpalimé
|
--> Atakpamé
|
--> Tsévié
|
--> Aného
|
--> Dapaong
|
--> Mango
|
--> Notsé

----Tonga
|
--> Nukuʻalofa
|
--> Neiafu
|
--> Pangai
|
--> ʻOhonua
|
--> Haveluloto
|
--> Vaini
|
--> Hihifo
|
--> Lapaha
|
--> Kolonga
|
--> Fuaʻamotu

----Trinidad
|
--> Port of Spain
|
--> San Fernando
|
--> Chaguanas
|
--> Arima
|
--> Point Fortin
|
--> Couva
|
--> Princes Town
|
--> Diego Martin
|
--> Siparia
|
--> Sangre Grande

----Tobago
|
--> Scarborough
|
--> Roxborough
|
--> Charlotteville
|
--> Plymouth
|
--> Speyside
|
--> Goodwood
|
--> Mason Hall
|
--> Bethel
|
--> Lambeau
|
--> Lowlands

----Tunisia
|
--> Tunis
|
--> Sfax
|
--> Sousse
|
--> Kairouan
|
--> Bizerte
|
--> Gabès
|
--> Ariana
|
--> Gafsa
|
--> Monastir
|
--> Nabeul

----Turkey
|
--> Istanbul
|
--> Ankara
|
--> Izmir
|
--> Bursa
|
--> Adana
|
--> Gaziantep
|
--> Konya
|
--> Antalya
|
--> Kayseri
|
--> Mersin

----Turkmenistan
|
--> Ashgabat
|
--> Türkmenabat
|
--> Dashoguz
|
--> Mary
|
--> Balkanabat
|
--> Tejen
|
--> Bayramaly
|
--> Abadan
|
--> Serdar
|
--> Gazanjyk

"""
    )

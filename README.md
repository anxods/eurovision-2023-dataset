# Eurovision 2023 Odds - Web Scraping

Este mini-proyecto consiste en la recopilación de datos de probabilidad de victoria en el Festival de Eurovisión 2023, que se celebrará en Reino Unido el sábado 13 de mayo.

## Funcionamiento

Con la ejecución del archivo escrito en python 'scraping.py', obtendremos diariamente, mediante _web scraping_, los datos de probabilidad de victoria de todas las canciones y artistas participantes, en distintas casas de apuestas.

Los datos, como comentamos, se obtendrán mediante la técnica de _web scraping_, accediendo a la siguiente URL y recogiendo los datos de la tabla que aparece en ella: https://eurovisionworld.com/odds/eurovision

A día 21 de marzo del 2023, las casas de apuestas que aparecen en esta tabla son las siguientes:

- BET365
- UNIBET
- COOL BET
- BETFAIR SPORT
- SKY BET
- BETSSON 
- LAD BROKES
- COMEON
- SMARKETS
- 888 SPORT
- BOYLE SPORTS
- BET FRED
- 10BET
- BETWAY
- WILLIAM HILL
- BETFAIR EXCHANGE
- BWIN

Un ejemplo de tabla que podremos visualizar en los archivos que genere el script es la siguiente:

|date      |position|country       |song                                  |winning chance|BET365|UNIBET|COOL BET|BETFAIR SPORT|SKY BET|BETSSON|LAD BROKES|COMEON|* SMARKETS|888 SPORT|BOYLE SPORTS|BET FRED|10BET|BETWAY|WILLIAM  HILL|BETFAIR*  EXCHANGE|
|----------|--------|--------------|--------------------------------------|--------------|------|------|--------|-------------|-------|-------|----------|------|----------|---------|------------|--------|-----|------|-------------|------------------|
|2023-03-20|1       |Sweden        |Loreen - Tattoo                       |40%           |1.8   |1.73  |1.85    |1.83         |1.83   |1.85   |1.73      |1.8   |1.96      |1.83     |1.8         |1.8     |1.8  |1.91  |1.83         |2.04              |
|2023-03-20|2       |Finland       |Käärijä - Cha Cha Cha                 |14%           |5.5   |4.5   |4.75    |6            |6      |4.5    |5.5       |4     |6.4       |5        |4.5         |5.5     |4    |4     |5.5          |7                 |
|2023-03-20|3       |Ukraine       |Tvorchi - Heart of Steel              |12%           |6.5   |7     |6       |6            |6      |7      |6         |6     |7         |5.5      |5           |6       |6    |7.5   |5            |8                 |
|2023-03-20|4       |Norway        |Alessandra - Queen of Kings           |5%            |15    |13    |15      |15           |15     |13     |15        |15    |17        |13       |15          |17      |15   |19    |13           |20                |
|2023-03-20|5       |Israel        |Noa Kirel - Unicorn                   |4%            |21    |21    |21      |23           |26     |25     |21        |17    |16        |21       |17          |23      |17   |23    |13           |20                |
|2023-03-20|6       |Spain         |Blanca Paloma - Eaea                  |3%            |21    |29    |21      |21           |34     |20     |29        |26    |25        |29       |21          |23      |26   |26    |23           |28                |
|2023-03-20|7       |United Kingdom|Mae Muller - I Wrote A Song           |3%            |29    |34    |41      |34           |26     |30     |26        |29    |44        |14       |23          |26      |29   |26    |17           |50                |
|2023-03-20|8       |Czechia       |Vesna - My Sister's Crown             |2%            |34    |34    |31      |34           |34     |35     |29        |29    |38        |23       |34          |34      |29   |34    |17           |46                |
|2023-03-20|9       |Austria       |Teya & Salena - Who The Hell Is Edgar?|2%            |34    |41    |41      |51           |34     |45     |29        |34    |46        |26       |34          |34      |34   |41    |26           |55                |
|2023-03-20|10      |France        |La Zarra - Évidemment                 |2%            |41    |51    |51      |51           |41     |40     |41        |41    |50        |34       |34          |41      |41   |34    |26           |65                |
|2023-03-20|11      |Italy         |Marco Mengoni - Due vite              |1%            |56    |67    |61      |81           |51     |50     |51        |51    |85        |34       |51          |51      |51   |51    |26           |100               |
|2023-03-20|12      |Armenia       |Brunette - Future Lover               |1%            |41    |67    |81      |81           |81     |75     |51        |41    |100       |51       |41          |67      |41   |41    |34           |130               |
|2023-03-20|13      |Georgia       |Iru - Echo                            |1%            |67    |51    |81      |81           |41     |70     |67        |67    |110       |41       |67          |34      |67   |26    |29           |140               |
|2023-03-20|14      |Switzerland   |Remo Forrer - Watergun                |1%            |67    |81    |81      |51           |81     |70     |81        |67    |100       |41       |51          |67      |67   |67    |51           |130               |
|2023-03-20|15      |Serbia        |Luke Black - Samo mi se spava         |1%            |101   |126   |81      |101          |126    |120    |101       |101   |85        |41       |67          |101     |101  |101   |67           |100               |
|2023-03-20|16      |Croatia       |Let 3 - Mama ŠČ!                      |1%            |101   |101   |101     |151          |126    |120    |101       |101   |190       |34       |81          |101     |101  |101   |41           |220               |
|2023-03-20|17      |Moldova       |Pasha Parfeni - Soarele și Luna       |1%            |126   |101   |101     |151          |151    |125    |101       |101   |200       |101      |81          |101     |101  |126   |101          |230               |
|2023-03-20|18      |Australia     |Voyager - Promise                     |1%            |126   |201   |101     |151          |301    |100    |151       |101   |120       |101      |101         |101     |101  |126   |34           |150               |
|2023-03-20|19      |Netherlands   |Nicolai & Cooper - Burning Daylight   |1%            |151   |151   |151     |151          |201    |150    |151       |151   |220       |101      |101         |101     |151  |151   |34           |250               |
|2023-03-20|20      |Germany       |Lord Of The Lost - Blood & Glitter    |1%            |151   |151   |151     |151          |201    |150    |126       |151   |150       |81       |101         |201     |151  |151   |101          |180               |
|2023-03-20|21      |Estonia       |Alika - Bridges                       |<1%           |201   |201   |101     |201          |201    |150    |201       |201   |200       |51       |151         |201     |201  |201   |67           |230               |
|2023-03-20|22      |Iceland       |Diljá - Power                         |<1%           |151   |151   |101     |251          |201    |120    |201       |201   |280       |101      |126         |201     |201  |151   |101          |620               |
|2023-03-20|23      |Azerbaijan    |TuralTuranX - Tell Me More            |<1%           |151   |201   |301     |201          |201    |200    |201       |151   |280       |101      |101         |201     |151  |151   |101          |800               |
|2023-03-20|24      |Poland        |Blanka - Solo                         |<1%           |201   |201   |201     |151          |301    |150    |201       |201   |260       |201      |101         |201     |201  |151   |21           |360               |
|2023-03-20|25      |Ireland       |Wild Youth - We Are One               |<1%           |201   |251   |251     |151          |301    |250    |151       |151   |280       |101      |67          |201     |151  |201   |101          |780               |
|2023-03-20|26      |Portugal      |Mimicat - Ai Coração                  |<1%           |201   |201   |251     |201          |301    |200    |201       |201   |270       |101      |101         |201     |201  |201   |101          |480               |
|2023-03-20|27      |Cyprus        |A. Lambrou - Break a Broken Heart     |<1%           |201   |251   |201     |251          |301    |200    |201       |201   |280       |67       |151         |201     |201  |201   |101          |800               |
|2023-03-20|28      |Greece        |Victor Vernicos - What They Say       |<1%           |201   |251   |251     |251          |301    |250    |201       |201   |280       |101      |126         |201     |201  |201   |151          |550               |
|2023-03-20|29      |Denmark       |Reiley - Breaking My Heart            |<1%           |201   |251   |251     |201          |301    |250    |201       |201   |280       |101      |201         |201     |201  |201   |151          |730               |
|2023-03-20|30      |Slovenia      |Joker Out - Carpe Diem                |<1%           |251   |251   |151     |251          |301    |250    |251       |201   |280       |151      |201         |201     |201  |251   |67           |480               |
|2023-03-20|31      |Malta         |The Busker - Dance (Our Own Party)    |<1%           |251   |251   |301     |251          |501    |200    |201       |201   |290       |151      |126         |201     |201  |251   |151          |1000              |
|2023-03-20|32      |Belgium       |Gustaph - Because of You              |<1%           |251   |251   |301     |251          |501    |250    |201       |251   |290       |151      |201         |201     |251  |251   |201          |1000              |
|2023-03-20|33      |Lithuania     |Monika Linkytė - Stay                 |<1%           |251   |501   |301     |251          |501    |250    |201       |251   |290       |101      |126         |201     |251  |251   |101          |1000              |
|2023-03-20|34      |San Marino    |Piqued Jacks - Like An Animal         |<1%           |251   |251   |301     |251          |501    |250    |251       |251   |290       |151      |201         |201     |251  |301   |151          |1000              |
|2023-03-20|35      |Latvia        |Sudden Lights - Aijā                  |<1%           |251   |501   |301     |251          |501    |250    |251       |251   |290       |151      |201         |201     |251  |251   |151          |1000              |
|2023-03-20|36      |Albania       |Albina & Familja Kelmendi - Duje      |<1%           |301   |251   |301     |251          |501    |300    |251       |251   |290       |201      |201         |201     |251  |301   |251          |1000              |
|2023-03-20|37      |Romania       |Theodor Andrei - D.G.T. (Off and On)  |<1%           |301   |501   |301     |251          |501    |300    |251       |251   |290       |151      |201         |201     |251  |301   |201          |1000              |

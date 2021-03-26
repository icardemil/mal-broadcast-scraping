# MAL Broadcast Scraping 📅
Utiliza la API Jikan para obtener infomación sobre los animes de temporada y agrega el horario de emisión al modelo de la serie, por medio de web scraping en su perfil de MyAnimeList (MAL). Retorna un archivo JSON con el resultado obtenido.

## Modelo 📄
| Atributo 	| Contenido 	| Ejemplo 	|
|-	|-	|-	|
| title 	| Nombre de anime 	| Shingeki no Kyojin: The Final Season 	|
| img_url 	| Imagen de anime (MAL) 	| https://cdn.myanimelist.net/images/anime/1000/110531.jpg 	|
| synopsis 	| Resumen de anime (MAL) 	| Gabi Braun and Falco Gri… [Written by MAL Rewrite] 	|
| mal_url 	| Página de serie en MyAnimeList 	| https://myanimelist.net/anime/40028/Shingeki_no_Kyojin__The_Final_Season 	|
| day 	| Día de emisión (MAL) 	| Mondays 	|
| hour 	| Hora de emisión 	| 00:10:00 	|
| time 	| Zona horaria 	| JST 	|

## Requisitos ✔️
 Para ejecutar el script se necesitan las siguientes librerías:
 * Beautiful Soup
 * lxml

## Resultado 💙
[Descargar el JSON para la temporada de Inivierno/Winter 2021.](https://github.com/icardemil64/mal-broadcast-scraping/blob/master/anime_schedule.json)
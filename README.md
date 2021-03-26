# MAL Broadcast Scraping 📅
Utiliza la API de [Jikan](https://jikan.moe/) para obtener infomación sobre los animes de temporada y agrega el horario de emisión al modelo de la serie, por medio de web scraping en su perfil de MyAnimeList (MAL). Retorna un archivo JSON con el resultado obtenido.

## Modelo 📄
| Atributo 	| Contenido 	| Ejemplo 	| Fuente 	|
|-	|-	|-	|-	|
| title 	| Nombre de anime 	| Shingeki no Kyojin: The Final Season 	| Jikan 	|
| img_url 	| Imagen de anime 	| https://cdn.myanimelist.net/images/anime/1000/110531.jpg 	| Jikan 	|
| synopsis 	| Resumen de anime 	| Gabi Braun and Falco Gri… [Written by MAL Rewrite] 	| Jikan 	|
| mal_url 	| Página de anime en MyAnimeList 	| https://myanimelist.net/anime/40028/Shingeki_no_Kyojin__The_Final_Season 	| Jikan 	|
| day 	| Día de emisión 	| Mondays 	| Jikan 	|
| hour 	| Hora de emisión 	| 00:10:00 	| Scraping MAL 	|
| time 	| Zona horaria 	| JST 	| Scraping MAL 	|

## Requisitos ✔️
 Para ejecutar el script se necesitan las siguientes librerías:
 * Beautiful Soup
 * lxml

## Resultado 💙
[Descargar el JSON para la temporada de Inivierno/Winter 2021.](https://github.com/icardemil64/mal-broadcast-scraping/blob/master/anime_schedule.json)
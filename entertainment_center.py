# -*- coding: cp1252 -*-

import fresh_tomatoes
import media

ms_dhoni = media.Movie(
 "MS Dhoni", "Ranchi boy MS Dhoni aspire to play cricket for India.",
 "http://fr.web.img6.acsta.net/c_215_290/pictures/16/09/02/15/42/085648.jpg",
 "https://www.youtube.com/watch?v=6L6XqWoS8tw")

# print(ms_dhoni.storyline)
# ms_dhoni.show_trailer()

midnight_in_paris = media.Movie(
 "Midnight in Paris", "Romantic comedy set in Paris about a family.",
 "https://i.ytimg.com/vi/-NoGpkSTK8k/movieposter.jpg",
 "https://www.youtube.com/watch?v=FAfR8omt-CY")

ddlj = media.Movie(
 "Dilwale Dulhaniya Le Jayenge",
 "When Raj (Shahrukh Khan) & Simran (Kajol) fell for each other.",
 "https://i.ytimg.com/vi/IbwjDTOvwG8/movieposter.jpg",
 "https://www.youtube.com/watch?v=c25GKl5VNeY")

junooniyat = media.Movie(
 "Junooniyat",
 "Suhani, a Punjabi woman, falls in love with a passionate army officer.",
 "http://im.rediff.com/movies/2016/jun/10junooniyat.jpg",
 "https://www.youtube.com/watch?v=8vicEGLOEdw")

yeh_jawani = media.Movie(
 "Yeh Jawani Hai Deewani", "Kabir and Naina who fell in love on a trip",
 "http://im.rediff.com/movies/2013/may/28ranbirs-heroines1.jpg",
 "https://www.youtube.com/watch?v=Rbp2XUSeUNE")

sonu = media.Movie(
 "Sonu ke titu ki sweety", "Sonu ke Titu ki Sweety explore.",
 "https://i.imgur.com/5KVoFGY.jpg",
 "https://www.youtube.com/watch?v=M2q64UowX9g")

movies = [ms_dhoni, midnight_in_paris, ddlj, junooniyat, yeh_jawani, sonu]
# print(media.Movie.VALID_RATINGS)
fresh_tomatoes.open_movies_page(movies)



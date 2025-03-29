import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-movie-details',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './movie-details.component.html',
})
export class MovieDetailsComponent implements OnInit {
  movie: any;
  error = '';

  constructor(private route: ActivatedRoute) {}

  async getMovieDetails(movieId: string) {
    try {
      const response = await axios.get(`https://api.themoviedb.org/3/movie/${movieId}?language=fr`, {
        headers: {
          Accept: "application/json",
          Authorization: "Bearer [token]"
        }
      });
      this.movie = response.data;
    } catch (error) {
      this.error = "Erreur lors de la récupération du film";
    }
  }

  ngOnInit() {
    const movieId = this.route.snapshot.paramMap.get("id");
    if (movieId) {
      this.getMovieDetails(movieId);
    }
  }
}

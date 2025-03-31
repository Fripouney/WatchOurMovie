import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-movie-details',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './movie-details.component.html',
})
export class MovieDetailsComponent implements OnInit {
  movie: any;
  error = '';
  viewed = false;

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

  async toggleViewedMovie(userId: string) {
    if (!this.viewed) {
      try {
        await axios.post(`http://localhost:8000/user/${userId}/watched`, {
          user_id: userId,
          movie_id: this.movie.id
        });

      } catch (error) {
        this.error = "Le film n'a pas pu être marqué comme vu";
      }

    } else {

      try {
        await axios.delete(`http://localhost:8080/user/${userId}/watched/${movieId}`);

      } catch (error) {
        this.error = "Le film n'a pas pu être marqué comme non vu";
      }
    }
  }

  async checkIfMovieIsViewed(userId: string) {
    try {
      const response = await axios.get(`http://localhost:8000/user/${userId}/watched/${this.movie.id}`);
      this.viewed = response.data.viewed;
    } catch (error) {
      this.error = "Erreur lors de la vérification du visionnage du film"
    }
  }

  ngOnInit() {
    const movieId = this.route.snapshot.paramMap.get("id");
    if (movieId) {
      this.getMovieDetails(movieId);
    }
  }
}

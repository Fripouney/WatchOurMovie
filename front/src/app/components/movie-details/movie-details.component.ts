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
  token = localStorage.getItem("token");
  tmdbToken = 'TOKEN';

  constructor(private route: ActivatedRoute) {}

  async getMovieDetails(movieId: string) {
    try {
      const response = await axios.get(`https://api.themoviedb.org/3/movie/${movieId}?language=fr`, {
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${this.tmdbToken}`
        }
      });
      this.movie = response.data;
    } catch (error) {
      this.error = "Erreur lors de la récupération du film";
    }
  }

  async toggleViewedMovie() {
    if (this.viewed) {
      try {
        const response = await axios.post("http://localhost:8000/user/watched", 
          { movie_id: this.movie.id },
          { headers: { "Content-Type": "application/json", Authorization: `Bearer ${this.token}` } }
        );

      } catch (error) {
        this.error = "Le film n'a pas pu être marqué comme vu";
      }

    } else {

      try {
        await axios.delete(`http://localhost:8000/user/watched/${this.movie.id}`, {
          headers: {
            Authorization: `Bearer ${this.token}`
          }
        });

      } catch (error) {
        this.error = "Le film n'a pas pu être marqué comme non vu";
      }
    }
  }

  async checkIfMovieIsViewed() {
    try {
      const response = await axios.get(`http://localhost:8000/user/watched/${this.movie.id}`, {
        headers: {
          Authorization: `Bearer ${this.token}`
        }
      });
      this.viewed = response.data.viewed;
    } catch (error) {
      if(axios.isAxiosError(error)) {
        error.response ? this.error = error.response.data : this.error = "Aucune réponse du serveur";
      }
    }
  }

  ngOnInit() {
    const movieId = this.route.snapshot.paramMap.get("id");
    if (movieId) {
      this.getMovieDetails(movieId).then(() => {
        this.checkIfMovieIsViewed();
      });
    }
  }
}

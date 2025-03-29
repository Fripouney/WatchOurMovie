import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-movies',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './movies.component.html',
})
export class MoviesComponent implements OnInit {
  link = "https://api.themoviedb.org/3/movie/popular?language=fr&page=1";
  error = '';
  movies: any[] = [];
  constructor(private router: Router) {}

  // Récupère la liste des films populaires du moment
  // Il peut y avoir plusieurs pages, est-ce nécessaire ?
  async getPopularMovies() {
    try {
      const response = await axios.get(this.link, {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer [token]'
        }
      });
      this.movies = response.data.results; 
    } catch(error) {
      this.error = "Erreur lors de la récupération des films";
    }
  }

  ngOnInit() {
    this.getPopularMovies();
  }

  // Permet de faire des lignes de 5 films
  getMoviesInRows(): any[][] {
    const rows = [];
    for (let i = 0; i < this.movies.length; i += 5) {
      rows.push(this.movies.slice(i, i + 5));
    }
    return rows;
  }

  // Redirige vers la page de détails d'un film
  goToMovieDetails(movieId: number) {
    this.router.navigate(['/films', movieId]);
  }
}
